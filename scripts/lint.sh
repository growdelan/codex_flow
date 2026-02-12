#!/usr/bin/env bash
set -euo pipefail

uv add ruff
uv run ruff check .
