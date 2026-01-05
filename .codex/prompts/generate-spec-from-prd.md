---
description: Generuje z PRD nowe pliki spec.md i ROADMAP.md
---

Na podstawie pliku `prd/000-initial-prd.md`:

## CZĘŚĆ 1 — Specyfikacja
1. Wypełnij treścią istniejący plik `spec.md`, korzystając z jego OBECNEJ struktury.
2. Nie zmieniaj nagłówków, nazw sekcji ani kolejności w `spec.md`.
3. Uzupełnij każdą sekcję na poziomie wysokim (bez szczegółów implementacyjnych).
4. Jeśli którejś sekcji nie da się uzupełnić na podstawie PRD:
   - zostaw krótką notatkę `TODO` z opisem brakującej informacji.
5. Decyzje techniczne wpisuj wyłącznie do sekcji `## Decyzje techniczne`
   i tylko jeśli wynikają bezpośrednio z PRD.

## CZĘŚĆ 2 — Roadmapa
6. Wypełnij istniejący plik `ROADMAP.md`, zachowując jego strukturę.
7. Nie zmieniaj nazw sekcji ani dozwolonych statusów milestone’ów.
8. Zachowaj Milestone 0.5 jako pierwszy element roadmapy.
9. Dodaj kolejne milestone’y po Milestone 0.5.
10. Każdy milestone musi zawierać:
    - Cel
    - Definition of Done
    - Zakres

## Zasady:
- Nie zmieniaj struktury `spec.md` ani `ROADMAP.md`.
- Nie zmieniaj kodu.
- Jeśli coś jest niejednoznaczne, użyj `TODO` zamiast zgadywania.
