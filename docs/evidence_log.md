# Evidence Log — Credit Risk PD Project

> Goal: keep a lightweight audit trail of what was done, why, and where (links to scripts/commits).

## 2025-12-26
- **Setup:** repo structure + venv + requirements + Jupyter kernels
- **Data:** added `src/data/make_dataset.py` (validation + normalized copy)
- **Splits:** added `src/data/prepare_dataset.py` (70/15/15 stratified)
- **Baseline:** logistic regression baseline metrics saved
- **Tuning:** LR and GB tuning saved to `reports/*_tuning_results.csv`
- **Models:** trained RF + GB (tuned) and built leaderboard (`reports/leaderboard.csv`)
- **Calibration:** sigmoid/isotonic calibration evaluated (`src/models/calibrate_models.py`)
- **Final test:** champion RF+isotonic evaluated on held-out test (`reports/final_test_metrics.json`)
- **Docs:** README finalized

### Links
- Repo: credit-risk-default-prediction
- Key scripts:
  - `src/data/make_dataset.py`
  - `src/data/prepare_dataset.py`
  - `src/models/*`
- Outputs:
  - `reports/leaderboard.csv`
  - `reports/final_test_metrics.json`
