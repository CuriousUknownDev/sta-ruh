from __future__ import annotations

import argparse
import json
from pathlib import Path

from .adapters import OracleAdapter
from .environment import AuthoritativeEnvironment
from .generator import generate_manifest
from .io import manifest_from_dict, manifest_to_dict, read_jsonl, trace_from_dict, write_json, write_jsonl
from .prompting import SYSTEM_PROMPT, scenario_prompt
from .scoring import summarize


def generate(args: argparse.Namespace) -> None:
    rule, scenarios = generate_manifest(args.seed, args.families)
    write_json(args.output, manifest_to_dict(rule, scenarios))


def demo(args: argparse.Namespace) -> None:
    payload = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    rule, scenarios = manifest_from_dict(payload)
    environment = AuthoritativeEnvironment(rule)
    adapter = OracleAdapter(environment)
    traces = []
    for scenario in scenarios:
        decision = adapter.decide(scenario)
        trace = environment.execute(
            scenario,
            decision,
            agent_id="mechanical-oracle",
            model="not-a-model-result",
            repetition=1,
        )
        traces.append(trace.to_dict())
    write_jsonl(args.output, traces)


def score(args: argparse.Namespace) -> None:
    raw = read_jsonl(args.traces)
    traces = [trace_from_dict(item) for item in raw]
    write_json(args.output, summarize(traces))


def export_prompts(args: argparse.Namespace) -> None:
    payload = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    _, scenarios = manifest_from_dict(payload)
    rows = [
        {
            "custom_id": scenario.scenario_id,
            "condition": scenario.condition,
            "family_id": scenario.family_id,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": scenario_prompt(scenario)},
            ],
        }
        for scenario in scenarios
    ]
    write_jsonl(args.output, rows)


def main() -> None:
    parser = argparse.ArgumentParser(prog="sta-ruh")
    subparsers = parser.add_subparsers(required=True)

    generate_parser = subparsers.add_parser("generate")
    generate_parser.add_argument("--seed", type=int, default=7)
    generate_parser.add_argument("--families", type=int, default=12)
    generate_parser.add_argument("--output", required=True)
    generate_parser.set_defaults(func=generate)

    demo_parser = subparsers.add_parser("demo")
    demo_parser.add_argument("--manifest", required=True)
    demo_parser.add_argument("--output", required=True)
    demo_parser.set_defaults(func=demo)

    score_parser = subparsers.add_parser("score")
    score_parser.add_argument("--manifest", required=False)
    score_parser.add_argument("--traces", required=True)
    score_parser.add_argument("--output", required=True)
    score_parser.set_defaults(func=score)

    prompt_parser = subparsers.add_parser("export-prompts")
    prompt_parser.add_argument("--manifest", required=True)
    prompt_parser.add_argument("--output", required=True)
    prompt_parser.set_defaults(func=export_prompts)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

