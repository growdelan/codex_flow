---
name: git-diff-narrator
description: "Przekłada git diff/zmiany w PR na narrację: co zmienia się w zachowaniu systemu, konsekwencje techniczne/biznesowe, ryzyka/regresje, co przetestować oraz gotowe podsumowanie do opisu PR/commit. Używaj przy code review i przed merge."
---

# Git Diff Narrator

## Cel
Nie opisuję diffa linijka po linijce. Wyjaśniam **sens** zmian: co zmieni się w systemie, jakie są skutki uboczne i ryzyka, oraz jak to dobrze opisać w PR.

## Zasada nadrzędna
**Opisuj semantykę i konsekwencje, nie składnię.**

## Procedura narracji zmian

### 1) Zakres i obszary
- Jakie moduły/warstwy dotknięte?
- Zmiana lokalna czy przekrojowa?
- Czy to refactor, feature, bugfix, hardening, performance?

### 2) Co się zmienia w zachowaniu (before/after)
W 3–8 punktach:
- **Było:** …
- **Jest:** …
- **Efekt:** …

Unikaj: listy plików i powtarzania diffa.

### 3) Konsekwencje techniczne
Sprawdź i opisz (jeśli dotyczy):
- kontrakty API (request/response/statusy)
- kompatybilność wsteczna (breaking changes)
- migracje danych / formaty / serializacja
- wpływ na wydajność i zasoby
- bezpieczeństwo (walidacja, auth, injection, tajne dane)
- obserwowalność (logi, metryki, tracing)

### 4) Konsekwencje biznesowe (jeśli widać)
- Co odczuje użytkownik/klient API?
- Czy zmiana zmienia reguły biznesowe?
- Czy to wymaga komunikacji/rolloutu?

### 5) Ryzyka i „co przetestować”
Wypisz:
- potencjalne regresje
- edge case’y
- zależności (feature flags, konfiguracja, env)
- minimalny plan testów (unit/integration/e2e)

### 6) Gotowe podsumowanie do PR / commit
Wygeneruj:
- **Tytuł PR (1 linia)**
- **Opis PR (3–6 punktów)**: co, dlaczego, zakres
- **Ryzyka/uwagi (1–3 punkty)**
- **Test plan (checklista)**

## Antywzorce
- Nie przepisuj diffa.
- Nie pomijaj skutków ubocznych.
- Nie zakładaj, że „ktoś to przetestuje”.

## Format odpowiedzi (preferowany)
1. **Zakres zmian**
2. **Zmiana zachowania (before/after)**
3. **Konsekwencje techniczne**
4. **Konsekwencje biznesowe**
5. **Ryzyka + test plan**
6. **Propozycja opisu PR/commit**

