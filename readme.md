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
├── pipeline.py              # Backend: Script ETL automatizzato (Transform -> Load -> Test SQL)
├── requirements.txt         # Elenco delle dipendenze per la riproducibilità dell'ambiente
└── README.md                # Documentazione architetturale e descrizione del progetto (questo file)