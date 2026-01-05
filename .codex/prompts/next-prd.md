---
description: Generuje z kolejnego PRD - spec.md i ROADMAP.md
argument-hint: PRD_NAME=<name>
---

Na podstawie nowej funkcjonalności opisanej w pliku `prd/$PRD_NAME`:

## CZĘŚĆ 1 — Aktualizacja specyfikacji
1. Zaktualizuj istniejący plik `spec.md`, korzystając z jego OBECNEJ struktury.
2. Nie zmieniaj nagłówków, nazw sekcji ani kolejności w `spec.md`.
3. Dodaj lub rozszerz treść tylko w sekcjach, których dotyczy nowe PRD.
4. Nie usuwaj ani nie reinterpretuj wcześniejszych decyzji.
5. Jeśli nowa funkcjonalność wymaga nowych decyzji technicznych:
   - dodaj je do sekcji `## Decyzje techniczne`
   - jasno zaznacz, że dotyczą nowej funkcjonalności.

## CZĘŚĆ 2 — Aktualizacja roadmapy
6. Zaktualizuj istniejący plik `ROADMAP.md`.
7. Nie zmieniaj treści ani statusów istniejących milestone’ów.
8. Dodaj nowe milestone’y wynikające z PRD:
   - na końcu roadmapy
   - z nowymi numerami
9. Każdy nowy milestone musi zawierać:
   - Cel
   - Definition of Done
   - Zakres
10. Nowe milestone’y muszą być:
    - spójne z istniejącą specyfikacją
    - możliwe do realizacji iteracyjnie

## Zasady ogólne:
- Nie zmieniaj struktury `spec.md` ani `ROADMAP.md`.
- Nie zmieniaj kodu.
- Jeśli nowe PRD jest w konflikcie z istniejącą specyfikacją:
  - opisz konflikt w `spec.md` (sekcja `## Decyzje techniczne`)
  - nie rozwiązuj go samodzielnie.
