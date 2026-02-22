---
description: "poprawia jakość kodu"
---


Zrób improvement pass dla całego repozytorium.

Cel:
- poprawa jakości kodu
- uproszczenie implementacji
- redukcja zbędnej złożoności

Zasady:
- NIE dodawaj nowych funkcjonalności
- NIE zmieniaj architektury systemu
- NIE zmieniaj publicznych interfejsów (chyba że są ewidentnie błędne)
- NIE zmieniaj `ROADMAP.md`
- NIE zmieniaj zakresu milestone’ów

Co możesz zrobić:
- uprościć logikę
- usunąć martwy kod
- połączyć nadmiarowe warstwy
- poprawić nazewnictwo
- poprawić testy
- usunąć zbędne abstrakcje
- poprawić czytelność

Jeśli zmiana wpływa na decyzje techniczne:
- zaktualizuj `spec.md` → sekcja `## Decyzje techniczne`

Po zakończeniu:
- uruchom testy
- upewnij się, że wszystko działa
- zrób commit z opisem: "improvement pass – <krótki opis zmian>"
