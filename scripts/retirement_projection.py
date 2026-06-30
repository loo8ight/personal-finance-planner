#!/usr/bin/env python3
"""Retirement projection calculator."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_input(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def future_value(current_assets, monthly_saving, annual_return, years):
    months = int(round(years * 12))
    monthly_return = annual_return / 12.0
    value = float(current_assets)
    for _ in range(months):
        value = value * (1 + monthly_return) + monthly_saving
    return value


def monthly_saving_needed(current_assets, target_assets, annual_return, years):
    if years <= 0:
        return max(0.0, target_assets - current_assets)
    low, high = 0.0, max(1.0, target_assets / max(1, years * 12))
    while future_value(current_assets, high, annual_return, years) < target_assets:
        high *= 2
        if high > target_assets:
            break
    for _ in range(80):
        mid = (low + high) / 2
        if future_value(current_assets, mid, annual_return, years) >= target_assets:
            high = mid
        else:
            low = mid
    return high


def calculate(data):
    current_age = float(data.get("current_age", 0) or 0)
    retirement_age = float(data.get("retirement_age", 65) or 65)
    years = max(0.0, retirement_age - current_age)
    monthly_spending = float(data.get("monthly_retirement_spending", 0) or 0)
    annual_spending = monthly_spending * 12
    annual_pension_income = float(data.get("annual_pension_income", 0) or 0)
    withdrawal_rate = float(data.get("withdrawal_rate", 0.04) or 0.04)
    current_assets = float(data.get("current_retirement_assets", 0) or 0)
    monthly_saving = float(data.get("monthly_retirement_saving", 0) or 0)

    annual_gap = max(0.0, annual_spending - annual_pension_income)
    required_capital = annual_gap / withdrawal_rate if withdrawal_rate else 0.0

    scenarios = data.get(
        "scenarios",
        {
            "conservative": 0.02,
            "base": 0.04,
            "optimistic": 0.06,
        },
    )

    scenario_rows = {}
    for name, annual_return in scenarios.items():
        annual_return = float(annual_return)
        projected = future_value(current_assets, monthly_saving, annual_return, years)
        needed = monthly_saving_needed(current_assets, required_capital, annual_return, years)
        scenario_rows[name] = {
            "annual_return_assumption_percent": round(annual_return * 100, 2),
            "projected_assets_at_retirement": round(projected),
            "estimated_gap": round(required_capital - projected),
            "monthly_saving_needed": round(needed),
        }

    return {
        "years_to_retirement": round(years, 1),
        "annual_retirement_spending": round(annual_spending),
        "annual_pension_income": round(annual_pension_income),
        "annual_spending_gap": round(annual_gap),
        "withdrawal_rate_percent": round(withdrawal_rate * 100, 2),
        "required_retirement_capital": round(required_capital),
        "scenarios": scenario_rows,
        "note": "Projection uses assumptions only. Pension benefits, tax, inflation, and withdrawal rules require current confirmation.",
    }


def main():
    parser = argparse.ArgumentParser(description="Project retirement readiness.")
    parser.add_argument("--input", required=True, help="JSON file with retirement inputs.")
    args = parser.parse_args()
    print(json.dumps(calculate(load_input(args.input)), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
