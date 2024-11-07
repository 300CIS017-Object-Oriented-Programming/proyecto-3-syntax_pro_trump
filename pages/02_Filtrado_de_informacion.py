import streamlit as st
import pandas as pd
import plotly.express as px

def filtrado_de_info():
    # Sección 1: Filtrado de Información
    st.subheader("Filtrado de Información")
    keyword = st.text_input("Buscar programas por palabras clave")

    # Datos ficticios para mostrar
    programs_df = pd.DataFrame({
        "Programa": ["Ingeniería", "Medicina", "Derecho", "Arquitectura"],
        "Universidad": ["Uni1", "Uni2", "Uni3", "Uni4"],
        "Año": [2021, 2022, 2021, 2022],
        "Matriculados": [100, 150, 200, 180]
    })

    # Aplicar filtrado si se ingresa una palabra clave
    if keyword:
        filtered_df = programs_df[programs_df["Programa"].str.contains(keyword, case=False)]
    else:
        filtered_df = programs_df

    # Mostrar la tabla filtrada
    st.table(filtered_df)

    # Sección 2: Parámetros de Análisis
    st.subheader("Parámetros de Análisis")
    years = st.slider("Seleccione el rango de años", min_value=2019, max_value=2023, value=(2021, 2023))
    selected_programs = st.multiselect("Programas seleccionados para análisis",
                                       options=filtered_df["Programa"].tolist())

    # Filtrar el DataFrame según los años seleccionados
    filtered_df = filtered_df[(filtered_df["Año"] >= years[0]) & (filtered_df["Año"] <= years[1])]

    # Filtrar el DataFrame según los programas seleccionados
    if selected_programs:
        filtered_df = filtered_df[filtered_df["Programa"].isin(selected_programs)]

    # Sección 3: Visualización de Datos
    st.subheader("Visualización de Datos")

    # Asegurarse de que hay datos para graficar
    if not filtered_df.empty:
        fig = px.bar(filtered_df, x="Año", y="Matriculados", color="Programa", barmode="group")
        fig.update_layout(
            xaxis=dict(
                dtick=1,  # Esto asegura que el eje X solo tendrá valores enteros, de 1 en 1
                tickmode="linear"  # Esto asegura que los ticks sean lineales y no fraccionados
            )
        )
        st.plotly_chart(fig)
    else:
        st.write("No hay datos para mostrar según los filtros aplicados.")
filtrado_de_info()