---
description: start nowego projektu, tworzenie spec.md, ROADMAP.md  i STATUS.md
---

Utwórz pliki `spec.md`, `ROADMAP.md` i `STATUS.md` jako szablony w ustalonym układzie.

`spec.md` ma zawierać DOKŁADNIE poniższy szablon.
Nie zmieniaj nazw sekcji, nagłówków ani kolejności.
Nie uzupełniaj treści merytorycznej.

====================
# Specyfikacja techniczna

## Cel
Krótki opis celu aplikacji:
- jaki problem rozwiązuje
- dla kogo
- w jakim zakresie (co jest poza zakresem)

---

## Zakres funkcjonalny (high-level)
Opis funkcjonalności na wysokim poziomie:
- kluczowe use-case’i
- główne przepływy użytkownika
- czego aplikacja **nie** robi

Bez wchodzenia w szczegóły implementacyjne.

---

## Architektura i przepływ danych
Opis architektury na poziomie koncepcyjnym.

1. Główne komponenty systemu
2. Przepływ danych między komponentami
3. Granice odpowiedzialności

---

## Komponenty techniczne
Lista kluczowych komponentów technicznych i ich odpowiedzialności.

---

## Decyzje techniczne
Jawne decyzje techniczne wraz z uzasadnieniem.

Każda decyzja powinna zawierać:
- Decyzja:
- Uzasadnienie:
- Konsekwencje:

---

## Jakość i kryteria akceptacji
Wspólne wymagania jakościowe dla całego projektu.

---

## Zasady zmian i ewolucji
- zmiany funkcjonalne → aktualizacja `ROADMAP.md`
- zmiany architektoniczne → aktualizacja tej specyfikacji
- nowe zależności → wpis do `## Decyzje techniczne`
- refactory tylko w ramach aktualnego milestone’u

---

## Powiązanie z roadmapą
- Szczegóły milestone’ów i ich statusy znajdują się w `ROADMAP.md`.

---

## Status specyfikacji
- Data utworzenia:
- Ostatnia aktualizacja:
- Aktualny zakres obowiązywania:

====================

`ROADMAP.md` ma zawierać DOKŁADNIE poniższy szablon.
Nie zmieniaj struktury ani statusów.
Nie uzupełniaj treści merytorycznej.

====================
# Roadmapa (milestones)

## Statusy milestone’ów
Dozwolone statusy:
- planned
- in_progress
- done
- blocked

---

## Milestone 0.5: Minimal end-to-end slice (planned)

Cel:
- aplikacja uruchamia się
- wykonuje jedno bardzo proste zadanie
- zwraca poprawny wynik

Definition of Done:
- aplikację da się uruchomić jednym poleceniem (opisanym w README.md)
- istnieje co najmniej jeden smoke test
- testy przechodzą lokalnie
- brak placeholderów w kodzie

Zakres:
- minimalny entrypoint aplikacji
- minimalna logika domenowa
- minimalna obsługa IO (jeśli dotyczy)
- smoke test end-to-end

---

## Milestone <numer>: <nazwa> (<status>)

Cel:
Definition of Done:
Zakres:
Uwagi:

====================

`STATUS.md` ma zawierać DOKŁADNIE poniższy szablon.
Nie uzupełniaj treści merytorycznej.

====================
# Aktualny stan projektu

## Co działa

## Co jest skończone

## Co jest w trakcie

## Co jest następne

## Blokery i ryzyka

## Ostatnie aktualizacje

====================

Nie zmieniaj kodu.
