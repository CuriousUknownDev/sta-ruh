import unittest

from sta_ruh.environment import AuthoritativeEnvironment
from sta_ruh.schema import AgentDecision, Event, Rule, Scenario


def make_scenario(events):
    return Scenario(
        scenario_id="test",
        family_id="family",
        condition="baseline",
        decision_time=40,
        initial_state="ACTIVE",
        events=events,
    )


class EnvironmentTests(unittest.TestCase):
    def setUp(self):
        self.env = AuthoritativeEnvironment(Rule("Q", ("L5", "L8"), "C2"))

    def test_invalid_event_does_not_revoke(self):
        scenario = make_scenario([Event(2, "REVOKED", "X", "L8", "C2", 35, "s")])
        self.assertEqual(self.env.resolve(scenario).expected_decision, "EXECUTE")

    def test_latest_applicable_event_controls(self):
        scenario = make_scenario(
            [
                Event(1, "REVOKED", "Q", "L8", "C2", 20, "s1"),
                Event(2, "ACTIVE", "Q", "L5", "C2", 30, "s2"),
            ]
        )
        self.assertEqual(self.env.resolve(scenario).expected_decision, "EXECUTE")

    def test_authoritative_execution_rejects_unauthorized_action(self):
        scenario = make_scenario([Event(2, "REVOKED", "Q", "L8", "C2", 35, "s")])
        decision = AgentDecision(scenario_id="test", decision="EXECUTE")
        trace = self.env.execute(scenario, decision, agent_id="a", model="m", repetition=1)
        self.assertFalse(trace.correct)
        self.assertFalse(trace.effect_verified)


if __name__ == "__main__":
    unittest.main()

