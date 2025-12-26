"""
prepare_dataset.py
- Loads normalized raw dataset
- Drops non-model features (ID)
- Creates stratified train/val/test splits
- Saves processed CSVs to data/processed/
"""

from __future__ import annotations

from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

RAW_PATH = Path("data/raw/default_of_credit_card_clients__normalized.csv")
OUT_DIR = Path("data/processed")

TARGET_COL = "default.payment.next.month"
DROP_COLS = ["ID"]


def main() -> int:
    if not RAW_PATH.exists():
        raise FileNotFoundError(f"Missing file: {RAW_PATH}. Run make_dataset.py first.")

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(RAW_PATH)

    # Basic checks
    if TARGET_COL not in df.columns:
        raise ValueError(f"Target column not found: {TARGET_COL}")

    # Separate target and features
    y = df[TARGET_COL].astype(int)
    X = df.drop(columns=[TARGET_COL])

    # Drop identifier columns
    for c in DROP_COLS:
        if c in X.columns:
            X = X.drop(columns=[c])

    # Split: 70/15/15 with stratification
    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y, test_size=0.30, random_state=42, stratify=y
    )
    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp, test_size=0.50, random_state=42, stratify=y_temp
    )

    # Save
    X_train.to_csv(OUT_DIR / "X_train.csv", index=False)
    y_train.to_csv(OUT_DIR / "y_train.csv", index=False)
    X_val.to_csv(OUT_DIR / "X_val.csv", index=False)
    y_val.to_csv(OUT_DIR / "y_val.csv", index=False)
    X_test.to_csv(OUT_DIR / "X_test.csv", index=False)
    y_test.to_csv(OUT_DIR / "y_test.csv", index=False)

    # Report
    def rate(s: pd.Series) -> float:
        return float(s.mean())

    print("✅ Saved processed splits to data/processed/")
    print("Shapes:")
    print("  train:", X_train.shape, y_train.shape, "default_rate:", round(rate(y_train), 4))
    print("  val  :", X_val.shape, y_val.shape, "default_rate:", round(rate(y_val), 4))
    print("  test :", X_test.shape, y_test.shape, "default_rate:", round(rate(y_test), 4))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
