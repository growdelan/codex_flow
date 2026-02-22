---
description: "sprawdza samego siebie aby znaleźć niespójności i złamanie zasad"
---


Wykonaj self-review ostatnich zmian.

Cel:
- sprawdzić spójność implementacji z dokumentacją
- wykryć niespójności
- wykryć złamanie zasad projektu

Krok 1 — zgodność z ROADMAP
- sprawdź czy zakres zmiany odpowiada Definition of Done aktualnego milestone’u
- sprawdź czy nie dodano funkcji spoza zakresu

Krok 2 — zgodność ze specyfikacją
- sprawdź czy implementacja jest spójna z `spec.md`
- sprawdź czy nie złamano wcześniejszych decyzji technicznych

Krok 3 — zgodność z AGENTS.md
- sprawdź czy:
  - użyto poprawnej struktury repo
  - nie dodano zależności bez uzasadnienia
  - testy istnieją i są zgodne z zasadami
  - entrypoint jest poprawnie opisany

Krok 4 — jakość kodu
- zbędne abstrakcje?
- duplikacja logiki?
- nadmierna złożoność?
- martwy kod?

Zasady:
- niczego jeszcze nie zmieniaj
- wypisz listę problemów (jeśli istnieją)
- zaproponuj konkretne poprawki

Jeśli wszystko jest poprawne:
- napisz jasno: "Self-review zakończony – brak problemów krytycznych."
