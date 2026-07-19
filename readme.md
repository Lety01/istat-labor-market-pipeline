📊 Transizione Studio-Lavoro in Italia: Full-Stack Data Pipeline & BI Dashboard 

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-thebadge&logo=python&logoColor=white) 

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-thebadge&logo=streamlit&logoColor=white) 

![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-thebadge&logo=sqlite&logoColor=white) 

![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the- 

badge&logo=plotly&logoColor=white) 

![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-thebadge&logo=pandas&logoColor=white) 

Un progetto end-to-end di  Data Engineering e Business Intelligence  che analizza il capitale umano e la transizione studio-lavoro in Italia utilizzando i dati ufficiali dell' ISTAT . 

Il sistema dimostra l'implementazione di una pipeline  ETL (Extract, Transform, Load) automatizzata per la pulizia di serie storiche complesse e la contestuale creazione di un cruscotto esecutivo interattivo per il supporto alle decisioni strategiche. 

--- 

🎯 Obiettivo del Progetto e Valore per il Business 

L'analisi del mercato del lavoro giovanile e della popolazione studentesca presenta spesso problematiche legate alla frammentazione dei dati e al rumore statistico. Questo progetto risolve la sfida architetturale trasformando archivi di dati grezzi in un sistema decisionale interattivo. 

Il cruscotto è progettato per rispondere alle seguenti domande strategiche: 

*  Analisi dei Trend:  Come evolve il tasso di inattività e di occupazione degli studenti nelle diverse fasce d'età? 

*  Divario Territoriale:  Quali sono le differenze strutturali tra le varie regioni italiane nella transizione verso il mercato del lavoro? 

*  Supporto alle Decisioni:  Quali segmenti demografici richiedono maggiori investimenti in formazione o incentivi all'occupazione? 

--- 

Architettura della Pipeline e Stack Tecnologico 🏗️� 

Il sistema è suddiviso in due livelli principali: il *Data Processing Layer* (pipeline di backend) e il *Presentation Layer* (interfaccia frontend). 

| Fase | Tecnologia | Descrizione del Ruolo | 

| :--- | :--- | :--- | 

|  Extract & Transform  | `Pandas` / `Python` | Acquisizione file CSV grezzi, normalizzazione dei tipi, filtraggio delle colonne ridondanti e standardizzazione della nomenclatura. | 

|  Load (Persistenza)  | `SQLAlchemy` / `SQLite` | Caricamento ottimizzato dei dati puliti all'interno di un database relazionale locale, garantendo integrità e accessibilità via SQL. | 

|  Business Intelligence  | `Streamlit` / `Plotly` | Interfaccia web interattiva con filtraggio dinamico (per anno, territorio e sesso), calcolo di KPI in tempo reale e visualizzazioni grafiche avanzate. | 

--- 

🎯 Struttura del Repository 

```text 

├── .gitignore                 Esclusione di ambienti virtuali, cache e file temporanei 

├── app.py                     Frontend: Dashboard web interattiva sviluppata in Streamlit 

├── pipeline.py                Backend: Script ETL automatizzato (Transform -> Load -> Test SQL) 

├── requirements.txt           Elenco delle dipendenze per la riproducibilità dell'ambiente 

└── README.md                  Documentazione architetturale e descrizione del progetto (questo file) 

# **🚀 Guida all'Avvio Rapido (Local Setup)** 

Per riprodurre il progetto sul proprio ambiente locale, seguire i passaggi sottostanti. 

# **1. Clona il repository e crea l'ambiente virtuale** 

Bash 

git clone [https://github.com/tuo-username/istat-labor-market-pipeline.git](https:// github.com/tuo-username/istat-labor-market-pipeline.git) 

cd istat-labor-market-pipeline 

python -m venv .venv 

Attivazione dell'ambiente virtuale: 

Bash 

Su Windows: 

.\.venv\Scripts\activate 

Su macOS/Linux: 

source .venv/bin/activate 

# **2. Installa le dipendenze** 

Bash 

pip install -r requirements.txt 

# **3. Esegui la Pipeline ETL** 

Avvia lo script di backend per processare il dataset grezzo, generare la pulizia e istanziare il database relazionale locale (istat_data.db): 

Bash 

python pipeline.py 

_L'elaborazione produrrà un log a terminale che conferma la creazione della tabella SQL e il numero di record caricati correttamente (es. 22.044 righe)._ 

# **4. Avvia la Dashboard Interattiva** 

Lancia il server locale per esplorare il cruscotto di Business Intelligence: 

# Bash 

python -m streamlit run app.py 

Apri il browser all'indirizzo http://localhost:8501 per interagire con l'interfaccia. 

# **🚀 Metodologia ETL: Dettaglio Tecnico** 

La logica del codice nello script pipeline.py segue un approccio rigoroso volto alla qualità e alla governance del dato: 

1. **Selezione selettiva delle feature:** Riduzione del rumore statistico scartando codici interni ISTAT vuoti o ridondanti (es. OBS_STATUS, codici alfanumerici territoriali non necessari all'analisi informativa). 

2. **Standardizzazione dello Schema:** Ridenominazione strategica delle colonne in formato _snake_case_ (fascia_eta, condizione_lavorativa) per facilitare la scrittura di query SQL chiare, performanti e conformi agli standard di produzione. 

3. **Idempotenza:** La fase di caricamento implementa la logica di sovrascrittura controllata (if_exists='replace') su SQLite, garantendo che lo script possa essere eseguito più volte in modo deterministico senza rischiare la duplicazione o la corruzione dei record nel database. 

# **🚀 Sviluppi Futuri (Roadmap)** 

- **Migrazione Cloud DB:** Sostituzione di SQLite con un'istanza distribuita **PostgreSQL** su cloud (es. Supabase o AWS RDS) per supportare carichi di lavoro multi-utente e logiche di accesso concorrente. 

- **Orchestrazione dei Flussi:** Integrazione con strumenti di workflow management (es. 

- **Apache Airflow** o Prefect) per programmare e automatizzare l'estrazione incrementale di nuovi dati rilasciati dai server ISTAT. 

- **Analisi Predittiva:** Sviluppo di un modulo di machine learning (tramite Scikit-Learn) integrato nella dashboard per prevedere i trend del tasso di occupazione giovanile e studentesca sul medio periodo. 

