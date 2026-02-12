---
description: Bootstrap agent-first after template copy (fill project specifics + validate repo knowledge)
---

Założenie: szablon agent-first został już skopiowany do repo:
- `AGENTS.md`
- `docs/**`
- `plans/**`

Twoje zadanie nie polega na tworzeniu tych plików, tylko na ich dopasowaniu do projektu i walidacji.

1) Sprawdź, że istnieją:
- `AGENTS.md`
- `docs/index.md`
- `docs/product.md`
- `docs/quality.md`
- `docs/architecture.md`
- `docs/agent-first.md`
- `plans/README.md`


2) Uzupełnij projektowo `docs/product.md` na bazie:
- `README.md`
- `spec.md` (jeśli istnieje)
- `ROADMAP.md` (jeśli istnieje)
Maks 10–20 linii, konkretnie: co, dla kogo, use-case, poza zakresem.

3) Uzupełnij `docs/architecture.md`:
- jeśli repo ma już kod/strukturę, dopisz minimalną mapę komponentów i granic
- jeśli nie ma danych, zostaw TODO + napisz dokładnie gdzie to doprecyzować (np. `spec.md`)

4) Zweryfikuj spójność mapy:
- `docs/index.md` ma linki do realnie istniejących plików
- jeśli `spec.md`/`STATUS.md`/`ROADMAP.md` nie istnieją, dopisz w INDEX “TODO: add …” zamiast linku do nieistniejącego pliku

5) Commit:
- `chore: bootstrap agent-first project docs`
