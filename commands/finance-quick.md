# `/finance quick`

Use for a fast financial diagnosis when the user wants a quick answer before creating a full plan.

## Ask For

- Monthly take-home income
- Monthly spending
- Cash-like assets
- Total debt
- Monthly saving/investment amount
- Age
- Main goal

Do not ask for account numbers, card numbers, resident registration numbers, passwords, or authentication details.

## Analyze

- Savings rate
- Spending-to-income ratio
- Debt-to-income pressure
- Emergency fund coverage
- Initial financial health score

Use `scripts/finance_score.py` when enough values are available.

## Output

1. Financial Health Score from 0 to 100.
2. Three risk signals, framed as fixable issues.
3. Three actions for this month.
4. Additional questions needed for a more accurate plan.

## Tone

Use phrases such as "현재 입력값 기준으로는", "가정이 맞다면", and "우선순위는". Do not use alarmist or guaranteed language.
