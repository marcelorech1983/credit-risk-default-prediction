# Baseline Plan — Credit Default Prediction (UCI)

## Goal
Predict probability of default (PD) for the next month using customer profile + payment history.

## Data
- Source: UCI Credit Card Default dataset (30,000 rows)
- Target: `default.payment.next.month` (1 = default, 0 = non-default)
- Class balance: ~22% default (6636/30000)

## Modeling approach (baseline → stronger)
1) Logistic Regression (with scaling)
2) Tree-based model (e.g., RandomForest / Gradient Boosting)
3) Calibrated model (Platt / Isotonic)

## Splitting
- Train/Validation/Test: 70/15/15
- Stratified by target (keep default rate consistent)

## Metrics
**Discrimination**
- ROC-AUC
- PR-AUC (important with class imbalance)

**Calibration**
- Brier score
- Calibration curve (reliability plot)

**Operational / Decision**
- Confusion matrix at chosen threshold
- Expected cost / benefit (later)

## Minimum deliverables
- Reproducible pipeline (data → features → model → evaluation)
- Data Dictionary (done)
- Model Card + Data Card (later)
- Evidence Log entries (weekly)
