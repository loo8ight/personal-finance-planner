#!/usr/bin/env python3
"""Budget and cash-flow calculator for Personal Finance Planner."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def money_sum(value):
    if value is None:
        return 0.0
    if isinstance(value, dict):
        return sum(money_sum(v) for v in value.values())
    if isinstance(value, list):
        return sum(money_sum(v) for v in value)
    return float(value)


def ratio(numerator, denominator):
    return 0.0 if not denominator else numerator / denominator


def percent(value):
    return round(value * 100, 1)


def load_input(path):
    if not path:
        return {}
    return json.loads(Path(path).read_text(encoding="utf-8"))


def calculate_budget(data):
    income = money_sum(data.get("income"))
    fixed = money_sum(data.get("fixed_costs"))
    variable = money_sum(data.get("variable_costs"))
    subscriptions = money_sum(data.get("subscriptions"))
    debt_payments = money_sum(data.get("debt_payments"))
    savings = money_sum(data.get("savings"))

    total_spending = fixed + variable + subscriptions + debt_payments
    surplus = income - total_spending - savings
    calculated_savings = income - total_spending
    savings_rate = ratio(savings if savings else calculated_savings, income)

    flags = []
    if income <= 0:
        flags.append("Monthly income is missing or zero.")
    if ratio(fixed + debt_payments, income) > 0.65:
        flags.append("Fixed costs and debt payments are taking a large share of income.")
    if savings_rate < 0.1:
        flags.append("Savings rate is low based on the provided values.")
    if subscriptions > income * 0.05 and income:
        flags.append("Subscriptions exceed 5 percent of monthly income.")
    if surplus < 0:
        flags.append("Budget shows a monthly shortfall after planned savings.")

    actions = []
    if surplus < 0:
        actions.append("Find the shortfall source before adding new goals.")
    if subscriptions:
        actions.append("Review subscriptions and automatic payments this month.")
    if savings_rate < 0.1:
        actions.append("Set one realistic automatic savings amount after essentials.")
    if debt_payments:
        actions.append("Separate minimum debt payments from extra payoff capacity.")

    return {
        "monthly_income": round(income),
        "fixed_costs": round(fixed),
        "variable_costs": round(variable),
        "subscriptions": round(subscriptions),
        "debt_payments": round(debt_payments),
        "planned_savings": round(savings),
        "total_spending_before_savings": round(total_spending),
        "surplus_after_spending_and_savings": round(surplus),
        "savings_rate_percent": percent(savings_rate),
        "fixed_cost_ratio_percent": percent(ratio(fixed, income)),
        "variable_cost_ratio_percent": percent(ratio(variable, income)),
        "debt_payment_burden_percent": percent(ratio(debt_payments, income)),
        "risk_flags": flags,
        "actions": actions[:5],
        "note": "Educational estimate based on provided values; verify missing or irregular items.",
    }


def main():
    parser = argparse.ArgumentParser(description="Calculate monthly budget metrics.")
    parser.add_argument("--input", help="Path to JSON input.")
    parser.add_argument("--income", type=float, help="Monthly income override.")
    parser.add_argument("--fixed", type=float, default=None, help="Fixed costs override.")
    parser.add_argument("--variable", type=float, default=None, help="Variable costs override.")
    parser.add_argument("--savings", type=float, default=None, help="Planned monthly savings override.")
    args = parser.parse_args()

    data = load_input(args.input)
    if args.income is not None:
        data["income"] = args.income
    if args.fixed is not None:
        data["fixed_costs"] = args.fixed
    if args.variable is not None:
        data["variable_costs"] = args.variable
    if args.savings is not None:
        data["savings"] = args.savings

    print(json.dumps(calculate_budget(data), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
