#!/usr/bin/env python3
"""Housing affordability and loan burden calculator."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_input(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def loan_payment(principal, annual_rate, years):
    principal = float(principal or 0)
    annual_rate = float(annual_rate or 0) / 100.0
    years = float(years or 0)
    months = int(round(years * 12))
    if principal <= 0 or months <= 0:
        return 0.0
    monthly_rate = annual_rate / 12.0
    if monthly_rate == 0:
        return principal / months
    factor = (1 + monthly_rate) ** months
    return principal * monthly_rate * factor / (factor - 1)


def ratio(numerator, denominator):
    return 0.0 if not denominator else numerator / denominator


def calculate(data):
    income = float(data.get("monthly_income", 0) or 0)
    other_debt_payments = float(data.get("other_monthly_debt_payments", 0) or 0)
    options = data.get("options", [])
    results = []

    for option in options:
        name = option.get("name", "Option")
        rent = float(option.get("monthly_rent", 0) or 0)
        maintenance = float(option.get("monthly_maintenance", 0) or 0)
        loan = option.get("loan", {}) or {}
        payment = loan_payment(loan.get("principal", 0), loan.get("annual_rate", 0), loan.get("years", 0))
        total_monthly = rent + maintenance + payment
        total_debt_burden = other_debt_payments + payment
        results.append(
            {
                "name": name,
                "upfront_cash": round(float(option.get("upfront_cash", 0) or 0)),
                "monthly_rent": round(rent),
                "monthly_maintenance": round(maintenance),
                "estimated_loan_payment": round(payment),
                "total_monthly_housing_cost": round(total_monthly),
                "housing_burden_percent": round(ratio(total_monthly, income) * 100, 1),
                "debt_payment_burden_percent": round(ratio(total_debt_burden, income) * 100, 1),
                "notes": option.get("notes", ""),
            }
        )

    flags = []
    for result in results:
        if result["housing_burden_percent"] > 35:
            flags.append(f"{result['name']}: housing burden is high based on provided income.")
        if result["debt_payment_burden_percent"] > 40:
            flags.append(f"{result['name']}: debt payment burden should be stress-tested.")

    return {
        "monthly_income": round(income),
        "options": results,
        "flags": flags,
        "verification_needed": [
            "Current DSR/LTV/DTI treatment",
            "Financial-institution loan review",
            "Policy-loan eligibility",
            "Cheongyak and housing program rules",
            "Taxes, fees, insurance, and maintenance costs",
        ],
        "note": "Affordability estimate only; loan approval and regulatory treatment require current confirmation.",
    }


def main():
    parser = argparse.ArgumentParser(description="Compare housing affordability options.")
    parser.add_argument("--input", required=True, help="JSON file with housing inputs.")
    args = parser.parse_args()
    print(json.dumps(calculate(load_input(args.input)), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
