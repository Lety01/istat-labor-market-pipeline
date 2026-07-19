# 📊 Transizione Studio-Lavoro in Italia: Full-Stack Data Pipeline & BI Dashboard

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

Un progetto end-to-end di **Data Engineering e Business Intelligence** che analizza il capitale umano e la transizione studio-lavoro in Italia utilizzando i dati ufficiali dell'**ISTAT**. 

Il sistema dimostra l'implementazione di una pipeline **ETL (Extract, Transform, Load)** automatizzata per la pulizia di serie storiche complesse e la contestuale creazione di un cruscotto esecutivo interattivo per il supporto alle decisioni strategiche.

---

## 🎯 Obiettivo del Progetto e Valore per il Business

L'analisi del mercato del lavoro giovanile e della popolazione studentesca presenta spesso problematiche legate alla frammentazione dei dati e al rumore statistico. Questo progetto risolve la sfida architetturale trasformando archivi di dati grezzi in un sistema decisionale interattivo.

Il cruscotto è progettato per rispondere alle seguenti domande strategiche:
* **Analisi dei Trend:** Come evolve il tasso di inattività e di occupazione degli studenti nelle diverse fasce d'età?
* **Divario Territoriale:** Quali sono le differenze strutturali tra le varie regioni italiane nella transizione verso il mercato del lavoro?
* **Supporto alle Decisioni:** Quali segmenti demografici richiedono maggiori investimenti in formazione o incentivi all'occupazione?

---

## 🏗️ Architettura della Pipeline e Stack Tecnologico

Il sistema è suddiviso in due livelli principali: il *Data Processing Layer* (pipeline di backend) e il *Presentation Layer* (interfaccia frontend).

| Fase | Tecnologia | Descrizione del Ruolo |
| :--- | :--- | :--- |
| **Extract & Transform** | `Pandas` / `Python` | Acquisizione file CSV grezzi, normalizzazione dei tipi, filtraggio delle colonne ridondanti e standardizzazione della nomenclatura. |
| **Load (Persistenza)** | `SQLAlchemy` / `SQLite` | Caricamento ottimizzato dei dati puliti all'interno di un database relazionale locale, garantendo integrità e accessibilità via SQL. |
| **Business Intelligence** | `Streamlit` / `Plotly` | Interfaccia web interattiva con filtraggio dinamico (per anno, territorio e sesso), calcolo di KPI in tempo reale e visualizzazioni grafiche avanzate. |

---

## 📁 Struttura del Repository

```text
├── .gitignore               # Esclusione di ambienti virtuali, cache e file temporanei
├── app.py                   # Frontend: Dashboard web interattiva sviluppata in Streamlit
├── dati_grezzi_istat.csv    # Dataset grezzo ufficiale scaricato dal portale ISTAT (Input)
├── dati_puliti_istat.csv    # Dataset normalizzato e pulito dallo script (Output fase Transform)
├── pipeline.py              # Backend: Script ETL automatizzato (Transform -> Load -> Test SQL)
├── requirements.txt         # Elenco delle dipendenze per la riproducibilità dell'ambiente
└── README.md                # Documentazione architetturale e descrizione del progetto (questo file)

```

### ⚙️ Guida all'Installazione e Configurazione Locale

Il progetto è progettato per essere **100% riproducibile** su qualsiasi ambiente locale (Windows, macOS o Linux) isolando le dipendenze tramite un ambiente virtuale Python.

### 1. Prerequisiti del Sistema
* **Python** (versione 3.10 o superiore raccomandata)
* **Git** installato e configurato nel terminale

---

### 2. Clona il Repository e Naviga nella Cartella
Apri il terminale ed esegui i seguenti comandi per scaricare una copia locale del progetto:
```bash
git clone [https://github.com/tuo-username/istat-labor-market-pipeline.git](https://github.com/tuo-username/istat-labor-market-pipeline.git)
cd istat-labor-market-pipeline

```

### 3. Creazione e Attivazione dell'Ambiente Virtuale

Per evitare conflitti con i pacchetti di sistema, crea un ambiente virtuale isolato (`.venv`):

**Creazione dell'ambiente:**

Bash

```
python -m venv .venv

```

