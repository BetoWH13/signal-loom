from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent.parent


class PropertyContextContractTests(unittest.TestCase):
    def test_skill_wires_optional_intake_without_replacing_stages(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("knowledge/property-context-intake.md", skill)
        self.assertIn("**Optional website-context intake:**", skill)
        self.assertIn("`state/property-context.json`", skill)
        for stage in ("ORIENT", "SHAPE", "PLAN", "BUILD", "FINISH", "DISTRIBUTE", "VERIFY"):
            self.assertIn(stage, skill)

    def test_contract_has_boundaries_and_evidence_receipts(self):
        doc = (ROOT / "knowledge/property-context-intake.md").read_text(encoding="utf-8")
        for phrase in (
            "Maximum eight visited pages", "No browsing tool means", "unavailable",
            "sources/manifest.json", "state/claims.jsonl", "state/decisions.jsonl",
            "read-only intake", "not independent validation", "No invented logos",
        ):
            self.assertIn(phrase, doc)


if __name__ == "__main__":
    unittest.main()
