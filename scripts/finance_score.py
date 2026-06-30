#!/usr/bin/env python3
"""Financial Health Score calculator."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_input(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def ratio(numerator, denominator):
    return 0.0 if not denominator else numerator / denominator


def clamp(value, low, high):
    return max(low, min(high, value))


def grade(score):
    if score >= 85:
        return "Excellent"
    if score >= 70:
        return "Healthy"
    if score >= 55:
        return "Watch"
    if score >= 40:
        return "Weak"
    return "Critical"


def calculate_score(data):
    income = float(data.get("monthly_income", 0) or 0)
    spending = float(data.get("monthly_spending", 0) or 0)
    saving = float(data.get("monthly_saving", max(0.0, income - spending)) or 0)
    liquid_assets = float(data.get("liquid_assets", 0) or 0)
    monthly_debt_payments = float(data.get("monthly_debt_payments", 0) or 0)
    total_debt = float(data.get("total_debt", 0) or 0)
    total_assets = float(data.get("total_assets", 0) or 0)
    risk_assets = float(data.get("risk_assets", 0) or 0)
    retirement_saving = float(data.get("retirement_monthly_saving", 0) or 0)
    insurance_premium = float(data.get("insurance_monthly_premium", 0) or 0)
    housing_cost = float(data.get("monthly_housing_cost", 0) or 0)

    savings_rate = ratio(saving, income)
    emergency_months = ratio(liquid_assets, spending if spending else income)
    debt_payment_ratio = ratio(monthly_debt_payments, income)
    total_debt_ratio = ratio(total_debt, income * 12)
    risk_asset_ratio = ratio(risk_assets, total_assets)
    retirement_rate = ratio(retirement_saving, income)
    insurance_ratio = ratio(insurance_premium, income)
    housing_ratio = ratio(housing_cost, income)

    cash_flow = clamp(savings_rate / 0.25 * 16, 0, 16)
    if spending <= income and income:
        cash_flow += 4

    debt = 20
    debt -= clamp(debt_payment_ratio / 0.4 * 10, 0, 10)
    debt -= clamp(total_debt_ratio / 2.0 * 7, 0, 7)
    if data.get("has_high_interest_debt"):
        debt -= 3
    debt = clamp(debt, 0, 20)

    protection = clamp(emergency_months / 6.0 * 10, 0, 10)
    if data.get("has_basic_insurance") or insurance_premium > 0:
        protection += 3
    if insurance_ratio <= 0.12 or insurance_premium == 0:
        protection += 2
    protection = clamp(protection, 0, 15)

    investment = 0
    if total_assets > 0:
        investment += 5
    if 0.15 <= risk_asset_ratio <= 0.8:
        investment += 5
    elif risk_asset_ratio > 0:
        investment += 3
    if data.get("has_diversification"):
        investment += 3
    if data.get("has_rebalancing_plan"):
        investment += 2
    investment = clamp(investment, 0, 15)

    retirement = clamp(retirement_rate / 0.15 * 8, 0, 8)
    if data.get("has_national_pension_estimate"):
        retirement += 3
    if data.get("has_pension_accounts"):
        retirement += 4
    retirement = clamp(retirement, 0, 15)

    systems = 0
    if housing_ratio <= 0.35 or housing_cost == 0:
        systems += 5
    if data.get("tax_reviewed"):
        systems += 4
    if data.get("uses_tax_advantaged_accounts"):
        systems += 3
    if data.get("housing_plan_reviewed"):
        systems += 3
    systems = clamp(systems, 0, 15)

    breakdown = {
        "cash_flow_budgeting": round(cash_flow, 1),
        "debt_stability": round(debt, 1),
        "emergency_protection": round(protection, 1),
        "investment_allocation": round(investment, 1),
        "pension_retirement": round(retirement, 1),
        "housing_tax_systems": round(systems, 1),
    }
    total = round(sum(breakdown.values()), 1)

    actions = []
    if savings_rate < 0.1:
        actions.append("Improve monthly cash flow before adding new long-term commitments.")
    if debt < 12:
        actions.append("Review debt rates and minimum payments; prioritize high-rate debt.")
    if emergency_months < 3:
        actions.append("Build emergency cash toward at least several months of essential expenses.")
    if retirement < 8:
        actions.append("Confirm National Pension estimate and retirement-account contributions.")
    if systems < 8:
        actions.append("Review housing, tax, and account-system checklists with current official rules.")

    return {
        "score": total,
        "grade": grade(total),
        "breakdown": breakdown,
        "metrics": {
            "savings_rate_percent": round(savings_rate * 100, 1),
            "emergency_months": round(emergency_months, 1),
            "debt_payment_ratio_percent": round(debt_payment_ratio * 100, 1),
            "risk_asset_ratio_percent": round(risk_asset_ratio * 100, 1),
        },
        "actions": actions[:5],
        "note": "Educational score based on provided values and assumptions; not a professional rating.",
    }


def main():
    parser = argparse.ArgumentParser(description="Calculate Financial Health Score.")
    parser.add_argument("--input", required=True, help="JSON file with score inputs.")
    args = parser.parse_args()
    print(json.dumps(calculate_score(load_input(args.input)), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
