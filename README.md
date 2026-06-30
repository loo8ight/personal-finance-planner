# Personal Finance Planner

A Claude Skill for personal budgeting, debt planning, investing, retirement planning, housing decisions, and tax-aware financial planning workflows for Korean residents.

## What It Does

- Builds your personal financial profile
- Creates a monthly budget
- Calculates net worth
- Reviews debt payoff options
- Checks investment allocation
- Helps with retirement and FIRE planning
- Reviews housing decisions
- Flags tax and insurance items to check
- Generates a financial health score
- Creates visual Markdown, HTML, and optional PDF reports

## What It Does Not Do

- It does not provide financial, investment, tax, legal, or insurance advice.
- It does not execute trades.
- It does not access your bank account.
- It does not guarantee investment returns.
- It does not replace a licensed professional.

## Commands

- `/finance`
- `/finance quick`
- `/finance budget`
- `/finance debt`
- `/finance networth`
- `/finance invest`
- `/finance retirement`
- `/finance fire`
- `/finance housing`
- `/finance tax`
- `/finance compare`
- `/finance report`

## Generated User Files

When used in a work folder, the skill creates and maintains:

- `1-my-profile.md`
- `2-my-budget.md`
- `3-my-plan.md`
- `4-my-dashboard.html`
- `check-ins/`
- `shareable/`
- `README.txt`

Do not put account numbers, resident registration numbers, card numbers, passwords, authentication codes, or other direct identifiers in these files.

## Recommended First Prompt

"Help me organize my finances."

Korean prompt:

"내 돈 관리 도와줘."

## Requirements

The bundled Python scripts use only the Python standard library. No external packages are required.

PDF export is optional and depends on the local environment. `scripts/generate_report.py --pdf` and `scripts/html_to_pdf.py` try to use a local Chrome or Edge headless browser to convert the visual HTML report to PDF. Markdown and HTML reports are the default portable outputs.

## License

MIT License. See `LICENSE` and `NOTICE.md`.
