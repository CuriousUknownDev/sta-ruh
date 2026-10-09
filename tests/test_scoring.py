import unittest

from sta_ruh.schema import AgentDecision, Trace
from sta_ruh.scoring import summarize


def row(condition, expected, actual, correct):
    return Trace(
        scenario_id=condition,
        condition=condition,
        agent_id="a",
        model="m",
        repetition=1,
        decision=AgentDecision(scenario_id=condition, decision=actual),
        pre_state="ACTIVE" if expected == "EXECUTE" else "REVOKED",
        post_state="ACTIVE" if expected == "EXECUTE" else "REVOKED",
        effect_verified=correct,
        effect_valid_at_checkpoint=correct,
        expected_decision=expected,
        correct=correct,
    )


class ScoringTests(unittest.TestCase):
    def test_false_hold_rate_and_artifact_gain(self):
        result = summarize(
            [
                row("baseline", "EXECUTE", "HOLD", False),
                row("artifact_retained", "EXECUTE", "EXECUTE", True),
            ]
        )
        self.assertEqual(result["conditions"]["baseline"]["false_hold_rate"], 1.0)
        self.assertEqual(result["derived"]["artifact_gain"], 1.0)


if __name__ == "__main__":
    unittest.main()

