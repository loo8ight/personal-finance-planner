#!/usr/bin/env python3
"""Convert an existing HTML report to PDF with local browser tooling."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from generate_report import convert_html_to_pdf

try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass


def main():
    parser = argparse.ArgumentParser(description="Convert HTML report to PDF.")
    parser.add_argument("--html", required=True, help="Path to an HTML report.")
    parser.add_argument("--pdf", help="Output PDF path. Defaults to the HTML path with .pdf suffix.")
    args = parser.parse_args()

    html_path = Path(args.html)
    pdf_path = Path(args.pdf) if args.pdf else html_path.with_suffix(".pdf")
    result, note = convert_html_to_pdf(html_path, pdf_path)
    print(json.dumps({"pdf_report": result, "note": note}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
