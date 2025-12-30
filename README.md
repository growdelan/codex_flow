# Codex Flow

## Konfiguracja Codex

Skopiowanie zawartości z [.codex](https://github.com/growdelan/codex_flow/blob/main/.codex) do swojego `~/.codex/` (domyślnie wykorzstanie `Pythona` + `UV`)
  
## 1. PRD w GPT  
  
Poprosić o PRD do nowego projektu za pomocą promptu podmieniająć `[nazwa lub krótki opis produktu/usługi]` na własny opis:  
```
Jesteś ekspertem w tworzeniu dokumentów PRD (Product Requirements Document) dla aplikacji.

Chciałbym stworzyć PRD dla [nazwa lub krótki opis produktu/usługi]. 

Przeprowadź ze mną wywiad – zadawaj mi pytania jedno po drugim, aż poznasz cały potrzebny kontekst do stworzenia dokumentu dla mojej aplikacji. 

Gdy będziesz miał wystarczający kontekst, przejdź do utworzenia dokumentu w formacie markdown.
```
Na koniec poprosić aby podsumował cała aplikację tylko jednym zdaniem. (Przyda się za chwile)  
  
## 2. Utworzenie repozytorium projektu  
* Tworzymy czyste repozytorium tylko z `README.md` i pobieramy na dysk.  
* Po pobraniu edytujemy plik `README.md` i wklejamy do niego to pojedyncze zdanie na temat naszej aplikacji, które wygenerował `GPT`, i zapisujemy.

> ⚠️ **UWAGA**  
> Jeśli nie skopiowałeś pliku [.codex](https://github.com/growdelan/codex_flow/blob/main/.codex) do `~/.codex/`,  
> uruchom `Codex` a następnie wykonaj komendę `/init`.  
> Spowoduje to utworzenie domyślnego pliku `AGENTS.md`.
  
Uruchamiamy Codex i wykonujemy prompt `/prompts:start-new-project`:  
```
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
```
Z tak przygotowanym repozytorium jesteśmy gotowi do pracy.  
  
## 3. Rozpoczęcie projektu  
W Repozytorium tworzymy plik `PRD.md` z naszym PRD utworzonym przez `GPT` i zapisujemy w katalogu głównym.  
  
Następnie w Codex uruchamiamy prompt `/prompts:generate-spec-from-prd`:  
```
Na podstawie pliku `PRD.md`:

CZĘŚĆ 1 — Specyfikacja
1. Wypełnij treścią istniejący plik `spec.md`, korzystając z jego OBECNEJ struktury.
2. Nie zmieniaj nagłówków, nazw sekcji ani kolejności w `spec.md`.
3. Uzupełnij każdą sekcję na poziomie wysokim (bez szczegółów implementacyjnych).
4. Jeśli którejś sekcji nie da się uzupełnić na podstawie PRD:
   - zostaw krótką notatkę `TODO` z opisem brakującej informacji.
5. Decyzje techniczne wpisuj wyłącznie do sekcji `## Decyzje techniczne`
   i tylko jeśli wynikają bezpośrednio z PRD.

CZĘŚĆ 2 — Roadmapa
6. Wypełnij istniejący plik `ROADMAP.md`, zachowując jego strukturę.
7. Nie zmieniaj nazw sekcji ani dozwolonych statusów milestone’ów.
8. Zachowaj Milestone 0.5 jako pierwszy element roadmapy.
9. Dodaj kolejne milestone’y po Milestone 0.5.
10. Każdy milestone musi zawierać:
    - Cel
    - Definition of Done
    - Zakres

Zasady:
- Nie zmieniaj struktury `spec.md` ani `ROADMAP.md`.
- Nie zmieniaj kodu.
- Jeśli coś jest niejednoznaczne, użyj `TODO` zamiast zgadywania.
```
  
Po tej czynności sprawdzamy pliki `spec.md` i `ROADMAP.md`. Jeśli coś trzeba poprawić zróbmy to, ale przez `Codex`, niech sam poprawi.  
  
## 4. Implemetacja Milestone 0.5 

Sprawdzamy czy w `ROADMAP.md` znajduje się Milestone 0.5 jeśli tak implementujemy go `/prompts:implement-milestone-0-5`:  
```
Zaimplementuj Milestone 0.5 dokładnie zgodnie z `ROADMAP.md`.

Zasady:
- minimalna ilość kodu
- brak optymalizacji
- brak refactorów niezwiązanych z milestone’em
- jeśli coś jest niejasne:
  - podejmij najprostszą decyzję
  - opisz ją w `spec.md` w sekcji `## Decyzje techniczne`

Po zakończeniu:
- upewnij się, że aplikacja się uruchamia
- uruchom testy
- zrób commit z czytelnym opisem
```
Po implementacji i sprawdzeniu czy działa czyli testy / ręczne uruchomienie i zatwierdzamy zmiany `/prompts:finalize-and-push-change`:  
```
Zmiana działa poprawnie.

1. Zaktualizuj `ROADMAP.md`:
   - oznacz wykonany milestone jako `done`

2. Zaktualizuj `STATUS.md`:
   - co działa
   - co jest skończone
   - co jest następne
   - (jeśli istnieją) blokery

3. Jeśli pojawiły się nowe decyzje:
   - zaktualizuj `spec.md` (`## Decyzje techniczne`)

Zasady:
- Nie zmieniaj kodu.
- Zrób commit i push.
- Jeśli push nie jest możliwy, opisz dokładnie co należy wykonać ręcznie.
```
To będzie nasza baza na której będziemy pracować, takie nasze „Hello World” dla obecnego projektu.  
  
## 5. Praca z kolejnymi Milestone’ami  
Każdy kolejny milestone wyzwalamy przez `/prompts:implement-milestone`:  
```
Zaimplementuj kolejny milestone ze `ROADMAP.md`: Milestone <numer>.

Zasady:
- realizuj wyłącznie zakres danego milestone’u
- nie zmieniaj architektury bez wyraźnej potrzeby
- jeśli zakres jest niejasny:
  - najpierw doprecyzuj `ROADMAP.md` lub `spec.md`
  - dopiero potem implementuj

Po zakończeniu:
- uruchom testy
- zrób commit z czytelnym opisem
```
I zatwierdzamy zmiany identycznie jak w przypadku Milestone 0.5 (==PO SPRAWDZENIU CZY DZIAŁA!==)  
  
## 6. Kończenie pracy w obrębie danego kontekstu  
Kończymy pracę z danym kontekstem w momencie ukończenia danego milestone/po ukończeniu serii milestone’ów z danego PRD.  
  
Używamy promptu `/prompts:project-wrap-up`:  
```
Zrób porządek w projekcie:

1. Upewnij się, że `AGENTS.md` jest aktualne (tylko zasady pracy).
2. Zaktualizuj `ROADMAP.md`:
   - statusy milestone’ów zgodnie z rzeczywistością
3. Zaktualizuj `STATUS.md`:
   - aktualny stan projektu
4. Upewnij się, że wszystko jest commitowane.

Zasady:
- Nie zmieniaj kodu.
```
  
## 7. Rozpoczęcie nowego kontekstu - np. Gdy mamy nowy PRD  
Nowy kontekst rozpoczynamy promptem sprawdzającym czy Codex wie w jakim jest miejscu i co to za projekt `/prompts:continue-project`:  
```
To jest kontynuacja istniejącego projektu.

Kontekst:
- przeczytaj `spec.md`
- przeczytaj `ROADMAP.md`
- przeczytaj `STATUS.md`
- przeczytaj `AGENTS.md`
- zapoznaj się z aktualnym stanem repozytorium

Zasady:
- nie reinterpretuj wcześniejszych decyzji
- nie zmieniaj architektury bez wyraźnej prośby
- trzymaj się roadmapy

Po przeczytaniu:
- krótko streść projekt
- wskaż aktualny milestone do realizacji
- nic nie implementuj
```
Jeśli daliśmy nowy PRD, to aktualizujemy `spec.md `i `ROADMAP.md` promptem `/prompts:next-prd`  
```
Na podstawie nowej funkcjonalności opisanej w pliku `PRD.md`:

CZĘŚĆ 1 — Aktualizacja specyfikacji
1. Zaktualizuj istniejący plik `spec.md`, korzystając z jego OBECNEJ struktury.
2. Nie zmieniaj nagłówków, nazw sekcji ani kolejności w `spec.md`.
3. Dodaj lub rozszerz treść tylko w sekcjach, których dotyczy nowe PRD.
4. Nie usuwaj ani nie reinterpretuj wcześniejszych decyzji.
5. Jeśli nowa funkcjonalność wymaga nowych decyzji technicznych:
   - dodaj je do sekcji `## Decyzje techniczne`
   - jasno zaznacz, że dotyczą nowej funkcjonalności.

CZĘŚĆ 2 — Aktualizacja roadmapy
6. Zaktualizuj istniejący plik `ROADMAP.md`.
7. Nie zmieniaj treści ani statusów istniejących milestone’ów.
8. Dodaj nowe milestone’y wynikające z PRD:
   - na końcu roadmapy
   - z nowymi numerami
9. Każdy nowy milestone musi zawierać:
   - Cel
   - Definition of Done
   - Zakres
10. Nowe milestone’y muszą być:
    - spójne z istniejącą specyfikacją
    - możliwe do realizacji iteracyjnie

Zasady ogólne:
- Nie zmieniaj struktury `spec.md` ani `ROADMAP.md`.
- Nie zmieniaj kodu.
- Jeśli nowe PRD jest w konflikcie z istniejącą specyfikacją:
  - opisz konflikt w `spec.md` (sekcja `## Decyzje techniczne`)
  - nie rozwiązuj go samodzielnie.
```
Po tym zabiegu, powtarzamy standardowe kroki z implementacją poszczególnych milestone’ów.  