**Attivazione dell'ambiente:**

-   **Su Windows (PowerShell):**
    
    PowerShell
    
    ```
    .\.venv\Scripts\activate
    
    ```
    
-   **Su macOS / Linux:**
    
    Bash
    
    ```
    source .venv/bin/activate
    
    ```
    

### 4. Installazione delle Dipendenze

Una volta attivato l'ambiente virtuale (vedrai `(.venv)` all'inizio della riga del terminale), installa le librerie necessarie (`pandas`, `streamlit`, `plotly`, `sqlalchemy`):

Bash

```
pip install --upgrade pip
pip install -r requirements.txt

```

### 5. Esecuzione della Pipeline ETL (Backend)

Prima di lanciare l'interfaccia grafica, è necessario processare il dataset grezzo (`dati_grezzi_istat.csv`). Lo script di backend eseguirà la pulizia, la normalizzazione e genererà sia il file `dati_puliti_istat.csv` che il database relazionale `istat_data.db`:

Bash

```
python pipeline.py

```

_💡 **Nota tecnica:** Lo script è **idempotente**; può essere lanciato più volte in sicurezza senza rischiare di duplicare o corrompere i record nel database locale._

### 6. Avvio della Dashboard di BI (Frontend)

Una volta generato il database, avvia il server locale di Streamlit per esplorare il cruscotto interattivo di Business Intelligence:

Bash

```
python -m streamlit run app.py

```

Appena premuto _Invio_, il browser si aprirà automaticamente all'indirizzo **`http://localhost:8501`**, mostrando i filtri dinamici e i grafici interattivi.




## 🔮 Roadmap e Implementazioni Future

Questo progetto pone le basi per un'infrastruttura dati scalabile. Le evoluzioni pianificate per i prossimi rilasci mirano a trasformare la pipeline locale in un software di livello **production-ready**:

### 1. Dockerizzazione dell'Architettura (Containerization)

-   **Obiettivo:** Rimuovere completamente la necessità di configurare manualmente gli ambienti virtuali.
    
-   **Implementazione:** Creazione di un `Dockerfile` per la dashboard e un file `docker-compose.yml` per orchestrare l'avvio simultaneo del container ETL e dell'applicazione web con un singolo comando (`docker compose up`).
    

### 2. Migrazione a Database Relazionale Cloud (PostgreSQL)

-   **Obiettivo:** Superare i limiti di concorrenza del file locale SQLite e consentire l'accesso multi-utente.
    
-   **Implementazione:** Sostituzione del motore SQLite con un'istanza cloud **PostgreSQL** (es. su _Supabase_, _AWS RDS_ o _Google Cloud SQL_), integrando un sistema di gestione sicura delle credenziali tramite variabili d'ambiente (`.env`).
    

### 3. Orchestrazione e Automazione del Flusso Dati

-   **Obiettivo:** Automatizzare il monitoraggio e l'estrazione periodica dei dati dal portale ISTAT senza intervento manuale.
    
-   **Implementazione:** Configurazione di un workflow **GitHub Actions** (o integrazione con **Apache Airflow**) schedulato con un _Cron Job_ per scaricare automaticamente i nuovi rilasci statistici, eseguire i test di integrità e aggiornare il database in produzione.
    

### 4. Integrazione di Modelli di Machine Learning e Analisi Predittiva

-   **Obiettivo:** Passare da un'analisi prettamente _descrittiva_ a un supporto decisionale _predittivo_.
    
-   **Implementazione:** Sviluppo di un modulo analitico con **Scikit-Learn** per eseguire una regressione sulle serie storiche, prevedendo l'andamento del tasso di occupazione studentesca per i successivi 3-5 anni e integrando il forecast visivamente nei grafici Plotly della dashboard.
    

### 5. CI/CD e Data Quality Testing

-   **Obiettivo:** Garantire che dati incompleti o formattati erroneamente non arrivino mai nell'interfaccia utente.
    
-   **Implementazione:** Introduzione della libreria **Pytest** e di framework di validazione come **Great Expectations** per verificare automaticamente la conformità dello schema, l'assenza di valori nulli critici e il rispetto dei vincoli di dominio prima della fase di _Load_.
    



