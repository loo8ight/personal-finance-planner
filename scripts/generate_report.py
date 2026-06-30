#!/usr/bin/env python3
"""Generate Markdown report and simple HTML dashboard from structured JSON."""

from __future__ import annotations

import argparse
import html
import json
from datetime import date
from pathlib import Path


def load_input(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def krw(value):
    try:
        return f"{float(value):,.0f} KRW"
    except (TypeError, ValueError):
        return str(value or "Unknown")


def list_lines(items):
    if not items:
        return "- Unknown"
    return "\n".join(f"- {item}" for item in items)


def make_markdown(data):
    today = data.get("prepared_date") or date.today().isoformat()
    score = data.get("score", {})
    budget = data.get("budget", {})
    networth = data.get("networth", {})
    actions = data.get("actions", [])
    assumptions = data.get("assumptions", [])
    gaps = data.get("data_gaps", [])

    return f"""# Personal Finance Planner Report

- Prepared: {today}
- Currency: KRW
- Residency context: {data.get("residency_context", "Unknown")}
- Report purpose: {data.get("purpose", "Personal planning")}

## 1. Executive Summary

- Current situation: {data.get("summary", "Not provided")}
- Financial Health Score: {score.get("score", "Unknown")} / 100 ({score.get("grade", "Unknown")})
- First priority: {data.get("first_priority", "Confirm missing data and stabilize monthly cash flow.")}

## 2. Assumptions And Data Gaps

### Assumptions

{list_lines(assumptions)}

### Missing Data

{list_lines(gaps)}

## 3. Budget And Cash Flow

- Monthly income: {krw(budget.get("monthly_income"))}
- Monthly spending: {krw(budget.get("monthly_spending"))}
- Savings rate: {budget.get("savings_rate_percent", "Unknown")}%
- Debt payment burden: {budget.get("debt_payment_burden_percent", "Unknown")}%

## 4. Net Worth

- Total assets: {krw(networth.get("total_assets"))}
- Total liabilities: {krw(networth.get("total_liabilities"))}
- Net worth: {krw(networth.get("net_worth"))}

## 5. 90-Day Action Plan

{list_lines(actions)}

## 6. Verification Items

{list_lines(data.get("verification_items", []))}

## 7. Disclaimers

This report is for informational and educational planning support only. It is not financial, investment, tax, legal, insurance, or real-estate advice. Variable Korean rules require current official confirmation. Consult qualified professionals before making major decisions.
"""


def make_dashboard_html(data):
    score = data.get("score", {})
    networth = data.get("networth", {})
    budget = data.get("budget", {})
    actions = data.get("actions", [])
    allocation = networth.get("allocation", [])

    rows = "\n".join(
        "<tr><td>{}</td><td>{}</td><td>{}%</td></tr>".format(
            html.escape(str(row.get("category", ""))),
            html.escape(krw(row.get("amount", ""))),
            html.escape(str(row.get("share_percent", ""))),
        )
        for row in allocation
    ) or "<tr><td colspan=\"3\">No allocation data</td></tr>"

    action_items = "\n".join(f"<li>{html.escape(str(item))}</li>" for item in actions) or "<li>Confirm missing data.</li>"

    return f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Personal Finance Planner Dashboard</title>
  <style>
    body {{ margin: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background: #f7f8fa; color: #17202a; }}
    main {{ max-width: 1040px; margin: 0 auto; padding: 32px 20px; }}
    .grid {{ display: grid; grid-template-columns: repeat(12, 1fr); gap: 16px; }}
    .card {{ background: white; border: 1px solid #d9dee7; border-radius: 8px; padding: 18px; }}
    .span-4 {{ grid-column: span 4; }} .span-8 {{ grid-column: span 8; }} .span-12 {{ grid-column: span 12; }}
    .metric {{ font-size: 30px; font-weight: 700; }}
    table {{ width: 100%; border-collapse: collapse; }} th, td {{ border-bottom: 1px solid #d9dee7; padding: 10px; text-align: left; }}
    @media (max-width: 800px) {{ .span-4, .span-8 {{ grid-column: span 12; }} }}
  </style>
</head>
<body>
<main>
  <h1>Personal Finance Planner Dashboard</h1>
  <p>Updated: {html.escape(data.get("prepared_date") or date.today().isoformat())}</p>
  <section class="grid">
    <article class="card span-4"><h2>Financial Health Score</h2><div class="metric">{html.escape(str(score.get("score", "Unknown")))} / 100</div><p>{html.escape(str(score.get("grade", "Unknown")))}</p></article>
    <article class="card span-8"><h2>Core Metrics</h2><p>Net worth: <strong>{html.escape(krw(networth.get("net_worth")))}</strong></p><p>Savings rate: <strong>{html.escape(str(budget.get("savings_rate_percent", "Unknown")))}%</strong></p><p>Debt burden: <strong>{html.escape(str(budget.get("debt_payment_burden_percent", "Unknown")))}%</strong></p></article>
    <article class="card span-12"><h2>Asset Allocation</h2><table><thead><tr><th>Category</th><th>Amount</th><th>Share</th></tr></thead><tbody>{rows}</tbody></table></article>
    <article class="card span-12"><h2>90-Day Actions</h2><ol>{action_items}</ol></article>
  </section>
  <p>This dashboard is for educational planning support only and is not professional advice. Variable Korean rules require current official confirmation.</p>
</main>
</body>
</html>
"""


def main():
    parser = argparse.ArgumentParser(description="Generate finance report files from JSON.")
    parser.add_argument("--input", required=True, help="Structured JSON input.")
    parser.add_argument("--output-dir", default="shareable", help="Directory for generated report files.")
    parser.add_argument("--prefix", default="finance-report", help="Output file prefix.")
    args = parser.parse_args()

    data = load_input(args.input)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    markdown_path = out_dir / f"{args.prefix}.md"
    html_path = out_dir / f"{args.prefix}.html"
    markdown_path.write_text(make_markdown(data), encoding="utf-8")
    html_path.write_text(make_dashboard_html(data), encoding="utf-8")

    print(
        json.dumps(
            {
                "markdown_report": str(markdown_path),
                "html_dashboard": str(html_path),
                "pdf_report": None,
                "note": "PDF generation is optional and was not attempted by this standard-library script.",
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
