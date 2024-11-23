import streamlit as st
import pandas as pd
import plotly.express as px

# Simular datos como ejemplo
df_original = pd.DataFrame({
    "CÓDIGO SNIES": [101, 102, 103, 101, 102, 103],
    "PROGRAMA ACADÉMICO": ["Ingeniería", "Medicina", "Ingeniería", "Ingeniería", "Medicina", "Ingeniería"],
    "AÑO": [2020, 2020, 2020, 2021, 2021, 2021],
    "ADMITIDOS": [150, 100, 180, 200, 120, 210],
    "GRADUADOS": [50, 30, 60, 70, 40, 80]
})

# Selección de métrica (Admitidos, Graduados, etc.)
keyword = st.selectbox("Seleccione la métrica para analizar:", options=["ADMITIDOS", "GRADUADOS"])

if keyword:
    # Crear identificadores únicos para cada programa académico basado en CÓDIGO SNIES
    df_original["IDENTIFICADOR"] = df_original["PROGRAMA ACADÉMICO"] + " (SNIES: " + df_original["CÓDIGO SNIES"].astype(str) + ")"

    # Selección de programas académicos
    programas = df_original["IDENTIFICADOR"].unique()
    programas_seleccionados = st.multiselect(
        "Seleccione los programas académicos que desea comparar:",
        options=programas,
        default=programas
    )

    # Filtrar el DataFrame según la selección del usuario
    if programas_seleccionados:
        df_filtered = df_original[df_original["IDENTIFICADOR"].isin(programas_seleccionados)]

        # Crear el gráfico de barras
        fig = px.bar(
            df_filtered,
            x="AÑO",
            y=keyword,
            color="IDENTIFICADOR",
            barmode="group",  # Agrupar barras por programa académico
            labels={
                "AÑO": "Año",
                keyword: f"Número de {keyword}",
                "IDENTIFICADOR": "Programa Académico"
            },
            title=f"Comparación de {keyword} entre Programas Académicos"
        )

        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Seleccione al menos un programa académico para visualizar el gráfico.")
else:
    st.warning("Seleccione una métrica para continuar.")
