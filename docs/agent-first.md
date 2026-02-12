---
owner: <ty/albo team>
status: draft
last_verified: 2026-02-12
---

# Agent-first operating model

## Zasada
Humans steer, agents execute.

## Pętla pracy (zawsze)
1. Ustal kryteria i zakres (ROADMAP/spec/docs)
2. Zrób plan (dla większych zmian: `plans/<id>-<temat>.md`)
3. Implementuj
4. Uruchom testy + smoke
5. Self-review: diff + checklist jakości
6. Poprawki aż wszystko jest green
7. Update docs/status/roadmap
8. PR → review (agent-to-agent) → merge

## Kiedy eskalować do człowieka
Tylko gdy potrzebny jest osąd/priorytet/produktowa decyzja.
Wtedy:
- opisz 2–3 opcje
- konsekwencje
- rekomendację
- i gdzie to zapiszesz w repo po decyzji
