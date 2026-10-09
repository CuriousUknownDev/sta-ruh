from __future__ import annotations

from abc import ABC, abstractmethod

from .environment import AuthoritativeEnvironment
from .schema import AgentDecision, Scenario


class AgentAdapter(ABC):
    @abstractmethod
    def decide(self, scenario: Scenario) -> AgentDecision:
        raise NotImplementedError


class OracleAdapter(AgentAdapter):
    """Mechanical benchmark validator; never report as an LLM result."""

    def __init__(self, environment: AuthoritativeEnvironment):
        self.environment = environment

    def decide(self, scenario: Scenario) -> AgentDecision:
        resolution = self.environment.resolve(scenario)
        cited = [] if resolution.controlling_sequence is None else [resolution.controlling_sequence]
        return AgentDecision(
            scenario_id=scenario.scenario_id,
            decision=resolution.expected_decision,
            inspected_sources=[event.source_id for event in scenario.events],
            cited_event_sequences=cited,
            artifact_used=scenario.correction_artifact is not None,
            peer_claim_used=False,
            rationale="Deterministic oracle decision for mechanical validation only.",
        )


class AlwaysHoldAdapter(AgentAdapter):
    def decide(self, scenario: Scenario) -> AgentDecision:
        return AgentDecision(scenario_id=scenario.scenario_id, decision="HOLD", rationale="Always-hold baseline")

