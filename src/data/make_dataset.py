"""
make_dataset.py
- Downloads or loads the UCI/Kaggle Credit Default dataset
- Saves a local copy into data/raw/
Note: data/raw is ignored by git (do not commit).
"""

from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd

RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

# You can place the dataset manually as:
# data/raw/default_of_credit_card_clients.csv
DEFAULT_CSV = RAW_DIR / "default_of_credit_card_clients.csv"


def main() -> int:
    """
    Strategy:
    - For simplicity and reliability, we start with manual download (UCI/Kaggle),
      then you place the CSV into data/raw/ with the expected name.
    - This script validates the file and writes a cleaned copy for consistent reading.
    """
    if not DEFAULT_CSV.exists():
        print("❌ Dataset not found.")
        print(f"Expected file at: {DEFAULT_CSV}")
        print("\nDownload options:")
        print("- UCI: https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients")
        print("- Kaggle: https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset")
        print("\nThen place the CSV here and re-run:")
        print(f"  {DEFAULT_CSV}")
        return 1

    df = pd.read_csv(DEFAULT_CSV)

    # Basic validation
    print("✅ Loaded dataset")
    print("Shape:", df.shape)
    print("Columns:", len(df.columns))
    print(df.head(3))

    # Save a normalized copy (optional but helpful)
    normalized_path = RAW_DIR / "default_of_credit_card_clients__normalized.csv"
    df.to_csv(normalized_path, index=False)
    print(f"\n✅ Normalized copy saved to: {normalized_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
