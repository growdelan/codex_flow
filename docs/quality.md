# Quality & DoD

## Minimalny DoD dla każdego milestone’u
- da się uruchomić jednym poleceniem (opisanym w README projektu)
- testy przechodzą lokalnie
- istnieje smoke test end-to-end (minimalny, ale realny)
- brak TODO/placeholderów związanych z wdrażaną funkcją
- `ROADMAP.md` i `STATUS.md` odzwierciedlają rzeczywistość

## Invariants (promote-to-code)
Jeśli coś jest ważne i powtarzalne:
- dodaj regułę tutaj
- a potem dodaj mechaniczne sprawdzenie (test/lint/CI)

Przykłady invariants:
- walidacja danych na granicach
- structured logging
- limity wielkości plików/modułów
- zakaz nielegalnych zależności warstw (jeśli projekt ma architekturę warstwową)
