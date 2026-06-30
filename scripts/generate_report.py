#!/usr/bin/env python3
"""Generate Korean Markdown, visual HTML, and optional PDF finance reports."""

from __future__ import annotations

import argparse
import html
import json
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path


COLORS = ["#2563eb", "#1f8a5b", "#b7791f", "#7c3aed", "#c2410c", "#0891b2", "#be123c", "#475569"]

try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass


def load_input(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def safe_float(value, default=0.0):
    try:
        if value in (None, ""):
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def krw(value):
    if value in (None, "", "Unknown"):
        return "확인 필요"
    return f"{safe_float(value):,.0f}원"


def pct(value):
    if value in (None, "", "Unknown"):
        return "확인 필요"
    return f"{safe_float(value):.1f}%"


def width(value, max_value=100):
    return max(0, min(100, safe_float(value) / max_value * 100))


def list_lines(items):
    if not items:
        return "- 확인 필요"
    return "\n".join(f"- {item}" for item in items)


def li_items(items):
    if not items:
        return "<li>확인 필요한 항목을 정리합니다.</li>"
    return "\n".join(f"<li>{html.escape(str(item))}</li>" for item in items)


def score_label(grade):
    mapping = {
        "Excellent": "우수",
        "Healthy": "건강",
        "Watch": "관찰",
        "Weak": "취약",
        "Critical": "위험",
    }
    return mapping.get(str(grade), str(grade or "확인 필요"))


def score_color(score):
    score = safe_float(score)
    if score >= 85:
        return "#1f8a5b"
    if score >= 70:
        return "#2563eb"
    if score >= 55:
        return "#b7791f"
    if score >= 40:
        return "#c2410c"
    return "#b42318"


def breakdown_rows(score):
    raw = score.get("breakdown", {}) if isinstance(score, dict) else {}
    labels = [
        ("cash_flow_budgeting", "현금흐름 / 예산", 20),
        ("debt_stability", "부채 안정성", 20),
        ("emergency_protection", "비상금 / 보호장치", 15),
        ("investment_allocation", "투자 / 자산배분", 15),
        ("pension_retirement", "연금 / 은퇴준비", 15),
        ("housing_tax_systems", "주거 / 세금 / 제도활용", 15),
    ]
    rows = []
    for key, label, max_points in labels:
        points = safe_float(raw.get(key))
        rows.append(
            f"""
            <div class="bar-row">
              <div class="bar-label"><span>{html.escape(label)}</span><strong>{points:g} / {max_points}</strong></div>
              <div class="bar"><span style="width:{width(points, max_points):.1f}%"></span></div>
            </div>
            """
        )
    return "\n".join(rows)


def allocation_rows(allocation):
    if not allocation:
        return "<tr><td colspan=\"3\">자산배분 데이터가 아직 없습니다.</td></tr>"
    return "\n".join(
        "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(
            html.escape(str(row.get("category", "기타"))),
            html.escape(krw(row.get("amount"))),
            html.escape(pct(row.get("share_percent"))),
        )
        for row in allocation
    )


def allocation_gradient(allocation):
    if not allocation:
        return "#e5e7eb 0 100%"
    cursor = 0.0
    parts = []
    for index, row in enumerate(allocation):
        share = max(0.0, safe_float(row.get("share_percent")))
        end = min(100.0, cursor + share)
        color = COLORS[index % len(COLORS)]
        parts.append(f"{color} {cursor:.1f}% {end:.1f}%")
        cursor = end
    if cursor < 100:
        parts.append(f"#e5e7eb {cursor:.1f}% 100%")
    return ", ".join(parts)


def legend_items(allocation):
    if not allocation:
        return "<li><span style=\"background:#e5e7eb\"></span>데이터 없음</li>"
    items = []
    for index, row in enumerate(allocation):
        color = COLORS[index % len(COLORS)]
        label = html.escape(str(row.get("category", "기타")))
        share = html.escape(pct(row.get("share_percent")))
        items.append(f"<li><span style=\"background:{color}\"></span>{label} {share}</li>")
    return "\n".join(items)


