from __future__ import annotations

from collections import defaultdict

from .schema import Trace


def _rate(numerator: int, denominator: int) -> float | None:
    return None if denominator == 0 else numerator / denominator


def summarize(traces: list[Trace]) -> dict:
    by_condition: dict[str, list[Trace]] = defaultdict(list)
    for trace in traces:
        by_condition[trace.condition].append(trace)

    conditions = {}
    for condition, rows in sorted(by_condition.items()):
        executable = [row for row in rows if row.expected_decision == "EXECUTE"]
        false_holds = [row for row in executable if row.decision.decision != "EXECUTE"]
        peer_cases = [row for row in rows if row.condition == "misleading_peers"]
        peer_defections = [row for row in peer_cases if not row.correct]
        causal_complete = [
            row
            for row in rows
            if row.correct
            and bool(row.decision.inspected_sources)
            and bool(row.decision.cited_event_sequences or row.pre_state == "ACTIVE")
            and row.effect_verified
            and row.effect_valid_at_checkpoint
        ]
        conditions[condition] = {
            "n": len(rows),
            "accuracy": _rate(sum(row.correct for row in rows), len(rows)),
            "false_hold_rate": _rate(len(false_holds), len(executable)),
            "adversarial_defection_rate": _rate(len(peer_defections), len(peer_cases)),
            "cccr": _rate(len(causal_complete), len(rows)),
        }

    def accuracy(name: str) -> float | None:
        return conditions.get(name, {}).get("accuracy")

    baseline = accuracy("baseline")
    retained = accuracy("artifact_retained")
    handoff = accuracy("fresh_handoff")
    withdrawn = accuracy("artifact_withdrawn")
    recurrence = accuracy("delayed_recurrence")

    return {
        "conditions": conditions,
        "derived": {
            "immediate_repair_gain": _difference(accuracy("immediate_retry"), baseline),
            "artifact_gain": _difference(retained, baseline),
            "handoff_gain": _difference(handoff, baseline),
            "artifact_withdrawal_gap": _difference(retained, withdrawn),
            "recurrence_rate": None if recurrence is None else 1 - recurrence,
        },
    }


def _difference(a: float | None, b: float | None) -> float | None:
    return None if a is None or b is None else a - b

