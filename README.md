# STA-RUH

**Structural Theory of Agency — Recurrence Under Handoff**

STA-RUH is an executable evaluation framework for distinguishing:

- successful retry from repair;
- repair from retained correction;
- artifact-mediated correction from internalized correction;
- retained correction from cross-context transfer;
- transfer from durable prevention.

The benchmark uses deterministic state machines. Agents may propose actions and claim success, but only the environment can change or certify authoritative state.

## Core experiment

Each scenario is evaluated through a lifecycle:

1. `baseline` — no corrective artifact;
2. `immediate_retry` — feedback is supplied;
3. `artifact_retained` — an explicit correction is available;
4. `fresh_handoff` — a new agent receives only the correction artifact;
5. `artifact_withdrawn` — prior exposure, but no correction at deployment;
6. `corrupted_artifact` — a plausible unsupported rule competes with the valid rule;
7. `misleading_peers` — peers advocate the wrong action;
8. `delayed_recurrence` — unrelated episodes intervene before recurrence;
9. `surface_transfer` — labels and domain change while causal structure is preserved.

## Quick start

```bash
python -m venv .venv
. .venv/bin/activate
pip install -e .
python -m sta_ruh.cli generate --seed 7 --families 12 --output runs/manifest.json
python -m sta_ruh.cli export-prompts --manifest runs/manifest.json --output runs/prompts.jsonl
python -m sta_ruh.cli demo --manifest runs/manifest.json --output runs/demo.jsonl
python -m sta_ruh.cli score --traces runs/demo.jsonl --output runs/summary.json
```

The `demo` runner is a deterministic policy baseline used only to verify benchmark mechanics. It is not an LLM result.

## Model integration

Run `export-prompts` and submit the resulting JSONL to any provider or local inference harness, then convert returned decisions to the trace schema in `docs/TRACE_SCHEMA.md`. Alternatively implement `AgentAdapter.decide()` in `src/sta_ruh/adapters.py`. Keep prompts, raw responses, parsed actions, tool calls, correction artifacts and authoritative state transitions.

The public manifest contains oracle labels for auditability. Never send it directly to a model. The exporter creates a model-visible projection that omits the latent rule and expected decision. For a sealed study, keep the labeled manifest with the evaluator and distribute only `prompts.jsonl`.

## Primary outcomes

- Immediate Repair Rate (IRR)
- Handoff Retention Rate (HRR)
- Artifact-Withdrawal Transfer Rate (ATR)
- Recurrence Rate (RR)
- Causal Correction Completion Rate (CCCR)
- False-Hold Rate (FHR)
- Adversarial Defection Rate (ADR)
- Harness-Dependency Gap (HDG)

STA principle scores remain an eleven-dimensional profile. They are not collapsed into a single compensatory score by default.

## Research status

The included pilot is preliminary. It demonstrated artifact-mediated reuse in a small opaque-codebook task, not model-weight learning. Publication-grade claims require preregistered multi-model replication, repeated trials, delayed retesting and authoritative execution.

## Repository map

- `src/sta_ruh/` — environment, scenario generation, scoring and CLI
- `configs/study_v1.json` — preregistered study configuration
- `docs/PREREGISTRATION.md` — hypotheses and analysis plan
- `docs/PAPER_DRAFT.md` — manuscript starter
- `docs/TRACE_SCHEMA.md` — required trajectory fields
- `docs/LAB_APPLICATION.md` — research pitch and application positioning
- `tests/` — deterministic validation tests

## License

Apache-2.0. See `LICENSE`.

