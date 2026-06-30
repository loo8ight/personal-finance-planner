#!/usr/bin/env python3
"""Net worth and allocation calculator."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


LIQUID_KEYS = {"cash", "demand_deposit", "parking", "cma", "savings", "deposits"}
RISK_KEYS = {"stocks", "domestic_stocks", "overseas_stocks", "etf", "funds", "crypto", "alternatives"}


def load_input(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def flatten_amounts(data):
    if not data:
        return {}
    if isinstance(data, dict):
        result = {}
        for key, value in data.items():
            if isinstance(value, dict):
                result[key] = sum(float(v or 0) for v in value.values())
            else:
                result[key] = float(value or 0)
        return result
    raise ValueError("Expected a JSON object for amounts.")


def ratio(numerator, denominator):
    return 0.0 if not denominator else numerator / denominator


def calculate_networth(data):
    assets = flatten_amounts(data.get("assets", {}))
    liabilities = flatten_amounts(data.get("liabilities", {}))
    total_assets = sum(assets.values())
    total_liabilities = sum(liabilities.values())
    net_worth = total_assets - total_liabilities

    liquid_assets = sum(amount for key, amount in assets.items() if key in LIQUID_KEYS)
    risk_assets = sum(amount for key, amount in assets.items() if key in RISK_KEYS)

    allocation = []
    for key, amount in sorted(assets.items(), key=lambda item: item[1], reverse=True):
        allocation.append(
            {
                "category": key,
                "amount": round(amount),
                "share_percent": round(ratio(amount, total_assets) * 100, 1),
            }
        )

    notes = []
    if total_assets <= 0:
        notes.append("Asset values are missing or zero.")
    if total_liabilities > total_assets:
        notes.append("Liabilities exceed assets based on provided values.")
    if ratio(liquid_assets, total_assets) < 0.1 and total_assets:
        notes.append("Liquid asset share is low; emergency fund should be reviewed.")
    if ratio(risk_assets, total_assets) > 0.75:
        notes.append("Risk-asset concentration is high based on provided categories.")

    return {
        "total_assets": round(total_assets),
        "total_liabilities": round(total_liabilities),
        "net_worth": round(net_worth),
        "liquid_assets": round(liquid_assets),
        "risk_assets": round(risk_assets),
        "liquid_asset_ratio_percent": round(ratio(liquid_assets, total_assets) * 100, 1),
        "risk_asset_ratio_percent": round(ratio(risk_assets, total_assets) * 100, 1),
        "allocation": allocation,
        "notes": notes,
        "note": "Values are planning estimates unless verified from statements or appraisals.",
    }


def main():
    parser = argparse.ArgumentParser(description="Calculate net worth and allocation.")
    parser.add_argument("--input", required=True, help="JSON file with assets and liabilities.")
    args = parser.parse_args()

    print(json.dumps(calculate_networth(load_input(args.input)), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