def make_markdown(data):
    today = data.get("prepared_date") or date.today().isoformat()
    score = data.get("score", {})
    budget = data.get("budget", {})
    networth = data.get("networth", {})
    actions = data.get("actions", [])
    assumptions = data.get("assumptions", [])
    gaps = data.get("data_gaps", [])

    return f"""# 개인 재무관리 리포트

- 작성일: {today}
- 통화: KRW
- 거주 기준: {data.get("residency_context", "확인 필요")}
- 리포트 목적: {data.get("purpose", "개인 재무 점검")}

## 1. 요약

- 현재 상황: {data.get("summary", "아직 충분한 설명이 없습니다.")}
- 재무 건강점수: {score.get("score", "확인 필요")} / 100 ({score_label(score.get("grade"))})
- 첫 번째 우선순위: {data.get("first_priority", "누락 데이터를 확인하고 월 현금흐름을 안정화합니다.")}

## 2. 가정과 누락 데이터

### 사용한 가정

{list_lines(assumptions)}

### 추가로 필요한 데이터

{list_lines(gaps)}

## 3. 예산과 현금흐름

- 월 소득: {krw(budget.get("monthly_income"))}
- 월 지출: {krw(budget.get("monthly_spending"))}
- 저축률: {pct(budget.get("savings_rate_percent"))}
- 부채상환 부담률: {pct(budget.get("debt_payment_burden_percent"))}

## 4. 순자산

- 총자산: {krw(networth.get("total_assets"))}
- 총부채: {krw(networth.get("total_liabilities"))}
- 순자산: {krw(networth.get("net_worth"))}

## 5. 90일 실행 계획

{list_lines(actions)}

## 6. 공식 확인이 필요한 항목

{list_lines(data.get("verification_items", []))}

## 7. 유의사항

이 리포트는 정보 제공과 교육 목적의 재무 정리 자료입니다. 금융, 투자, 세무, 법률, 보험, 부동산 자문이 아닙니다. 한국의 세금, 연금, 대출, 청약, 금융상품 관련 제도는 바뀔 수 있으므로 중요한 결정 전에는 공식 자료와 전문가 상담으로 확인하세요.
"""


