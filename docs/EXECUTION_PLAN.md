# STA-RUH-01 execution plan

## What is complete

- Deterministic authoritative environment and oracle resolver
- Balanced matched-family scenario generator
- Nine preregistered evaluation conditions
- Model-visible prompt export with oracle-label isolation
- Trace schema and non-compensatory outcome scoring
- Mechanical reference run over 360 cases
- Preregistration, paper starter and lab-facing research pitch

## What must happen before a public empirical claim

1. Freeze this repository and record its commit or archive checksum.
2. Generate the confirmatory manifest once with seed `20261009`.
3. Seal the labeled manifest; provide models only `model_prompts.jsonl`.
4. Run at least four model families, including two open-weight families.
5. Use three repetitions per model/configuration/case with temperature 0.2.
6. Preserve raw provider responses and parser failures.
7. Have an independent evaluator audit a stratified trace sample before labels open.
8. Score the immutable traces, bootstrap by family, and fit the preregistered recurrence models.
9. Report all exclusions and all nine conditions, including null results.

## Recommended first replication matrix

| Layer | Minimum design | Purpose |
|---|---:|---|
| Model families | 4 | Test cross-family robustness |
| Open-weight families | 2 | Permit reproducibility and mechanistic follow-up |
| Scenario families | 40 | Support family-clustered inference |
| Conditions | 9 | Separate retry, retention, transfer and recurrence |
| Repetitions | 3 | Estimate sampling instability |
| Total decisions | 4,320 | 4 × 40 × 9 × 3 |

Model names should be chosen and frozen immediately before execution so the study tests available systems without post-result selection.

## Pass/fail milestones

- **M1 — Mechanics:** all unit tests pass and oracle accuracy is 100%.
- **M2 — Leakage:** a prompt audit finds no expected decisions or evaluator-only rule objects.
- **M3 — Reliability:** fewer than 2% transport/parser failures after the stated retry policy.
- **M4 — Measurement:** independent trace raters achieve acceptable agreement on STA labels.
- **M5 — Scientific value:** correction lifecycle measures improve held-out recurrence prediction beyond endpoint controls, or the null result is reported as a constraint on STA.

## Lab-entry strategy

Use the project as evidence of research engineering and epistemic discipline, not as proof that STA is already established.

1. Publish the repository with a tagged preregistration snapshot.
2. Post a two-page technical note containing the design, one core figure and explicit falsifiers.
3. Record a two-minute demo: generate → export → model response → authoritative execution → score.
4. Ask evaluation researchers for one narrow critique: whether artifact withdrawal and recurrence are cleanly separated.
5. Apply to evaluation research engineer, model-behavior, benchmark, agent-safety and residency roles with the same reproducible package.

The strongest application sentence is: “I build tests that distinguish a successful retry from a correction that survives handoff, scaffold withdrawal and recurrence.”

## Claims permitted now

- STA-RUH is an executable proposed measurement framework.
- The environment and scorer have passed deterministic mechanical validation.
- Earlier small runs suggest artifact-mediated correction and motivate replication.

## Claims not yet permitted

- STA has been validated across model families.
- The correction was internalized into model weights.
- STA outpredicts conventional evaluation metrics.
- The pilot establishes general durable agency.
