# Zasady nadrzędne
- Komunikuj się z użytkownikiem wyłącznie w języku polskim.
- Ten plik definiuje nadrzędne zasady pracy w projekcie.
- Jest nadrzędny wobec promptów i kodu.
- Reguły poniżej obowiązują w całym repozytorium.
- Jeśli występuje konflikt:
  1. AGENTS.md
  2. spec.md
  3. ROADMAP.md
  4. STATUS.md
- Jeśli coś jest niejednoznaczne:
  - najpierw doprecyzuj w dokumentacji
  - nie zgaduj w kodzie

---

## Build, Test, and Development Commands

### Środowisko
- Zarządzanie środowiskiem i zależnościami odbywa się przez **UV**.
- UV zarządza lokalnym środowiskiem `.venv`.
- Nie twórz alternatywnych środowisk wirtualnych.
- Jeśli wymagane, aktywacja:
  - `source .venv/bin/activate`

### Uruchamianie aplikacji
- Aplikacja musi mieć **jeden, jasno określony entrypoint**.
- Uruchomienie odbywa się jednym poleceniem, np.:
  - `uv run <plik_entrypointu.py>`  
  lub  
  - `python -m <pakiet>`
- Dokładna komenda uruchomienia **musi być opisana w README.md**.

### Zależności
- Instalacja zależności:
  - `uv add <nazwa_paczki>`
- **Nie dodawaj nowych zależności**, jeśli nie jest to konieczne.
- Każda nowa zależność:
  - musi znacząco upraszczać implementację
  - musi być uzasadniona w `spec.md` w sekcji `## Decyzje techniczne`
  - jeśli sekcja `## Decyzje techniczne` nie istnieje, **dodaj ją** (bez zmiany pozostałej struktury dokumentu)

### Testy
- Uruchamianie testów:
  - `python -m unittest discover -s tests`

---

## Coding Style & Naming Conventions
- Indentacja: 4 spacje (bez tabulatorów).
- Nazwy:
  - moduły i funkcje: `snake_case`
  - klasy: `PascalCase`
- Kod ma być prosty i czytelny:
  - unikaj „magii” i skrótów
  - komentarze dodawaj tylko tam, gdzie logika nie jest oczywista
- Nie wprowadzaj refactorów niezwiązanych bezpośrednio z aktualnym milestone’em.

---

## Testing Guidelines
- Framework testów: `unittest`
- Lokalizacja testów: katalog `tests/`
- Nazewnictwo plików testowych: `test_*.py`
- Każdy milestone:
  - musi mieć testy adekwatne do zakresu
  - musi przechodzić `python -m unittest discover -s tests`

### Smoke Test
- Smoke test:
  - nie wykonuje realnego IO (sieć, baza danych, zewnętrzne API, filesystem)
  - używa stubów lub fake’ów adekwatnych do charakteru projektu
- Celem smoke testu jest potwierdzenie, że aplikacja:
  - uruchamia się
  - wykonuje minimalny przepływ end-to-end

---

## Repository Structure
- Kod aplikacji znajduje się w jednym, spójnym miejscu:
  - `src/` (preferowane)
  - lub katalog główny projektu (dla bardzo małych aplikacji)
- Testy znajdują się wyłącznie w katalogu `tests/`.

### Entry Point
- Projekt ma **jeden** entrypoint aplikacji.
- Entrypoint:
  - znajduje się w `src/` lub w katalogu głównym
  - jest jasno wskazany w README.md
- Nie twórz wielu entrypointów bez wyraźnej potrzeby.

### Pliki top-level
- Dozwolone pliki w katalogu głównym:
  - `README.md`
  - `AGENTS.md`
  - `spec.md`
  - `ROADMAP.md`
  - `STATUS.md`
  - `PRD.md`
  - pliki konfiguracyjne (`pyproject.toml`, itp.)
- Nie dodawaj losowych plików `.py` do katalogu głównego,
  jeśli projekt używa katalogu `src/`.

### Zmiany struktury
- Nie zmieniaj struktury repozytorium bez wyraźnej potrzeby.
- Jeśli zmiana struktury jest konieczna:
  - najpierw opisz ją w `spec.md`
  - uzasadnij decyzję
  - dopiero potem zmieniaj kod

---

## Configuration & Secrets
- Nie przechowuj sekretów w repozytorium.
- Klucze API i sekrety:
  - przechowuj w zmiennych środowiskowych
  - udokumentuj wymagane zmienne w README.md
- Nie dodawaj domyślnych kluczy ani fallbacków.

---

## Commit & Pull Request Guidelines
- Commity:
  - krótkie, zrozumiałe opisy
  - preferowany styl: Conventional Commits  
    (`feat: ...`, `fix: ...`, `chore: ...`, `test: ...`)
- Każdy commit:
  - odpowiada jednemu logicznemu krokowi
  - przechodzi testy

### Pull Requests
- Przed PR:
  - przeanalizuj różnice względem `main`
- Jeśli skill `git-diff-narrator` jest dostępne:
  - użyj go do opisu zmian
- Jeśli nie:
  - opisz ręcznie:
    - co się zmieniło
    - dlaczego
    - jak zostało przetestowane

---

## Zasady Architektury
- „Architektura” obejmuje:
  - strukturę katalogów
  - sposób uruchamiania aplikacji
  - warstwy i logikę domenową
  - sposób przechowywania danych
  - publiczne API aplikacji
- Nie zmieniaj architektury bez wyraźnej prośby użytkownika.
- Jeśli zmiana architektury jest konieczna:
  - najpierw zaktualizuj `spec.md`
  - opisz decyzję i uzasadnienie
  - dopiero potem zmieniaj kod

---

## Source of Truth
- Jedynym źródłem prawdy dla:
  - decyzji technicznych
  - zakresu funkcjonalności
  - architektury
jest plik `spec.md`.

- Roadmapa i kolejność prac: `ROADMAP.md`
- Aktualny stan projektu: `STATUS.md`

Jeśli występuje konflikt między kodem a dokumentacją — **dokumentacja wygrywa**.

---

## PRD (Product Requirements Documents)

- PRD są przechowywane w katalogu `prd/`.
- Każdy PRD jest niemutowalnym dokumentem wejściowym.
- PRD nie są źródłem prawdy po ich przetworzeniu.
- Po aktualizacji `spec.md` i `ROADMAP.md`:
  - PRD służy wyłącznie jako kontekst historyczny.
- W przypadku konfliktu:
  - `spec.md` wygrywa z każdym PRD.
