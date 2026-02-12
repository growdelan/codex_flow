# Quality & DoD

## Minimalny DoD dla każdego milestone’u
- da się uruchomić jednym poleceniem (opisanym w README projektu)
- `./scripts/check.sh` przechodzi lokalnie (lint + test + smoke)
- testy przechodzą lokalnie
- istnieje smoke test end-to-end (minimalny, ale realny)
- brak TODO/placeholderów związanych z wdrażaną funkcją
- `ROADMAP.md` i `STATUS.md` odzwierciedlają rzeczywistość

## Commands (single source of truth)

### One-command validation (preferowane)
- Full validation: `./scripts/check.sh`

### Tests
- Run all tests: `./scripts/test.sh`  
  (standard: `unittest`, uruchamiane przez `uv run python -m unittest ...` wewnątrz skryptu)

### Lint / format
- Lint: `./scripts/lint.sh`

### Python tooling (informacyjnie)
- Dependency manager: `uv`
- Instalcaja paczki `uv add <paczka>`
- Zasada: jeśli istnieje skrypt do danej czynności — **używaj skryptu**, nie “ręcznych” komend.

## Testing standard (twarde)
- Framework testów: **unittest** (Python standard library)
- Nowe testy mają być pisane w `unittest` (nie pytest).
- Pliki testów: `tests/test_*.py`
- Każdy nowy feature/fix musi mieć test(y) w `unittest`.
- Jeśli w repo są już testy w innym frameworku, nie przepisuj całości bez potrzeby — trzymaj się tej zasady dla nowych i modyfikowanych testów.

## Invariants (promote-to-code)
Jeśli coś jest ważne i powtarzalne:
- dodaj regułę tutaj
- a potem dodaj mechaniczne sprawdzenie (test/lint/CI lub skrypt w `scripts/`)

Przykłady invariants:
- walidacja danych na granicach
- structured logging
- limity wielkości plików/modułów
- zakaz nielegalnych zależności warstw (jeśli projekt ma architekturę warstwową)
