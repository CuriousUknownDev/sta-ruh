# STA-RUH-01 preregistration draft

## Research question

Can a structural profile of an agent system predict whether a correction will survive handoff, context reset, scaffold withdrawal, task variation and adversarial pressure better than conventional endpoint measures?

## Confirmatory hypotheses

**H1 — Repair is insufficient.** Immediate retry success will exceed delayed, reset recurrence success.

**H2 — Causal use matters.** Correction retrieval without evidence that the rule influenced action will not predict non-recurrence as strongly as the complete receipt–interpretation–selection–effect chain.

**H3 — Artifact-mediated retention.** A verified correction artifact will increase fresh-agent handoff accuracy relative to a no-artifact control.

**H4 — Internalization is distinct.** Performance after artifact withdrawal will be lower than performance with the artifact retained unless the correction has been internalized.

**H5 — Provenance protects selection.** Supported artifacts will outperform equally plausible corrupted artifacts, especially under peer consensus favoring the corrupted rule.

**H6 — STA predicts recurrence.** A preregistered STA structural profile will predict held-out recurrence beyond initial accuracy, confidence, model size, immediate retry success, retrieval rate and a generic trajectory-judge score.

## Primary estimands

- IRR: correct immediate retry after feedback.
- HRR: correct action by a fresh handoff agent receiving only the artifact.
- ATR: correct action after prior exposure with the artifact absent at deployment.
- RR: recurrence of the original structural failure on held-out variants.
- CCCR: complete receipt, interpretation, causal enactment and verified persistent effect.
- FHR: authorized actions incorrectly held or escalated.
- ADR: initially correct decisions abandoned under unsupported peer pressure.
- HDG: performance difference between richer and reduced scaffolds.

## Design

Use matched scenario families. Each family shares a latent causal rule while varying names, domain, ordering and representation. Conditions are assigned within family. Expected actions are balanced. Each cell is repeated at least three times per model configuration.

The authoritative environment executes decisions and records state. Agent claims never establish success. Uncertainty is retained as a behavioral outcome; a safe hold may avoid harm but still incur utility cost.

`artifact_withdrawn` and `delayed_recurrence` deliberately omit the artifact at decision time. For API models without persistent learning, these conditions test rule-absent behavioral transfer within the declared memory regime; they must not be described as weight-level internalization. Fresh sessions are the conservative default. Any provider-side memory or fine-tuning is a separate, explicitly labeled intervention.

## Primary analysis

Fit a mixed-effects logistic model predicting held-out recurrence, with random intercepts for scenario family and model configuration. Compare nested specifications:

1. conventional controls only;
2. controls plus individual STA principle scores;
3. controls plus lifecycle-chain measures;
4. reduced STA subsets selected only in the development split.

Report held-out log loss, Brier score, AUROC, calibration and likelihood-ratio comparisons. Bootstrap confidence intervals by scenario family. Do not choose the eleven-principle specification based on test-set performance.

## Failure and falsification criteria

STA is weakened if:

- a substantially smaller feature set predicts recurrence equally well;
- independent raters cannot score principles reliably;
- STA scores are unstable under meaning-preserving presentation changes;
- high profiles fail to predict non-recurrence;
- systems lacking a claimed necessary principle still show durable correction;
- artifact retrieval alone performs as well as the proposed causal chain.

## Exclusions

Exclude only confirmed transport failures and malformed records after two parser retries. Do not exclude refusals, uncertainty, timeouts, tool errors caused by the agent, or failures to retrieve the correction.

## Confirmatory boundary

All new task generation, model selection, sample size, exclusions, scoring rules and primary regressions must be frozen before opening held-out labels. Pilot results are never pooled into confirmatory estimates.

