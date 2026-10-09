from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Literal

Decision = Literal["EXECUTE", "HOLD", "ESCALATE"]
State = Literal["ACTIVE", "REVOKED"]
Condition = Literal[
    "baseline",
    "immediate_retry",
    "artifact_retained",
    "fresh_handoff",
    "artifact_withdrawn",
    "corrupted_artifact",
    "misleading_peers",
    "delayed_recurrence",
    "surface_transfer",
]


@dataclass(frozen=True)
class Event:
    sequence: int
    state: State
    glyph: str
    issuer: str
    channel: str
    activation: int
    source_id: str


@dataclass(frozen=True)
class Rule:
    glyph: str
    issuers: tuple[str, ...]
    channel: str

    def applicable(self, event: Event, decision_time: int) -> bool:
        return (
            event.glyph == self.glyph
            and event.issuer in self.issuers
            and event.channel == self.channel
            and event.activation <= decision_time
        )


@dataclass
class Scenario:
    scenario_id: str
    family_id: str
    condition: Condition
    decision_time: int
    initial_state: State
    events: list[Event]
    correction_artifact: dict[str, Any] | None = None
    peer_messages: list[str] = field(default_factory=list)
    surface: str = "procurement"
    expected_decision: Decision | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class AgentDecision:
    scenario_id: str
    decision: Decision
    inspected_sources: list[str] = field(default_factory=list)
    cited_event_sequences: list[int] = field(default_factory=list)
    artifact_used: bool = False
    peer_claim_used: bool = False
    rationale: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class Trace:
    scenario_id: str
    condition: str
    agent_id: str
    model: str
    repetition: int
    decision: AgentDecision
    pre_state: State
    post_state: State
    effect_verified: bool
    effect_valid_at_checkpoint: bool
    expected_decision: Decision
    correct: bool
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

