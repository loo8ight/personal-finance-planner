#!/usr/bin/env python3
"""FIRE target and timeline calculator."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_input(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def years_to_target(current_assets, monthly_saving, target_assets, annual_return, max_years=80):
    if current_assets >= target_assets:
        return 0.0
    if monthly_saving <= 0 and annual_return <= 0:
        return None
    value = current_assets
    monthly_return = annual_return / 12.0
    for month in range(1, max_years * 12 + 1):
        value = value * (1 + monthly_return) + monthly_saving
        if value >= target_assets:
            return round(month / 12.0, 1)
    return None


def calculate(data):
    monthly_expenses = float(data.get("monthly_expenses", 0) or 0)
    current_assets = float(data.get("current_investable_assets", 0) or 0)
    monthly_saving = float(data.get("monthly_saving", 0) or 0)
    withdrawal_rate = float(data.get("withdrawal_rate", 0.04) or 0.04)

    annual_expenses = monthly_expenses * 12
    fire_number = annual_expenses / withdrawal_rate if withdrawal_rate else 0.0
    gap = max(0.0, fire_number - current_assets)

    scenarios = data.get(
        "scenarios",
        {
            "conservative": 0.02,
            "base": 0.04,
            "aggressive": 0.06,
        },
    )

    timeline = {}
    for name, annual_return in scenarios.items():
        annual_return = float(annual_return)
        timeline[name] = {
            "annual_return_assumption_percent": round(annual_return * 100, 2),
            "years_to_fire": years_to_target(current_assets, monthly_saving, fire_number, annual_return),
        }

    return {
        "monthly_expenses": round(monthly_expenses),
        "annual_expenses": round(annual_expenses),
        "withdrawal_rate_percent": round(withdrawal_rate * 100, 2),
        "required_fire_assets": round(fire_number),
        "current_investable_assets": round(current_assets),
        "gap": round(gap),
        "monthly_saving": round(monthly_saving),
        "scenarios": timeline,
        "note": "FIRE result depends heavily on spending, returns, inflation, tax, housing, and withdrawal assumptions.",
    }


def main():
    parser = argparse.ArgumentParser(description="Calculate FIRE target and timeline.")
    parser.add_argument("--input", required=True, help="JSON file with FIRE inputs.")
    args = parser.parse_args()
    print(json.dumps(calculate(load_input(args.input)), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
