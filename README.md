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
* Tworzymy czyste repozytorium tylko z `README.md `i pobieramy na dysk.  
* Po pobraniu edytujemy plik `README.md` i wklejamy do niego to pojedyncze zdanie na temat naszej aplikacji które wygenerował `GPT` i zapisujemy.  
* Uruchamiamy `Codex` i inicjujemy komendą `/init`  co utworzy plik `AGENTS.md`  
  
Zostajemy w Codex i uruchamiamy prompt `/prompts:start-new-project`:  
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

`ROADMAP.md` ma zawierać:
# Roadmapa (milestones)

## Milestone <numer>: <nazwa> (<status>)
Cel:
Definition of Done:
Zakres:

Nie uzupełniaj treści merytorycznej.

`STATUS.md` ma zawierać:
# Aktualny stan
- co działa:
- co jest skończone:
- co jest następne:

Nie uzupełniaj treści merytorycznej.
Nie zmieniaj kodu.
```
Z tak przygotowanym repozytorium jesteśmy gotowi do pracy.  
  
## 3. Rozpoczęcie projektu  
W Repozytorium tworzymy plik `PRD.md` z naszym PRD utworzonym przez `GPT` i zapisujemy w katalogu głównym.  
  
Następnie w Codex uruchamiamy prompt `/prompts:generate-spec-from-prd`:  
```
Na podstawie pliku `PRD.md`:

1. Wypełnij treścią istniejący plik `spec.md`, korzystając z jego OBECNEJ struktury.
2. Nie zmieniaj nagłówków, nazw sekcji ani kolejności w `spec.md`.
3. Uzupełnij każdą sekcję na poziomie wysokim (bez detali implementacyjnych).
4. Jeśli którejś sekcji nie da się uzupełnić na podstawie PRD:
   - zostaw krótką notatkę `TODO` z opisem brakującej informacji.

Dodatkowo:
5. Zaproponuj roadmapę w formie jasno nazwanych milestone’ów.
6. Każdy milestone ma mieć:
   - cel
   - kryteria „Definition of Done”
   - krótki opis zakresu

Wynik zapisz do plików:
- `spec.md` — wypełniona specyfikacja wysokiego poziomu
- `ROADMAP.md` — roadmapa z milestone’ami

Zasady:
- Nie zmieniaj struktury `spec.md`.
- Nie zmieniaj kodu.
- Nie dodawaj zależności ani decyzji implementacyjnych bez wyraźnego uzasadnienia w `## Decyzje techniczne`.
```
  
Po tej czynności sprawdzamy pliki `spec.md` i `ROADMAP.md`. Jeśli coś trzeba poprawić zróbmy to, ale przez `Codex`, niech sam poprawi.  
  
## 4. Milestone 0.5  
Jeśli w `ROADMAP.md `Codex sam nie zaproponował milestone 0.5, robimy to za pomocą promptu `/prompts:create-milestone-05`:  
```
Dodaj do `ROADMAP.md` nowy milestone przed wszystkimi innymi:

Milestone 0.5 — Minimal end-to-end slice

Cel:
- aplikacja uruchamia się
- wykonuje jedno, bardzo proste zadanie
- zwraca poprawny wynik

Definition of Done:
- da się uruchomić jednym poleceniem
- istnieje jeden prosty test / smoke check
- brak placeholderów

Zapisz zmiany do `ROADMAP.md`.
```
Gdy jest gotowy implementujemy go `/prompts:implement-milestone-0-5`:  
```
Zaimplementuj Milestone 0.5 dokładnie zgodnie ze `ROADMAP.md`.

Zasady:
- minimalna ilość kodu
- brak optymalizacji
- jeśli coś jest niejasne, podejmij prostą decyzję i opisz ją w komentarzu

Po zakończeniu:
- upewnij się, że działa
- zrób commit z czytelnym opisem
```
Po implementacji i sprawdzeniu czy działa czyli testy / ręczne uruchomienie i zatwierdzamy zmiany `/prompts:finalize-and-push-change`:  
```
Zmiana działa poprawnie.

Zaktualizuj `ROADMAP.md`:
- oznacz wykonany milestone jako zrealizowany

Zaktualizuj `STATUS.md`:
- co działa
- co jest skończone
- co jest następne

Jeśli pojawiły się nowe decyzje/zmiany założeń:
- zaktualizuj `spec.md`

Nie zmieniaj kodu.
Zrób commit i push.
```
To będzie nasza baza na której będziemy pracować, takie nasze „Hello World” dla obecnego projektu.  
  
## 5. Praca z kolejnymi Milestone’ami  
Każdy kolejny milestone wyzwalamy przez `/prompts:implement-milestone`:  
```
Zaimplementuj kolejny milestone ze `ROADMAP.md`: Milestone <numer_milestone>
```
I zatwierdzamy zmiany identycznie jak w przypadku Milestone 0.5 (==PO SPRAWDZENIU CZY DZIAŁA!==)  
  
## 6. Kończenie pracy w obrębie danego kontekstu  
Kończymy pracę z danym kontekstem w momencie ukończenia danego milestone/po ukończeniu serii milestone’ów z danego PRD.  
  
Używamy promptu `/prompts:project-wrap-up`:  
```
Zrób porządek:
1. Upewnij się, że `AGENTS.md` jest aktualne (tylko zasady pracy).
2. Zaktualizuj `ROADMAP.md`:
   - oznacz statusy milestone’ów zgodnie ze stanem.
3. Zaktualizuj `STATUS.md`:
   - co działa
   - co jest skończone
   - co jest następne
4. Upewnij się, że wszystko jest commitowane.

Nie zmieniaj kodu.
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
- zapoznaj się z aktualnym stanem repo

Zasady:
- nie reinterpretuj wcześniejszych decyzji
- nie zmieniaj architektury bez wyraźnej prośby
- trzymaj się roadmapy

Po przeczytaniu:
- krótko streść projekt
- wymień aktualny milestone do realizacji
- nic nie implementuj
```
Jeśli daliśmy nowy PRD, to aktualizujemy `spec.md `i `ROADMAP.md` promptem `/prompts:next-prd`  
```
Na podstawie nowej funkcjonalności opisanej w pliku `PRD.md`:

- Zaktualizuj specyfikację aplikacji na wysokim poziomie w `spec.md`.
- Dodaj do roadmapy w `ROADMAP.md` nowe milestone’y wynikające z PRD.
- Każdy milestone ma mieć:
  - cel
  - kryteria „Definition of Done”
  - krótki opis zakresu

Nie zmieniaj kodu.
```
Po tym zabiegu, powtarzamy standardowe kroki z implementacją poszczególnych milestone’ów.  

