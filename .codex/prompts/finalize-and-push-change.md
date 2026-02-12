---
description: Finalizacja w trybie agent-first (update docs + PR/merge)
---

Finalizujesz zmianę w trybie agent-first.

1) Zweryfikuj DoD milestone’u:
- testy przechodzą
- smoke przechodzi
- uruchomienie jest opisane w README projektu
- brak TODO/placeholderów związanych ze zmianą

2) Zaktualizuj:
- `ROADMAP.md` → milestone na `done`
- `STATUS.md` → co działa / co skończone / co następne / blokery
- `spec.md` → `## Decyzje techniczne` (jeśli doszły nowe decyzje)
- `docs/**` jeśli zmiana wpływa na zasady jakości lub architekturę

3) Commit + push.
4) Jeśli możliwe: otwórz PR, przejdź przez review i zmerguj.

Zasady:
- Nie zmieniaj kodu poza poprawkami wynikającymi z DoD (np. brakujące testy).
