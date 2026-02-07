```mermaid
flowchart TD

  A[PRD w GPT] --> B[Repo plus README jedno zdanie]
  B --> C[Codex start-new-project tworzy spec roadmap status]
  C --> D[Dodaj prd 000-initial-prd.md]
  D --> E[Codex generate-spec-from-prd]

  E --> F[Implement Milestone 0.5]
  F --> G{Czy dziala}
  G -- nie --> F
  G -- tak --> H[Finalize update docs commit push]

  H --> I[Implement kolejny milestone]
  I --> J{Czy dziala}
  J -- nie --> I
  J -- tak --> K[Finalize update docs commit push]

  K --> I

  K --> L{Czy zakonczono caly PRD}
  L -- nie --> I
  L -- tak --> M[Project wrap up aktualizacja roadmap status]

  M --> N{Nowy PRD}
  N -- nie --> Z[Koniec pracy]
  N -- tak --> O[Dodaj nowy PRD.md]
  O --> P[Codex next-prd aktualizuje spec i roadmap]
  P --> I
```
