# `/finance retirement`

Use for retirement planning around National Pension, workplace retirement pension, IRP, pension savings, and personal assets.

## Inputs

- Current age
- Target retirement age
- Expected monthly retirement spending
- Current retirement assets
- Monthly retirement saving
- Expected National Pension amount if known
- Pension savings, IRP, and workplace retirement pension balances
- Scenario return assumptions

## Analyze

- Estimated retirement fund need.
- Existing pension and investment coverage.
- Funding gap.
- Monthly additional saving needed.
- Conservative, base, and optimistic scenarios.

Use `scripts/retirement_projection.py` when numeric inputs are available.

## Output

- Retirement readiness summary.
- Gap estimate under assumptions.
- Monthly saving estimate.
- Account checklist: National Pension, pension savings, IRP, workplace retirement pension.
- Items requiring official confirmation.

Do not treat pension rules, tax limits, or benefit estimates as final unless the user provides official current data.
