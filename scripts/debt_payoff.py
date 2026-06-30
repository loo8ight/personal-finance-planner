#!/usr/bin/env python3
"""Debt payoff simulator for avalanche and snowball strategies."""

from __future__ import annotations

import argparse
import json
from copy import deepcopy
from pathlib import Path


def load_input(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def normalize_debt(raw):
    return {
        "name": str(raw.get("name", "Debt")),
        "balance": max(0.0, float(raw.get("balance", 0))),
        "annual_rate": max(0.0, float(raw.get("annual_rate", raw.get("rate", 0)))) / 100.0,
        "minimum_payment": max(0.0, float(raw.get("minimum_payment", raw.get("payment", 0)))),
    }


def choose_target(debts, strategy):
    active = [debt for debt in debts if debt["balance"] > 0.005]
    if not active:
        return None
    if strategy == "snowball":
        return min(active, key=lambda debt: (debt["balance"], -debt["annual_rate"]))
    return max(active, key=lambda debt: (debt["annual_rate"], debt["balance"]))


def simulate(raw_debts, extra_payment, strategy, max_months=1200):
    debts = [normalize_debt(debt) for debt in deepcopy(raw_debts)]
    month = 0
    total_interest = 0.0
    payoff_log = []

    if sum(debt["minimum_payment"] for debt in debts) + extra_payment <= 0:
        return {
            "strategy": strategy,
            "months": None,
            "total_interest": None,
            "payoff_order": [],
            "warning": "No payment capacity was provided.",
        }

    while any(debt["balance"] > 0.005 for debt in debts) and month < max_months:
        month += 1
        for debt in debts:
            if debt["balance"] <= 0.005:
                continue
            interest = debt["balance"] * debt["annual_rate"] / 12.0
            debt["balance"] += interest
            total_interest += interest

        available_extra = float(extra_payment)
        for debt in debts:
            if debt["balance"] <= 0.005:
                continue
            payment = min(debt["minimum_payment"], debt["balance"])
            debt["balance"] -= payment
            if debt["balance"] <= 0.005 and debt["name"] not in payoff_log:
                payoff_log.append(debt["name"])

        target = choose_target(debts, strategy)
        while target and available_extra > 0.005:
            payment = min(available_extra, target["balance"])
            target["balance"] -= payment
            available_extra -= payment
            if target["balance"] <= 0.005 and target["name"] not in payoff_log:
                payoff_log.append(target["name"])
            target = choose_target(debts, strategy)

    warning = None
    if month >= max_months:
        warning = "Simulation reached the maximum month limit; payment may be too low."

    return {
        "strategy": strategy,
        "months": month if not warning else None,
        "years": round(month / 12.0, 1) if not warning else None,
        "total_interest": round(total_interest),
        "payoff_order": payoff_log,
        "warning": warning,
    }


def main():
    parser = argparse.ArgumentParser(description="Simulate debt payoff strategies.")
    parser.add_argument("--input", required=True, help="JSON file with debts and optional extra_payment.")
    parser.add_argument("--extra", type=float, default=None, help="Extra monthly payoff capacity.")
    args = parser.parse_args()

    data = load_input(args.input)
    debts = data.get("debts", data if isinstance(data, list) else [])
    extra_payment = args.extra if args.extra is not None else float(data.get("extra_payment", 0))

    result = {
        "extra_payment": round(extra_payment),
        "avalanche": simulate(debts, extra_payment, "avalanche"),
        "snowball": simulate(debts, extra_payment, "snowball"),
        "note": "Approximate estimate. Actual interest, fees, grace periods, and refinancing terms require lender confirmation.",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
