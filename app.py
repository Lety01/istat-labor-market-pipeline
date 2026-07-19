import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import streamlit as st

# 1. Configurazione della pagina Web
st.set_page_config(
    page_title="Dashboard Analisi Studenti & Lavoro - ISTAT",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Analisi Transizione Studio-Lavoro in Italia")
st.markdown(
    "Questo cruscotto interattivo analizza la condizione lavorativa e lo status degli studenti nel territorio italiano basandosi sui dati ufficiali **ISTAT**."
)
st.divider()


# 2. Funzione per caricare i dati dal Database SQLite (con cache per la massima velocità)
@st.cache_data
def carica_dati():
    engine = create_engine("sqlite:///istat_data.db")
    df = pd.read_sql("SELECT * FROM status_studente_istat", engine)
    return df


df = carica_dati()

# 3. Barra Laterale (Sidebar) con i Filtri Interattivi
st.sidebar.header("🔍 Filtra i Dati")

# Filtro Anno (Slider)
anno_min, anno_max = int(df["anno"].min()), int(df["anno"].max())
anni_selezionati = st.sidebar.slider(
    "Seleziona Periodo Storicizzato:",
    min_value=anno_min,
    max_value=anno_max,
    value=(anno_min, anno_max),
)

# Filtro Territorio
territori_disponibili = df["territorio"].unique()
territorio_selezionato = st.sidebar.multiselect(
    "Seleziona Territorio/Regione:",
    options=territori_disponibili,
    default=["Italia"]
    if "Italia" in territori_disponibili
    else territori_disponibili[:1],
)

# Filtro Sesso
sesso_selezionato = st.sidebar.radio(
    "Seleziona Sesso:", options=df["sesso"].unique(), horizontal=True
)

# 4. Applicazione dei filtri al DataFrame
df_filtrato = df[
    (df["anno"] >= anni_selezionati[0])
    & (df["anno"] <= anni_selezionati[1])
    & (df["territorio"].isin(territorio_selezionato))
    & (df["sesso"] == sesso_selezionato)
]

# 5. Sezione KPI Principali
col1, col2, col3 = st.columns(3)
totale_osservazioni = df_filtrato["valore_migliaia"].sum()
anno_piu_recente = df_filtrato["anno"].max()

with col1:
    st.metric(
        label="Totale Popolazione Analizzata (in migliaia)",
        value=f"{totale_osservazioni:,.0f}",
    )
with col2:
    st.metric(label="Anno più recente analizzato", value=f"{anno_piu_recente}")
with col3:
    st.metric(label="Fasce d'età monitorate", value=len(df["fascia_eta"].unique()))

st.divider()

# 6. Creazione del Grafico Interattivo con Plotly
st.subheader("📈 Andamento Temporale per Condizione Lavorativa")

# Raggruppiamo i dati per anno e condizione lavorativa
df_grafico = (
    df_filtrato.groupby(["anno", "condizione_lavorativa"])["valore_migliaia"]
    .sum()
    .reset_index()
)

fig = px.line(
    df_grafico,
    x="anno",
    y="valore_migliaia",
    color="condizione_lavorativa",
    markers=True,
    labels={
        "anno": "Anno",
        "valore_migliaia": "Valore (in migliaia)",
        "condizione_lavorativa": "Condizione Lavorativa",
    },
    template="plotly_white",
)

# Mostriamo il grafico nella pagina
st.plotly_chart(fig, use_container_width=True)

# 7. Tabella dati grezzi (opzionale, a comparsa)
with st.expander("📄 Visualizza i Dati Tabellari Filtrati"):
    st.dataframe(df_filtrato, use_container_width=True)