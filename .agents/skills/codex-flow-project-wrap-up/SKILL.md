---
name: codex-flow-project-wrap-up
description: >
  Użyj, gdy kończysz sesję pracy nad projektem i chcesz uporządkować stan
  dokumentacji operacyjnej bez implementacji nowych zmian: zaktualizować
  ROADMAP.md, STATUS.md oraz w razie potrzeby README.md, a następnie upewnić
  się, że bieżący stan jest zapisany w repo. Ten skill nie służy do wdrażania
  funkcji ani do tworzenia nowego planu.
---

Zrób porządek w projekcie:

1. Zaktualizuj `ROADMAP.md`:
   - statusy milestone’ów zgodnie z rzeczywistością

2. Zaktualizuj `STATUS.md`:
   - aktualny stan projektu

3. Sprawdź `README.md` i zaktualizuj go tylko wtedy, gdy ostatnie zmiany
   wpływają na informacje istotne dla człowieka:
   - sposób uruchamiania
   - wymagania
   - komendy developerskie
   - opis działania funkcji
   - ograniczenia lub ważne zachowania systemu
   Jeśli zmiany nie wpływają na te obszary, nie edytuj `README.md`.

4. Upewnij się, że wszystko jest commitowane.

Zasady:
- Nie zmieniaj kodu.
- Nie aktualizuj `README.md` kosmetycznie ani bez realnej potrzeby.
- Dokumentacja ma odzwierciedlać faktyczny stan repo.
