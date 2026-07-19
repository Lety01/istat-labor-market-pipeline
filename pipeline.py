import os
import pandas as pd
from sqlalchemy import create_engine


def avvia_fase_transform(nome_file_csv="dati_grezzi_istat.csv"):
    print("⏳ 1. Avvio della fase TRANSFORM (Pulizia dati)...")
    df = pd.read_csv(nome_file_csv)

    colonne_da_tenere = [
        "Territorio",
        "Sesso",
        "Età",
        "Condizione lavorativa europea",
        "Studente",
        "TIME_PERIOD",
        "Osservazione",
    ]
    df_pulito = df[colonne_da_tenere].copy()

    df_pulito.rename(
        columns={
            "Territorio": "territorio",
            "Sesso": "sesso",
            "Età": "fascia_eta",
            "Condizione lavorativa europea": "condizione_lavorativa",
            "Studente": "status_studente",
            "TIME_PERIOD": "anno",
            "Osservazione": "valore_migliaia",
        },
        inplace=True,
    )

    df_pulito.to_csv("dati_puliti_istat.csv", index=False)
    print("✅ Dati puliti e salvati nel file CSV!")
    return df_pulito


def avvia_fase_load(nome_file_pulito="dati_puliti_istat.csv"):
    print("\n⏳ 2. Avvio della fase LOAD (Caricamento nel Database SQLite)...")

    # Crea automaticamente un file database locale chiamato 'istat_data.db'
    engine = create_engine("sqlite:///istat_data.db")

    # Legge il file CSV pulito
    df = pd.read_csv(nome_file_pulito)

    # Carica i dati in una tabella SQL chiamata 'status_studente_istat'
    df.to_sql("status_studente_istat", engine, if_exists="replace", index=False)
    print("✅ Caricamento completato! È stato creato il database 'istat_data.db'.")


def test_query_database():
    print("\n⏳ 3. Test di verifica: interroghiamo il database con SQL...")
    engine = create_engine("sqlite:///istat_data.db")

    # Facciamo una query SQL per contare le righe nel database
    query = "SELECT COUNT(*) AS totale_righe FROM status_studente_istat;"
    risultato = pd.read_sql(query, engine)

    print(
        f"📊 RISULTATO QUERY: Il database contiene esattamente {risultato['totale_righe'][0]} righe!"
    )
    print("🎉 La tua pipeline ETL è ufficialmente completata e funzionante!")


# Questo blocco avvia l'intera sequenza quando premi Invio nel terminale
if __name__ == "__main__":
    avvia_fase_transform()
    avvia_fase_load()
    test_query_database()