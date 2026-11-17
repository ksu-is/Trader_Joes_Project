"""Offline tests for the public, standalone market summary demo."""

import tempfile
import unittest
from pathlib import Path

from demo.market_summary import summarize_csv


class SummaryTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / "sample.csv"

    def write_csv(self, body):
        self.path.write_text(body, encoding="utf-8")

    def test_summary(self):
        self.write_csv(
            "date,close,volume\n"
            "2026-01-05,100,10\n"
            "2026-01-06,110,20\n"
        )
        result = summarize_csv(self.path)
        self.assertEqual(result["observations"], 2)
        self.assertEqual(result["total_volume"], 30)
        self.assertAlmostEqual(result["percent_change"], 10.0)

    def test_missing_columns_rejected(self):
        self.write_csv("date,price\n2026-01-05,100\n")
        with self.assertRaises(ValueError):
            summarize_csv(self.path)

    def test_nonfinite_values_rejected(self):
        self.write_csv(
            "date,close,volume\n"
            "2026-01-05,100,10\n"
            "2026-01-06,nan,20\n"
        )
        with self.assertRaises(ValueError):
            summarize_csv(self.path)

    def test_duplicate_date_rejected(self):
        self.write_csv(
            "date,close,volume\n"
            "2026-01-05,100,10\n"
            "2026-01-05,110,20\n"
        )
        with self.assertRaises(ValueError):
            summarize_csv(self.path)

    def test_single_row_rejected(self):
        self.write_csv("date,close,volume\n2026-01-05,100,10\n")
        with self.assertRaises(ValueError):
            summarize_csv(self.path)

    def test_negative_volume_rejected(self):
        self.write_csv(
            "date,close,volume\n"
            "2026-01-05,100,10\n"
            "2026-01-06,110,-1\n"
        )
        with self.assertRaises(ValueError):
            summarize_csv(self.path)


if __name__ == "__main__":
    unittest.main()
