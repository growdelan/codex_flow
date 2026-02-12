---
owner: <ty/albo team>
status: draft
last_verified: 2026-02-12
---

# Architecture

## Cel
Dać agentowi “mapę” komponentów i granic odpowiedzialności.

## Zasady
- Zmiany architektury muszą być tu opisane przed wdrożeniem.
- Granice i zależności muszą być możliwe do sprawdzenia mechanicznie (test/lint), jeśli projekt rośnie.
- Nie refactoruj architektury poza zakresem milestone’u.
- Nie zgaduj danych na granicach — waliduj.

## Repo layout conventions (twarde, NIE ZMIENIAĆ)
- Application code: `src/`
- Tests: `tests/`
- Scripts: `scripts/`
- Docs: `docs/`
- Plans: `plans/`

## Mapa systemu (do uzupełnienia)
<!-- ARCH_MAP:BEGIN -->
TODO: Uzupełnij mapę systemu na bazie istniejącego kodu i/lub `spec.md`.
- Komponenty:
- Przepływ danych:
- Granice odpowiedzialności:
- Kontrakty na granicach (walidacja/typy):
<!-- ARCH_MAP:END -->
