import unittest

from sta_ruh.generator import CONDITIONS, generate_manifest


class GeneratorTests(unittest.TestCase):
    def test_balanced_expected_decisions_in_every_condition(self):
        _, scenarios = generate_manifest(seed=17, families=20)
        for condition in CONDITIONS:
            labels = [row.expected_decision for row in scenarios if row.condition == condition]
            self.assertEqual(labels.count("EXECUTE"), 10)
            self.assertEqual(labels.count("HOLD"), 10)

    def test_oracle_labels_are_populated(self):
        _, scenarios = generate_manifest(seed=2, families=4)
        self.assertTrue(all(row.expected_decision in {"EXECUTE", "HOLD"} for row in scenarios))


if __name__ == "__main__":
    unittest.main()
