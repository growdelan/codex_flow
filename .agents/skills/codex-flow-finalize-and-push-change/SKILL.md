---
name: codex-flow-finalize-and-push-change
description: >
  Użyj po zakończeniu implementacji, gdy zmiana działa i trzeba domknąć pracę:
  zaktualizować ROADMAP.md, STATUS.md i ewentualnie spec.md, a następnie zrobić
  commit oraz push, jeśli repozytorium ma skonfigurowany remote. Ten skill nie
  służy do implementacji kodu ani planowania zmian.
---

Zmiana działa poprawnie.

1. Zaktualizuj `ROADMAP.md`:
   - oznacz wykonany milestone jako `done`

2. Zaktualizuj `STATUS.md`:
   - co działa
   - co jest skończone
   - co jest następne
   - (jeśli istnieją) blokery

3. Jeśli pojawiły się nowe decyzje:
   - zaktualizuj `spec.md` (`## Decyzje techniczne`)

Zasady:
- Nie zmieniaj kodu.
- Zrób commit. Jeśli w repozytorium jest ustawiony remote-url to zrób push.
