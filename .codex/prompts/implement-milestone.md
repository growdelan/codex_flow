---
description: zaimplementuj konkretny milestone w trybie agent-first
argument-hint: MILESTONE_ID=<id>
---

Zaimplementuj milestone z `ROADMAP.md`: Milestone $MILESTONE_ID

Tryb agent-first:
- Ty wykonujesz całość end-to-end (kod/testy/docs/PR), człowiek tylko steruje intencją.

Kroki:
1) Kontekst:
   - przeczytaj `spec.md`, `ROADMAP.md`, `STATUS.md`, `docs/index.md`
2) Ustal zakres milestone’u:
   - realizuj wyłącznie “Zakres” milestone’u
   - DoD traktuj jako twarde kryteria
3) Jeśli coś jest niejasne:
   - doprecyzuj najpierw `ROADMAP.md` lub `spec.md` lub `docs/**`
   - NIE zgaduj w kodzie

Plan:
4) Jeśli zmiana ma więcej niż 2 kroki, utwórz `plans/$MILESTONE_ID-<krotki-temat>.md` i zapisz:
   - kroki wykonania
   - ryzyka
   - decyzje (jeśli są)

Implementacja:
5) Zaimplementuj rozwiązanie minimalnie, bez refactorów poza zakresem.
6) Uruchom testy + smoke.

Self-review loop (obowiązkowo):
7) Zrób self-review:
   - przejrzyj diff
   - sprawdź zgodność z DoD
   - usuń TODO/placeholdery związane z funkcją
8) Jeśli coś nie przechodzi / jest słabe:
   - popraw i wróć do kroku 6
   Loop until: testy przechodzą + smoke przechodzi + DoD spełnione.

Finalize:
9) Zaktualizuj `STATUS.md` i (jeśli trzeba) `spec.md` / `docs/**`.
10) Zrób commit(y) o czytelnych nazwach.

Jeśli narzędzia pozwalają:
- otwórz PR
- opisz zakres + testy
- doprowadź do merge.
