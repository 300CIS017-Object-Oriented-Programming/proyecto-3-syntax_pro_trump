import streamlit as st
import pandas as pd
import plotly.express as px



def filtrado_de_info(controlador):
    # Sección 1: Filtrado de Información
    st.subheader("Filtrado de programas por palabras clave")
    keyword = st.text_input("Buscar programas por palabras clave")

    #Se pasa el valor keyword a la funcion que va a buscar los programas que se estan buscando.

    # Sección 2: Parámetros de Análisis
    st.subheader("Parámetros de análisis")
    years = st.slider("Seleccione el rango de años", min_value=2020, max_value=2023, value=(2021, 2023))
    if st.button("Realizar primera busqueda"):
        controlador.procesar_datos(years[0], years[1], keyword)




    df = controlador

    # Título de la aplicación
    st.title("Selección de Programas para Análisis")

    # Subtítulo
    st.subheader("Seleccione los programas que desea incluir en el análisis")

    # Crear lista para almacenar programas seleccionados
    selected_programs = []

    # Mostrar tabla con checkboxes para cada programa
    for index, row in df.iterrows():
        if st.checkbox(f"{row['Programa']} - {row['Universidad']} (Código SNIES: {row['Código SNIES']})", key=index):
            selected_programs.append(row.to_dict())

    # Mostrar los programas seleccionados
    if selected_programs:
        st.subheader("Programas Seleccionados")
        st.write(pd.DataFrame(selected_programs))

        # Botón para exportar la selección
        if st.button("Exportar Selección a Excel"):
            selected_df = pd.DataFrame(selected_programs)
            selected_df.to_excel("programas_seleccionados.xlsx", index=False)
            st.success("¡Archivo Excel generado con éxito!")


filtrado_de_info(st.session_state.controlador)