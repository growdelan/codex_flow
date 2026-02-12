# AGENTS.md — mapa repo (agent-first)

- Komunikacja: **po polsku**.
- Ten plik jest **mapą** (table of contents), nie monolityczną instrukcją.
- Źródła prawdy (priorytet): `AGENTS.md` → `spec.md` → `ROADMAP.md` → `STATUS.md` → `docs/**` → `plans/**` → `prd/**`.

## Jak pracujesz (w skrócie)
1. Zrozum intencję z promptu.
2. Zbierz kontekst z repo (nie z “pamięci”):
   - zawsze przeczytaj: `spec.md`, `ROADMAP.md`, `STATUS.md`, `docs/INDEX.md`
3. Jeśli coś jest niejasne: **najpierw doprecyzuj w repo** (docs/spec/roadmap/plans), dopiero potem kod.
4. Pracuj w pętli:
   - plan → implementacja → testy/smoke → self-review → poprawki → repeat
5. Jeśli narzędzia pozwalają: twórz PR, odpowiadaj na review, merge.
6. Jeśli utknąłeś: zidentyfikuj brakującą “zdolność” (guardrail/docs/tool) i dodaj ją do repo.

## Gdzie szukać czego
- “Co budujemy i po co”: `spec.md` + `docs/product.md`
- “Co teraz robimy”: `ROADMAP.md` + `STATUS.md`
- “Architektura / granice / zasady zależności”: `docs/architecture.md`
- “Jakość / Definition of Done / testy / invariants”: `docs/quality.md`
- “Zasady pracy agent-first / review loop”: `docs/agent-first.md`
- “Plany wykonawcze i log decyzji”: `plans/`

## Invariants (nie negocjuj)
- Nie zgaduj brakujących kształtów danych: waliduj na granicach lub korzystaj z typowanych SDK.
- Bez refactorów poza zakresem milestone’u.
- Zmiany w architekturze muszą być opisane w `docs/architecture.md` i/lub `spec.md` **zanim** trafią do kodu.
- Każda zmiana musi mieć:
  - uruchomienie aplikacji opisane w README (projektowym)
  - testy + smoke przechodzą lokalnie
  - aktualne `STATUS.md` i `ROADMAP.md`

## Tooling (ogólne)
- Używaj narzędzi repo (skrypty, CI, linters) zamiast ręcznych instrukcji.
- Jeśli repo nie ma checków jakości: dodaj je (i opisz w `docs/quality.md`).
