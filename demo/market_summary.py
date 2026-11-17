"""Educational CSV price summary.

Standalone course demonstration. No broker connectivity, trading decisions,
account information, API credentials, or private implementation dependencies.
"""

import argparse
import csv
import math
from datetime import date
from pathlib import Path


def summarize_csv(path):
    """Return basic descriptive statistics for a dated sample-price CSV."""
    rows = []
    with Path(path).open("r", newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)
        if not {"date", "close", "volume"}.issubset(reader.fieldnames or []):
            raise ValueError("CSV must contain date, close, and volume columns")

        for line_number, record in enumerate(reader, start=2):
            try:
                day = date.fromisoformat(record["date"])
                close = float(record["close"])
                volume = int(record["volume"])
            except (ValueError, TypeError, KeyError) as exc:
                raise ValueError(f"Invalid row at line {line_number}") from exc
            if not math.isfinite(close) or close <= 0 or volume < 0:
                raise ValueError(f"Out-of-range values at line {line_number}")
            if rows and day <= rows[-1][0]:
                raise ValueError("Dates must be strictly increasing")
            rows.append((day, close, volume))

    if len(rows) < 2:
        raise ValueError("At least two dated observations are required")

    first, last = rows[0][1], rows[-1][1]
    return {
        "observations": len(rows),
        "first_date": rows[0][0].isoformat(),
        "last_date": rows[-1][0].isoformat(),
        "first_close": first,
        "last_close": last,
        "minimum_close": min(row[1] for row in rows),
        "maximum_close": max(row[1] for row in rows),
        "percent_change": (last - first) / first * 100,
        "total_volume": sum(row[2] for row in rows),
    }


def main():
    parser = argparse.ArgumentParser(description="Summarize sample CSV prices.")
    parser.add_argument("csv_path", type=Path, help="Path to dated sample data")
    args = parser.parse_args()
    for label, value in summarize_csv(args.csv_path).items():
        print(f"{label}: {value}")


if __name__ == "__main__":
    main()
