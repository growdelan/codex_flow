#!/usr/bin/env bash
set -euo pipefail

python -m compileall -q src

PKG=$(python - <<'PY'
import tomllib, pathlib
data = tomllib.loads(pathlib.Path("pyproject.toml").read_text())
print(data["project"]["name"].replace("-", "_"))
PY
)

test -d "src/$PKG"

python -c "import $PKG"