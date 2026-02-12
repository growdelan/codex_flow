#!/usr/bin/env bash
set -euo pipefail

uv sync

uv run python -m unittest discover -s tests -p "test_*.py" -v
