---
description: Generuje z kolejnego PRD - spec.md i ROADMAP.md
argument-hint: PRD_NAME=<name>
---

Na podstawie pliku `prd/$PRD_NAME`:

## ETAP 0 --- Ocena zmiany

0.1. Oceń zakres zmiany: **MAŁY / ŚREDNI / DUŻY**\
0.2. Oceń czy wpływa na istniejące milestone'y.\
0.3. Oceń czy istnieje potencjalny konflikt ze spec.\
0.4. Nie zapisuj tej oceny do plików.

------------------------------------------------------------------------

## ETAP 1 --- Aktualizacja specyfikacji

1. Zaktualizuj `spec.md`, zachowując OBECNĄ strukturę.
2. Nie zmieniaj nagłówków ani kolejności sekcji.
3. Rozszerz tylko te sekcje, których dotyczy nowe PRD.
4. Nie usuwaj wcześniejszych decyzji.
5. Nowe decyzje techniczne dodaj do `## Decyzje techniczne` z oznaczeniem `(dotyczy PRD: $PRD_NAME)`.
6. Jeśli pojawia się konflikt:
   - opisz go w `## Decyzje techniczne`
   - nie rozwiązuj go samodzielnie
   - nie nadpisuj istniejących decyzji
7. Jeśli brakuje informacji, dodaj:

```{=html}
<!-- -->
```
    TODO: [KONKRETNE PYTANIE DO DOPRECYZOWANIA]

------------------------------------------------------------------------

## ETAP 2 --- Aktualizacja roadmapy

8. Zaktualizuj `ROADMAP.md`.
9. Nie zmieniaj istniejących milestone'ów ani ich statusów.
10. Nowe milestone'y dodaj na końcu z kolejną numeracją.
11. Każdy nowy milestone musi zawierać:

- Cel
- Definition of Done
- Zakres

12. Jeśli zakres = DUŻY:
- podziel implementację na mniejsze kroki
- dodaj milestone redukcji ryzyka

------------------------------------------------------------------------

## ETAP 3 --- Spójność

13. Sprawdź:
- czy nowe milestone'y wynikają z aktualizacji spec
- czy nie powstały sprzeczności
- czy kolejność realizacji jest logiczna

------------------------------------------------------------------------

## Zasady ogólne

- Nie zmieniaj struktury plików.
- Nie zmieniaj kodu.
- Nie zgaduj brakujących informacji.
- Generuj konkretne pytania zamiast domysłów.
