# `/finance housing`

Use for housing decisions such as monthly rent vs jeonse vs purchase, cheongyak readiness, and housing-loan burden.

## Inputs

- Current housing cost
- Candidate rent, jeonse deposit, or purchase price
- Available cash
- Expected loan amount, interest rate, and term
- Monthly income and other debt payments
- Household status and rough timeline
- Cheongyak account status if relevant

## Analyze

- Monthly cash-flow burden.
- Deposit or down-payment liquidity impact.
- Loan payment stress.
- Opportunity cost and reversibility.
- Cheongyak and policy-loan items to verify.

Use `scripts/housing_affordability.py` for payment and burden estimates.

## Output

- Rent/jeonse/purchase comparison.
- Cash-flow impact.
- Risk and reversibility notes.
- 90-day action plan.
- Official confirmation checklist for DSR/LTV/DTI, policy loans, cheongyak, and lender review.

Do not say a loan will be approved. Actual eligibility requires current rules and financial-institution review.
