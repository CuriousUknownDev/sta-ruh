from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from typing import Iterable

from .schema import Event, Rule, Scenario, Trace


def write_json(path: str | Path, value: object) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, indent=2, sort_keys=True), encoding="utf-8")


def write_jsonl(path: str | Path, values: Iterable[dict]) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8") as handle:
        for value in values:
            handle.write(json.dumps(value, sort_keys=True) + "\n")


def read_jsonl(path: str | Path) -> list[dict]:
    with Path(path).open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def manifest_to_dict(rule: Rule, scenarios: list[Scenario]) -> dict:
    return {"rule": asdict(rule), "scenarios": [scenario.to_dict() for scenario in scenarios]}


def manifest_from_dict(payload: dict) -> tuple[Rule, list[Scenario]]:
    rule_data = payload["rule"]
    rule = Rule(rule_data["glyph"], tuple(rule_data["issuers"]), rule_data["channel"])
    scenarios = []
    for raw in payload["scenarios"]:
        raw = dict(raw)
        raw["events"] = [Event(**event) for event in raw["events"]]
        scenarios.append(Scenario(**raw))
    return rule, scenarios


def trace_from_dict(raw: dict) -> Trace:
    from .schema import AgentDecision

    raw = dict(raw)
    raw["decision"] = AgentDecision(**raw["decision"])
    return Trace(**raw)