def make_dashboard_html(data):
    today = data.get("prepared_date") or date.today().isoformat()
    score = data.get("score", {})
    networth = data.get("networth", {})
    budget = data.get("budget", {})
    actions = data.get("actions", [])
    allocation = networth.get("allocation", [])
    score_value = safe_float(score.get("score"))
    score_col = score_color(score_value)
    savings_rate = safe_float(budget.get("savings_rate_percent"))
    debt_burden = safe_float(budget.get("debt_payment_burden_percent"))
    monthly_income = safe_float(budget.get("monthly_income"))
    monthly_spending = safe_float(budget.get("monthly_spending"))
    monthly_saving = max(0.0, monthly_income - monthly_spending)
    max_budget = max(monthly_income, monthly_spending, monthly_saving, 1)

    return f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>개인 재무관리 시각화 리포트</title>
  <style>
    :root {{
      --bg: #f7f8fa;
      --panel: #ffffff;
      --ink: #17202a;
      --muted: #667085;
      --line: #d9dee7;
      --blue: #2563eb;
      --green: #1f8a5b;
      --amber: #b7791f;
      --red: #b42318;
    }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Malgun Gothic", sans-serif; background: var(--bg); color: var(--ink); line-height: 1.5; }}
    main {{ max-width: 1120px; margin: 0 auto; padding: 32px 20px; }}
    header {{ display: flex; justify-content: space-between; gap: 16px; align-items: end; margin-bottom: 24px; }}
    h1, h2, h3, p {{ margin-top: 0; }}
    h1 {{ font-size: 30px; letter-spacing: 0; }}
    h2 {{ font-size: 18px; margin-bottom: 14px; }}
    .muted {{ color: var(--muted); }}
    .grid {{ display: grid; grid-template-columns: repeat(12, 1fr); gap: 16px; }}
    .card {{ background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 18px; break-inside: avoid; }}
    .span-3 {{ grid-column: span 3; }}
    .span-4 {{ grid-column: span 4; }}
    .span-6 {{ grid-column: span 6; }}
    .span-8 {{ grid-column: span 8; }}
    .span-12 {{ grid-column: span 12; }}
    .metric {{ font-size: 28px; font-weight: 800; margin-top: 6px; }}
    .score-wrap {{ display: flex; align-items: center; gap: 20px; }}
    .score-donut {{ width: 148px; height: 148px; border-radius: 50%; display: grid; place-items: center; background: conic-gradient({score_col} {width(score_value):.1f}%, #e5e7eb 0); }}
    .score-inner {{ width: 104px; height: 104px; border-radius: 50%; background: white; display: grid; place-items: center; text-align: center; font-weight: 800; font-size: 26px; }}
    .bar {{ height: 12px; background: #edf0f5; border-radius: 999px; overflow: hidden; }}
    .bar span {{ display: block; height: 100%; background: var(--blue); }}
    .bar-row {{ margin-bottom: 13px; }}
    .bar-label {{ display: flex; justify-content: space-between; gap: 12px; margin-bottom: 6px; font-size: 14px; }}
    .budget-bar {{ display: grid; grid-template-columns: 90px 1fr 110px; gap: 10px; align-items: center; margin-bottom: 12px; }}
    .budget-bar strong {{ text-align: right; }}
    .donut {{ width: 170px; height: 170px; border-radius: 50%; background: conic-gradient({allocation_gradient(allocation)}); margin: 8px auto 12px; }}
    .legend {{ list-style: none; padding: 0; margin: 0; display: grid; gap: 8px; }}
    .legend li {{ display: flex; gap: 8px; align-items: center; font-size: 14px; }}
    .legend span {{ width: 12px; height: 12px; border-radius: 3px; display: inline-block; }}
    table {{ width: 100%; border-collapse: collapse; font-size: 14px; }}
    th, td {{ border-bottom: 1px solid var(--line); padding: 10px 8px; text-align: left; }}
    th {{ color: var(--muted); font-weight: 700; }}
    .timeline {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }}
    .step {{ border-left: 4px solid var(--blue); background: #f8fafc; padding: 12px; border-radius: 8px; }}
    .actions li {{ margin-bottom: 8px; }}
    footer {{ margin-top: 24px; color: var(--muted); font-size: 13px; }}
    @media (max-width: 840px) {{
      header, .score-wrap {{ display: block; }}
      .span-3, .span-4, .span-6, .span-8 {{ grid-column: span 12; }}
      .timeline {{ grid-template-columns: 1fr; }}
    }}
    @media print {{
      body {{ background: white; }}
      main {{ padding: 18px; }}
      .card {{ box-shadow: none; }}
    }}
  </style>
</head>
<body>
<main>
  <header>
    <div>
      <h1>개인 재무관리 시각화 리포트</h1>
      <p class="muted">작성일: {html.escape(str(today))} · 통화: KRW · 한국 거주자 기준</p>
    </div>
    <div class="muted">정보 제공 / 교육 목적</div>
  </header>

  <section class="grid">
    <article class="card span-5">
      <h2>재무 건강점수</h2>
      <div class="score-wrap">
        <div class="score-donut"><div class="score-inner">{score_value:g}<br><span class="muted">/100</span></div></div>
        <div>
          <h3>{html.escape(score_label(score.get("grade")))}</h3>
          <p class="muted">점수는 입력값 기준의 교육용 지표입니다. 낮은 영역은 실행 항목으로 개선할 수 있습니다.</p>
        </div>
      </div>
    </article>

    <article class="card span-7">
      <h2>핵심 지표</h2>
      <div class="grid">
        <div class="span-3"><div class="muted">순자산</div><div class="metric">{html.escape(krw(networth.get("net_worth")))}</div></div>
        <div class="span-3"><div class="muted">저축률</div><div class="metric">{savings_rate:.1f}%</div></div>
        <div class="span-3"><div class="muted">부채상환 부담</div><div class="metric">{debt_burden:.1f}%</div></div>
        <div class="span-3"><div class="muted">월 소득</div><div class="metric">{html.escape(krw(monthly_income))}</div></div>
      </div>
    </article>

    <article class="card span-6">
      <h2>점수 영역별 그래프</h2>
      {breakdown_rows(score)}
    </article>

    <article class="card span-6">
      <h2>월 예산 막대그래프</h2>
      <div class="budget-bar"><span>월 소득</span><div class="bar"><span style="width:{width(monthly_income, max_budget):.1f}%"></span></div><strong>{html.escape(krw(monthly_income))}</strong></div>
      <div class="budget-bar"><span>월 지출</span><div class="bar"><span style="width:{width(monthly_spending, max_budget):.1f}%; background:#c2410c"></span></div><strong>{html.escape(krw(monthly_spending))}</strong></div>
      <div class="budget-bar"><span>추정 잉여</span><div class="bar"><span style="width:{width(monthly_saving, max_budget):.1f}%; background:#1f8a5b"></span></div><strong>{html.escape(krw(monthly_saving))}</strong></div>
      <p class="muted">잉여금은 월 소득에서 월 지출을 뺀 단순 추정치입니다.</p>
    </article>

    <article class="card span-5">
      <h2>자산배분 도넛 차트</h2>
      <div class="donut" aria-label="자산배분 차트"></div>
      <ul class="legend">{legend_items(allocation)}</ul>
    </article>

    <article class="card span-7">
      <h2>자산배분 표</h2>
      <table>
        <thead><tr><th>구분</th><th>금액</th><th>비중</th></tr></thead>
        <tbody>{allocation_rows(allocation)}</tbody>
      </table>
    </article>

    <article class="card span-12">
      <h2>90일 실행 타임라인</h2>
      <div class="timeline">
        <div class="step"><h3>1-30일</h3><ol class="actions">{li_items(actions[:2])}</ol></div>
        <div class="step"><h3>31-60일</h3><ol class="actions">{li_items(actions[2:4])}</ol></div>
        <div class="step"><h3>61-90일</h3><ol class="actions">{li_items(actions[4:6])}</ol></div>
      </div>
    </article>
  </section>

  <footer>
    이 리포트는 정보 제공과 교육 목적의 재무 정리 자료입니다. 금융, 투자, 세무, 법률, 보험, 부동산 자문이 아니며, 변동 가능한 한국 제도는 공식 자료와 전문가 상담으로 확인해야 합니다.
  </footer>
</main>
</body>
</html>
"""


def browser_candidates():
    names = ["chrome", "chrome.exe", "chromium", "chromium.exe", "msedge", "msedge.exe"]
    paths = [shutil.which(name) for name in names]
    paths.extend(
        [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        ]
    )
    seen = set()
    for path in paths:
        if not path:
            continue
        candidate = Path(path)
        if candidate.exists() and str(candidate).lower() not in seen:
            seen.add(str(candidate).lower())
            yield candidate


def convert_html_to_pdf(html_path, pdf_path):
    html_path = Path(html_path).resolve()
    pdf_path = Path(pdf_path).resolve()
    pdf_path.parent.mkdir(parents=True, exist_ok=True)

    wkhtml = shutil.which("wkhtmltopdf")
    run_options = {"capture_output": True, "text": True, "encoding": "utf-8", "errors": "replace", "timeout": 90}

    attempted = []

    if wkhtml:
        attempted.append(wkhtml)
        result = subprocess.run([wkhtml, str(html_path), str(pdf_path)], **run_options)
        if result.returncode == 0 and pdf_path.exists():
            return str(pdf_path), "wkhtmltopdf로 PDF를 생성했습니다."

    for browser in browser_candidates():
        attempted.append(str(browser))
        for headless_flag in ("--headless=new", "--headless"):
            cmd = [
                str(browser),
                headless_flag,
                "--disable-gpu",
                "--no-first-run",
                f"--print-to-pdf={pdf_path}",
                html_path.as_uri(),
            ]
            result = subprocess.run(cmd, **run_options)
            if result.returncode == 0 and pdf_path.exists():
                return str(pdf_path), f"{browser.name} headless 모드로 PDF를 생성했습니다."

    if attempted:
        names = ", ".join(Path(item).name for item in attempted)
        return None, f"PDF 변환 도구를 찾았지만 변환에 실패했습니다: {names}. HTML 리포트는 생성되었습니다."
    return None, "Chrome, Edge, 또는 wkhtmltopdf를 찾지 못해 PDF 변환을 건너뛰었습니다."


def main():
    parser = argparse.ArgumentParser(description="Generate Korean finance report files from JSON.")
    parser.add_argument("--input", required=True, help="Structured JSON input.")
    parser.add_argument("--output-dir", default="shareable", help="Directory for generated report files.")
    parser.add_argument("--prefix", default="finance-report", help="Output file prefix.")
    parser.add_argument("--pdf", action="store_true", help="Attempt PDF conversion from the generated HTML report.")
    args = parser.parse_args()

    data = load_input(args.input)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    markdown_path = out_dir / f"{args.prefix}.md"
    html_path = out_dir / f"{args.prefix}.html"
    pdf_path = out_dir / f"{args.prefix}.pdf"
    markdown_path.write_text(make_markdown(data), encoding="utf-8")
    html_path.write_text(make_dashboard_html(data), encoding="utf-8")

    pdf_result = None
    pdf_note = "PDF 변환은 요청되지 않았습니다. 필요하면 --pdf 옵션을 사용하세요."
    if args.pdf:
        pdf_result, pdf_note = convert_html_to_pdf(html_path, pdf_path)

    print(
        json.dumps(
            {
                "markdown_report": str(markdown_path),
                "html_report": str(html_path),
                "pdf_report": pdf_result,
                "note": pdf_note,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
