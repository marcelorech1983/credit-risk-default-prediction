# Model Card — Credit Risk Default Prediction (PD)

## Model details
- **Project:** Credit Risk — Default Prediction (Probability of Default / PD)
- **Dataset:** UCI “Default of Credit Card Clients” (Kaggle mirror)
- **Target:** `default.payment.next.month` (1 = default, 0 = non-default)
- **Champion model:** Random Forest + **Isotonic** probability calibration
- **Primary goal:** produce **risk-ready probabilities** (PD), not only ranking.

## Intended use
- **Intended:** portfolio/demo of a classical credit risk workflow (EDA → splits → modeling → calibration → test).
- **Not intended:** real-world lending decisions without (1) governance, (2) local regulatory requirements, (3) monitoring, (4) bias analysis, (5) model risk management.

## Data
See `docs/data_card.md` for full details.

## Training / evaluation protocol
- **Split:** train/val/test = **70/15/15**, **stratified** by target.
- **Model selection:** based on **validation** metrics (PR-AUC prioritized due to imbalance).
- **Final test:** used **once** at the end (held-out).

## Metrics (current)
### Final test (held-out TEST)
Champion: **RF + isotonic calibration**  
- **Test ROC-AUC:** 0.7833  
- **Test PR-AUC:** 0.5580  
- **Test Brier:** 0.1345  

### Why these metrics
- **ROC-AUC / PR-AUC:** ranking quality (discrimination).
- **Brier + calibration curves:** probability quality (calibration) — critical for PD usage.

## Calibration
- Methods evaluated: **sigmoid (Platt)** and **isotonic** calibration.
- Calibration improves the reliability of predicted PDs (alignment between predicted probabilities and observed default rates).

## Explainability
- Global: feature importance (tree-based) and optional SHAP (future extension).
- Local: PD + explanation for a single applicant (future extension / “risk review assistant” repo).

## Limitations
- Dataset is not recent and is not representative of any specific country’s lending population.
- Feature set is limited to what the dataset provides (no bureau, income verification, macro factors, etc.).
- No fairness analysis included yet (should be added for real-world use).

## Ethical / risk considerations
- PD models can amplify historical biases. For production use, add:
  - bias/fairness checks,
  - drift monitoring,
  - governance + documentation + human oversight.
