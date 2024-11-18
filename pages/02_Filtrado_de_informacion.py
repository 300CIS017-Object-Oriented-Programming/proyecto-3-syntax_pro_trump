import streamlit as st
import pandas as pd
import plotly.express as px



def filtrado_de_info(sistema):
    # Sección 1: Filtrado de Información
    st.subheader("Filtrado de programas por palabras clave")
    keyword = st.text_input("Buscar programas por palabras clave")

    #Se pasa el valor keyword a la funcion que va a buscar los programas que se estan buscando.

    # Sección 2: Parámetros de Análisis
    st.subheader("Parámetros de análisis")
    years = st.slider("Seleccione el rango de años", min_value=2020, max_value=2023, value=(2021, 2023))
    if st.button("Realizar análisis"):
        sistema.procesar_datos(years[0], years[1], keyword)


    # Se le pasa years[0] y years[1] a la funcion para buscar los anios respectivos.

filtrado_de_info(st.session_state.sistema)