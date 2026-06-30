# `/finance report`

Use to generate a complete personal finance report from the current profile, budget, plan, and dashboard inputs.

## Steps

1. Confirm the report audience: personal use, spouse/partner discussion, advisor discussion, or monthly review.
2. Read `1-my-profile.md`, `2-my-budget.md`, and `3-my-plan.md` if available.
3. Ask for missing critical values before calculating, but do not block on optional details.
4. Generate a Markdown report in `shareable/`.
5. Update `4-my-dashboard.html` or a shareable HTML report with infographic cards, score bars, allocation charts, budget/debt visuals, and a 90-day action timeline.
6. Generate PDF from the HTML report only if a safe local conversion path is available.

Use `scripts/generate_report.py` for Markdown and HTML when structured JSON input is available. Add `--pdf` to attempt PDF conversion with a local Chrome or Edge headless browser. Use `scripts/html_to_pdf.py` for converting an existing HTML report.

## Report Sections

- Executive summary
- Assumptions and data gaps
- Financial health score
- Budget and cash flow
- Debt strategy
- Net worth and asset allocation
- Visual charts: score donut, score breakdown bars, asset allocation donut, budget bars, debt burden bar, and 90-day timeline
- Pension and retirement
- Housing
- Tax and insurance checks
- 90-day action plan
- Disclaimers

## Output Message

Tell the user which files were created or updated. If PDF was generated, provide its path. If PDF was not generated, say why and provide the Markdown/HTML alternatives.
