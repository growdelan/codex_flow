# Codex Flow

## 1. PRD w GPT  
  
Poprosić o PRD do nowego projektu za pomocą promptu podmieniająć `[nazwa lub krótki opis produktu/usługi]` na własny opis:  
```
Jesteś ekspertem w tworzeniu dokumentów PRD (Product Requirements Document) dla aplikacji.

Chciałbym stworzyć PRD dla **[nazwa lub krótki opis produktu/usługi]**. 

Przeprowadź ze mną wywiad – zadawaj mi pytania jedno po drugim, aż poznasz cały potrzebny kontekst do stworzenia dokumentu dla mojej aplikacji. 

Gdy będziesz miał wystarczający kontekst, przejdź do utworzenia dokumentu w formacie markdown.
```
Na koniec poprosić aby podsumował cała aplikację tylko jednym zdaniem. (Przyda się za chwile)  
  
## 2. Utworzenie repozytorium projektu  
* Tworzymy czyste repozytorium tylko z `README.md` i pobieramy na dysk.  
* Po pobraniu edytujemy plik `README.md` i wklejamy do niego to pojedyncze zdanie na temat naszej aplikacji, które wygenerował `GPT`, i zapisujemy.
* Kopiujemy do środka zawartość tego repozytorium `codex_flow` z pominięciem `README.md`, `.gitignore` i `.git` 

Uruchamiamy Codex.
Z tak przygotowanym repozytorium jesteśmy gotowi do pracy.  
  
## 3. Rozpoczęcie projektu  
W Repozytorium wypełniamy plik `prd/000-initial-prd.md` z naszym PRD utworzonym przez `GPT` i zapisujemy.  
  
Następnie w Codex uruchamiamy skill `$codex-flow-generate-spec-from-prd`
  
Po tej czynności sprawdzamy pliki `spec.md` i `ROADMAP.md`. Jeśli coś trzeba poprawić zróbmy to, ale przez `Codex`, niech sam poprawi.  
  
## 4. Implemetacja Milestone 0.5 
Sprawdzamy czy w `ROADMAP.md` znajduje się Milestone 0.5 jeśli tak implementujemy go `$codex-flow-implement-milestone-0-5`:  

Po implementacji i sprawdzeniu czy działa czyli testy / ręczne uruchomienie i zatwierdzamy zmiany `$codex-flow-finalize-and-push-change` 

To będzie nasza baza na której będziemy pracować, takie nasze „Hello World” dla obecnego projektu.  
  
## 5. Praca z kolejnymi Milestone’ami  
Każdy kolejny milestone wyzwalamy przez `$codex-flow-implement-milestone` 

**Opcjonalnie**

Uruchamiamy:
- `$codex-flow-self-review` - jeśli chcemy sprawdzić czy są niespójności i złamanie zasad.
- `$codex-flow-apply-self-review-fixes` - jeśli wyszły jakieś niesójności/żlamanie zasad.

I zatwierdzamy zmiany identycznie jak w przypadku Milestone 0.5 (==PO SPRAWDZENIU CZY DZIAŁA!==) `$codex-flow-finalize-and-push-change`  
  
## 6. Kończenie pracy w obrębie danego kontekstu  
Gdy zdecydujemy się zakończyć pracę.  
  
Używamy skilla `$codex-flow-project-wrap-up`
  
## 7. Rozpoczęcie nowego kontekstu - np. Gdy mamy nowy PRD  
Nowy kontekst rozpoczynamy skillem sprawdzającym czy Codex wie w jakim jest miejscu i co to za projekt `$codex-flow-continue-project` 

Jeśli daliśmy nowy PRD, to aktualizujemy `spec.md `i `ROADMAP.md` skillem `$codex-flow-next-prd`  

Po tym zabiegu, powtarzamy standardowe kroki z implementacją poszczególnych milestone’ów.  
