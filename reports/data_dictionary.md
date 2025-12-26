# Data Dictionary — UCI Credit Card Default
- Rows: 30000
- Columns: 25

## Target
- `default.payment.next.month`: 1 = default, 0 = non-default

## Columns
| column | dtype | example | notes |
|---|---:|---:|---|
| ID | int64 | 1 | Row identifier (drop from modeling). |
| LIMIT_BAL | float64 | 20000.0 |  |
| SEX | int64 | 2 | Categorical code (check code meanings in UCI description). |
| EDUCATION | int64 | 2 | Categorical code (check code meanings in UCI description). |
| MARRIAGE | int64 | 1 | Categorical code (check code meanings in UCI description). |
| AGE | int64 | 24 |  |
| PAY_0 | int64 | 2 | Repayment status by month (categorical/ordinal). |
| PAY_2 | int64 | 2 | Repayment status by month (categorical/ordinal). |
| PAY_3 | int64 | -1 | Repayment status by month (categorical/ordinal). |
| PAY_4 | int64 | -1 | Repayment status by month (categorical/ordinal). |
| PAY_5 | int64 | -2 | Repayment status by month (categorical/ordinal). |
| PAY_6 | int64 | -2 | Repayment status by month (categorical/ordinal). |
| BILL_AMT1 | float64 | 3913.0 | Bill statement amount by month. |
| BILL_AMT2 | float64 | 3102.0 | Bill statement amount by month. |
| BILL_AMT3 | float64 | 689.0 | Bill statement amount by month. |
| BILL_AMT4 | float64 | 0.0 | Bill statement amount by month. |
| BILL_AMT5 | float64 | 0.0 | Bill statement amount by month. |
| BILL_AMT6 | float64 | 0.0 | Bill statement amount by month. |
| PAY_AMT1 | float64 | 0.0 | Repayment status by month (categorical/ordinal). |
| PAY_AMT2 | float64 | 689.0 | Repayment status by month (categorical/ordinal). |
| PAY_AMT3 | float64 | 0.0 | Repayment status by month (categorical/ordinal). |
| PAY_AMT4 | float64 | 0.0 | Repayment status by month (categorical/ordinal). |
| PAY_AMT5 | float64 | 0.0 | Repayment status by month (categorical/ordinal). |
| PAY_AMT6 | float64 | 0.0 | Repayment status by month (categorical/ordinal). |
| default.payment.next.month | int64 | 1 |  |
