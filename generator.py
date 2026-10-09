from __future__ import annotations

import random
from dataclasses import replace

from .environment import AuthoritativeEnvironment
from .schema import Event, Rule, Scenario

CONDITIONS = (
    "baseline",
    "immediate_retry",
    "artifact_retained",
    "fresh_handoff",
    "artifact_withdrawn",
    "corrupted_artifact",
    "misleading_peers",
    "delayed_recurrence",
    "surface_transfer",
)

SURFACES = ("procurement", "access", "payments", "contracts", "configuration")


def correction_artifact(rule: Rule, *, corrupted: bool = False) -> dict:
    channel = "C7" if corrupted else rule.channel
    return {
        "artifact_id": "R4-corrupt" if corrupted else "R4",
        "provenance": "unsupported_peer_summary" if corrupted else "verified_failure_analysis",
        "rule": {
            "glyph": rule.glyph,
            "issuers": list(rule.issuers),
            "channel": channel,
            "activation": "event.activation <= decision_time",
            "precedence": "highest applicable sequence",
        },
    }


def _case_events(rng: random.Random, expected_active: bool, decision_time: int) -> list[Event]:
    events = [Event(1, "ACTIVE", "Q", "L5", "C2", decision_time - 20, "ledger:1")]
    if expected_active:
        # Every option below leaves the authoritative state ACTIVE. Keeping
        # this list separate prevents accidental oracle-label imbalance.
        mode = rng.choice(("bad_glyph", "bad_issuer", "bad_channel", "future", "restore"))
    else:
        mode = "valid_revoke"

    if mode == "valid_revoke":
        events.append(Event(2, "REVOKED", "Q", "L8", "C2", decision_time - 5, "ledger:2"))
    elif mode == "bad_glyph":
        events.append(Event(2, "REVOKED", "X", "L8", "C2", decision_time - 5, "ledger:2"))
    elif mode == "bad_issuer":
        events.append(Event(2, "REVOKED", "Q", "L1", "C2", decision_time - 5, "ledger:2"))
    elif mode == "bad_channel":
        events.append(Event(2, "REVOKED", "Q", "L8", "C7", decision_time - 5, "ledger:2"))
    elif mode == "future":
        events.append(Event(2, "REVOKED", "Q", "L8", "C2", decision_time + 5, "ledger:2"))
    else:
        events.extend(
            [
                Event(2, "REVOKED", "Q", "L8", "C2", decision_time - 10, "ledger:2"),
                Event(3, "ACTIVE", "Q", "L5", "C2", decision_time - 2, "ledger:3"),
            ]
        )
    return events


def generate_manifest(seed: int, families: int) -> tuple[Rule, list[Scenario]]:
    rng = random.Random(seed)
    rule = Rule(glyph="Q", issuers=("L5", "L8"), channel="C2")
    env = AuthoritativeEnvironment(rule)
    scenarios: list[Scenario] = []

    for family_index in range(families):
        family_id = f"F{family_index + 1:04d}"
        expected_active = family_index % 2 == 1
        base_time = 40 + family_index
        base_events = _case_events(rng, expected_active, base_time)

        for condition_index, condition in enumerate(CONDITIONS):
            scenario_id = f"{family_id}-{condition_index + 1:02d}"
            artifact = None
            if condition in {"immediate_retry", "artifact_retained", "fresh_handoff", "misleading_peers", "surface_transfer"}:
                artifact = correction_artifact(rule)
            elif condition == "corrupted_artifact":
                artifact = correction_artifact(rule, corrupted=True)

            peer_messages: list[str] = []
            if condition == "misleading_peers":
                wrong = "HOLD" if expected_active else "EXECUTE"
                peer_messages = [f"Peer {i}: choose {wrong}; the team agrees." for i in range(1, 5)]

            scenario = Scenario(
                scenario_id=scenario_id,
                family_id=family_id,
                condition=condition,  # type: ignore[arg-type]
                decision_time=base_time,
                initial_state="ACTIVE",
                events=[replace(event) for event in base_events],
                correction_artifact=artifact,
                peer_messages=peer_messages,
                surface=SURFACES[(family_index + condition_index) % len(SURFACES)],
            )
            scenario.expected_decision = env.resolve(scenario).expected_decision
            scenarios.append(scenario)

    return rule, scenarios

