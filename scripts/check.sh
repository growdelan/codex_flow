#!/usr/bin/env bash
set -euo pipefail

echo "==> Lint"
./scripts/lint.sh

echo "==> Tests"
./scripts/test.sh

echo "==> Smoke test"
./scripts/smoke.sh