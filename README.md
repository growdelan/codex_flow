# Codex Flow

## Konfiguracja Codex
[Ściąga w postaci diagramu](diagram.md)

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
 
Uruchamiamy Codex i wykonujemy prompt `/prompts:start-new-project`
Z tak przygotowanym repozytorium jesteśmy gotowi do pracy.  
  
## 3. Rozpoczęcie projektu  
W Repozytorium tworzymy katalog i plik `prd/000-initial-prd.md` z naszym PRD utworzonym przez `GPT` i zapisujemy w katalogu głównym.  
  
Następnie w Codex uruchamiamy prompt `/prompts:generate-spec-from-prd`
  
Po tej czynności sprawdzamy pliki `spec.md` i `ROADMAP.md`. Jeśli coś trzeba poprawić zróbmy to, ale przez `Codex`, niech sam poprawi.  
  
## 4. Implemetacja Milestone 0.5 
Sprawdzamy czy w `ROADMAP.md` znajduje się Milestone 0.5 jeśli tak implementujemy go `/prompts:implement-milestone-0-5`:  

Po implementacji i sprawdzeniu czy działa czyli testy / ręczne uruchomienie i zatwierdzamy zmiany `/prompts:finalize-and-push-change` 

To będzie nasza baza na której będziemy pracować, takie nasze „Hello World” dla obecnego projektu.  
  
## 5. Praca z kolejnymi Milestone’ami  
Każdy kolejny milestone wyzwalamy przez `/prompts:implement-milestone` 

I zatwierdzamy zmiany identycznie jak w przypadku Milestone 0.5 (==PO SPRAWDZENIU CZY DZIAŁA!==)  
  
## 6. Kończenie pracy w obrębie danego kontekstu  
Gdy zdecydujemy się zakończyć pracę.  
  
Używamy promptu `/prompts:project-wrap-up`
  
## 7. Rozpoczęcie nowego kontekstu - np. Gdy mamy nowy PRD  
Nowy kontekst rozpoczynamy promptem sprawdzającym czy Codex wie w jakim jest miejscu i co to za projekt `/prompts:continue-project` 

Jeśli daliśmy nowy PRD, to aktualizujemy `spec.md `i `ROADMAP.md` promptem `/prompts:next-prd`  

Po tym zabiegu, powtarzamy standardowe kroki z implementacją poszczególnych milestone’ów.  

