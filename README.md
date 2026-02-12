# Codex Flow (agent-first)

Ten repo to **szablon pracy agent-first** z Codex:
- **Human = intencja + kryteria + priorytety**
- **Agent = wykonanie end-to-end** (kod, testy, CI, docs, refactor w zakresie, PR, odpowiedzi na review, merge)

Klucz: repo jest **systemem prawdy**. To, czego agent nie widzi w repo, “nie istnieje”.

---

## Zasady nadrzędne (TL;DR)
1. **Nie piszemy kodu ręcznie** (jeśli się da — 0 manual code).
2. **AGENTS.md to mapa**, nie instrukcja na 1000 linijek.
3. Wiedza żyje w `docs/` i jest weryfikowana mechanicznie (CI/lintery/zasady).
4. Praca przebiega w pętli: **plan → implementacja → self-review → checks → agent-review → fix → repeat → merge**.
5. Jeśli agent się wykłada: nie “try harder”, tylko **dodaj brakującą zdolność** (docs/tooling/guardrail) i każ agentowi to wdrożyć.

---

## Struktura wiedzy w repo (system of record)
- `spec.md` — high-level spec + decyzje techniczne
- `ROADMAP.md` — milestones i DoD
- `STATUS.md` — aktualny stan
- `docs/` — repozytorium wiedzy (mapa, architektura, jakość, zasady)
- `plans/` — plany wykonawcze i log decyzji dla większych zmian
- `prd/` — PRD historyczne (niemutowalne)
- `src/` - aplikacja

> Zasada: jeśli coś ustaliliście na czacie/spotkaniu — dopisz to do repo w `docs/` lub `spec.md`.

---

## Start nowego projektu (agent-first)
1. Utwórz PRD wraz z GPT 
2. Utwórz puste repo `uv init <projekt>` (tylko `README.md` z 1 zdaniem: “co to jest za produkt”).
3. w projekcie `uv add ruff`
3. W Codex uruchom:
   - `/prompts:start-new-project`
   - `/prompts:generate-spec-from-prd` (po dodaniu `prd/000-initial-prd.md`)
4. Następnie od razu uruchom:
   - `/prompts:bootstrap-agent-first`
   To stworzy `docs/` (mapę wiedzy), `plans/` oraz podstawowe reguły “jak pracujemy”.

---

## Realizacja milestone’ów (agent-first)
Dla każdego milestone’u:
1. `/prompts:implement-milestone MILESTONE_ID=<id>`

Agent ma obowiązek:
- stworzyć/uzupełnić plan w `plans/`
- zaimplementować wyłącznie zakres milestone’u
- uruchomić testy + smoke
- zrobić self-review (diff + checklist)
- uruchomić pętlę napraw aż wszystkie checki przechodzą

2. Po wykonaniu agent sam robi:
- aktualizację `ROADMAP.md` / `STATUS.md` / (ew. `spec.md`)
- commit, PR, push, a na końcu merge (jeśli narzędzia pozwalają)

---

## Nowy kontekst / kontynuacja
- `/prompts:continue-project`  
Agent czyta repo, wskazuje aktualny milestone, **nic nie implementuje**.

---

## Nowy PRD
1. dodaj do `prd/<kolejny>.md`
2. `/prompts:next-prd PRD_NAME=<plik.md>`
3. potem standardowo `/prompts:implement-milestone ...`

---

## Reguła “promote to code”
Jeśli powtarza się problem (styl, architektura, testy, naming, logowanie, drift):
- nie dopisuj kolejnej linijki “proszę pamiętaj”
- dopisz zasadę do `docs/quality.md` **i każ agentowi dodać mechaniczne sprawdzenie** (linter/test/CI)
