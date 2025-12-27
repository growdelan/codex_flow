# Komunikacja z użytkownikiem
Komunikuj się z użytkownikiem w języku polskim

# Inicjacja AGENTS.md
Podczas inicjacji pliku AGENTS.md w projektach, dodaj poniższe kategorie w następujący sposób:

## Build, Test, and Development Commands
- `python -m unittest discover -s tests` — uruchamia wszystkie testy w `tests/`.
- `source .venv/bin/activate` — lokalne środowisko wirtualne.
- `uv add <nazwa_paczki>` — instalacja zależności.
- `uv run <nazwa_pliku.py>` - uruchomienie modułu/kodu

## Coding Style & Naming Conventions
- Indentacja: 4 spacje, bez tabulatorów.
- Nazwy: moduły i funkcje w `snake_case`, klasy w `PascalCase`.
- Unikaj kodu „na skróty”; krótkie komentarze dodawaj tylko tam, gdzie logika nie jest oczywista.

## Testing Guidelines
- Testy używają `unittest` i są trzymane w `tests/` z nazwami `test_*.py`.
- Smoke test nie wykonuje realnych wywołań; używa prostego `fetcher` stub.
- Dla każdego milestone dodaj testy i uruchom `python -m unittest discover -s tests`.

## Configuration & Secrets
- Nie przechowuj sekretów w repozytorium. Jeśli aplikacja będzie wymagać kluczy/API, trzymaj je w zmiennych środowiskowych i udokumentuj w README.

## Commit & Pull Request Guidelines
- Dla commitow w repozytorium; przyjmij zrozumiale, krotkie opisy (w stylu Conventional Commits: `feat: ...`, `fix: ...`).
- dla PR przeanalizuj różnice między moim branchem a main wykorzystując skill - `git-diff-narrator`

## Source of Truth
- Szczegoly funkcji, decyzji i architektury: `spec.md`.
