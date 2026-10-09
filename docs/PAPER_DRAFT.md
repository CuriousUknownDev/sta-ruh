# Structural Correction Under Handoff: Distinguishing Repair, Retention, Transfer, and Prevention in Language-Model Agents

**Michael Aguirre**

## Abstract

Agent evaluations commonly treat a successful retry as evidence that a system has learned from failure. This conflates local repair with retained correction, transfer and prevention. We introduce STA-RUH, an executable benchmark that follows corrections across agent handoffs, context resets, scaffold withdrawal, surface variation and adversarial social pressure. The benchmark records a causal correction chain from delivery and receipt through interpretation, action dependence, authoritative external effect and continued validity. A deterministic environment prevents agent self-report from certifying success. We define measures for immediate repair, handoff retention, artifact-independent transfer, recurrence, false holds, adversarial defection and causal correction completion. A preliminary opaque-codebook pilot increased operational decision accuracy from 33.3% to 100% after provision of an explicit correction artifact, reduced false holds from 80% to 0%, transferred to a fresh agent and resisted incorrect unanimous peers. These results demonstrate artifact-mediated reuse on a small controlled task, not model-weight learning. The preregistered study tests whether Structural Theory of Agency profiles predict held-out recurrence beyond endpoint accuracy, confidence, model size, retrieval and generic judge scores.

## 1. Introduction

A system may correct one answer while remaining structurally unchanged. It may store a lesson without retrieving it, retrieve it without letting it govern action, or act correctly without producing the intended world-state effect. In multi-agent systems, a correction may be written by one agent but lost, mis-scoped or socially overwritten during handoff.

STA-RUH evaluates the complete lifecycle of correction:

\[
\text{detection}\rightarrow\text{diagnosis}\rightarrow\text{repair}\rightarrow\text{retention}\rightarrow\text{transfer}\rightarrow\text{prevention}.
\]

The central hypothesis is that trajectory-level structural evidence predicts recurrence more reliably than immediate endpoint success.

## 2. Structural Theory of Agency

STA proposes eleven diagnostic principles: Initiation, Continuity, Stability, Movement, Integration, Alignment, Renewal, Selection, Repair, Prevention and Accountability/Memory. The benchmark treats them as a profile rather than a compensatory score. A critical failure of Alignment or Accountability cannot be erased by unrelated strengths.

The present work does not assume that all eleven principles are uniquely necessary or sufficient. It tests whether the profile, lifecycle organization or a reduced subset provides incremental predictive value.

## 3. Benchmark

### 3.1 Deterministic environment

Each task contains an initial state, time-indexed events, source metadata and a consequential action. A hidden oracle determines event applicability and authoritative state. Agents may inspect sources, communicate, retrieve artifacts and propose actions. Only the environment executes and verifies effects.

### 3.2 Matched conditions

The nine conditions isolate baseline competence, immediate repair, artifact-mediated retention, fresh-agent handoff, artifact withdrawal, corrupted memory, misleading peers, delayed recurrence and surface transfer.

### 3.3 Evidence chain

The trace distinguishes correction creation, delivery, receipt, interpretation, selection, enactment, effect and checkpoint validity. Missing evidence produces an undetermined attribution rather than presumed success.

## 4. Metrics

Report IRR, HRR, ATR, RR, CCCR, FHR, ADR and HDG with uncertainty intervals. Endpoint accuracy remains separate. Judge-generated principle scores must be audited for presentation invariance and inter-rater agreement.

## 5. Preliminary pilot

In an opaque-codebook pilot, the uncorrected agent safely held when unable to decode authority records, scoring 2/6 operationally and falsely holding 4/5 authorized cases. After receiving a localized applicability rule, the same agent scored 6/6. A fresh agent receiving only the artifact also scored 6/6, compared with 2/6 for a no-memory control. The handoff agent resisted two unanimous incorrect peer recommendations.

The pilot is a feasibility result. The rule remained available, samples were small, only one underlying model family was used, and no delayed or model-weight retention was shown.

## 6. Confirmatory study

The confirmatory study spans at least four model families, two open-weight families, multiple architectures, balanced actions, repeated trials and blinded held-out families. Mixed-effects models compare STA measures with conventional predictors of recurrence.

## 7. Limitations and falsification

The benchmark may show that a reduced subset explains recurrence as well as the full framework. Artifact-mediated correction may reflect reliable instruction following rather than learning. Synthetic authority tasks may not generalize to open-ended environments. Judge-based principle scoring may introduce construct instability. Each is treated as a testable limitation rather than hidden in an aggregate score.

## 8. Conclusion

Reliable correction requires more than a better second answer. It requires a supported rule to reach the responsible component, govern selection, produce a verified effect and remain effective when the original failure returns. STA-RUH makes those distinctions executable and falsifiable.

