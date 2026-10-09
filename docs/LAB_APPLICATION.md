# Lab application positioning

## One-sentence identity

Independent agent-evaluation researcher building executable tests of whether corrections survive handoff, context reset, scaffold withdrawal and adversarial recurrence.

## Short research pitch

Current agent benchmarks often credit successful retries without determining whether the correction persists or causally governs later action. I developed STA-RUH, a deterministic benchmark that follows a correction from receipt through interpretation, action dependence, authoritative external effect and recurrence. A preliminary controlled pilot produced a 66.7-point accuracy improvement after an explicit corrective artifact and transferred the effect to a fresh agent, while clearly separating artifact-mediated reuse from internalized learning. I am now building a preregistered multi-model replication.

## What to show

1. Public repository with one-command reproduction.
2. A figure showing baseline, corrected, handoff and artifact-withdrawal performance.
3. Calibration and recurrence prediction on held-out families.
4. Failure examples where endpoint success and causal correction disagree.
5. A concise limitations section stating what would falsify or compress STA.

## Target roles

- evaluation research engineer;
- benchmark or task-development engineer;
- model-behavior researcher;
- agent safeguards or alignment evaluations;
- research fellowship or residency.

## Outreach note

Subject: Evaluation for correction durability under agent handoff

I am building an open benchmark that measures whether an agent correction survives handoff, context reset, scaffold withdrawal and adversarial recurrence. The benchmark uses an authoritative state machine and separates artifact-mediated reuse from internalized correction. A small pilot improved operational accuracy from 33.3% to 100% after a corrective artifact and transferred to a fresh agent; the current work is a preregistered multi-model replication. I would value feedback on the artifact-withdrawal and recurrence controls. Repository: [link]. Two-page summary: [link].

## Readiness checklist

- [ ] At least four model families
- [ ] Frozen held-out scenario families
- [ ] Three or more repetitions per cell
- [ ] Public code and trace schema
- [ ] Preregistered hypotheses
- [ ] Independent scoring audit
- [ ] Reproducible environment hashes
- [ ] Paper or technical report
- [ ] Two-minute demo
- [ ] One-page research resume

