# `/finance debt`

Use for debt payoff planning.

## Inputs

For each debt, ask for:

- Name or type
- Balance
- Interest rate
- Minimum monthly payment
- Remaining term or maturity if known

Also ask for monthly extra payoff capacity.

## Analyze

- Highest-interest-first payoff order.
- Balance-smallest-first motivational payoff order.
- Expected payoff period.
- Approximate interest cost.
- Refinance, consolidation, or delinquency risk items that require professional or lender confirmation.

Use `scripts/debt_payoff.py` when balances, rates, and monthly payment capacity are available.

## Output

- Two payoff strategies: interest-first and motivation-first.
- Recommended direction based on the user's stated preference and cash-flow stability.
- 90-day debt action plan.
- Warning signs: revolving credit, card loans, delinquency risk, high-rate unsecured debt.

Do not guarantee credit-score impact, loan refinancing approval, or interest savings.
