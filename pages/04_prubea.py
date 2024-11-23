import streamlit as st
import os
import plotly.express as px
import pandas as pd

def gestion_archivos2():
    # Sección 1: Carga de Archivos
    st.title("Gestion de archivos")
    st.subheader("Archivos disponibles")

    input_folder = 'docs/inputs'  # Asegúrate de que la carpeta existe

    # Inicializar una lista vacía para almacenar los archivos .xlsx
    default_files = []

    # Recorrer cada archivo en la carpeta
    for f in os.listdir(input_folder):
        # Comprobar si el archivo tiene la extensión .xlsx
        if f.endswith('.xlsx'):
            # Si es así, agregarlo a la lista default_files
            default_files.append(f)

    # Mostrar los archivos disponibles en un selectbox o multiselect
    st.title("Archivos Disponibles en 'inputs'")
    st.info(
        "Este es un listado de los archivos de Excel disponibles en la carpeta 'inputs'.")
    st.selectbox("Archvios disponibles", options=default_files)


    st.subheader("Carga de Archivos")
    uploaded_file = st.file_uploader("Subir archivos", type="xlsx")
    if uploaded_file:
        pass

# Sección 1: Filtrado de Información
    st.subheader("Filtrado de Información")
    keyword = st.text_input("Buscar programas por palabras clave")

    programs_df = pd.read_excel('prueba_programas.xlsx')


    # Aplicar filtrado si se ingresa una palabra clave
    if keyword:
        filtered_df = programs_df[programs_df["PROGRAMA ACADÉMICO"].str.contains(keyword, case=False)]
    else:
        filtered_df = programs_df

    # Mostrar la tabla filtrada
    st.table(filtered_df)

    # Sección 2: Parámetros de Análisis
    st.subheader("Parámetros de Análisis")
    years = st.slider("Seleccione el rango de años", min_value=2019, max_value=2023, value=(2021, 2023))
    selected_programs = st.multiselect("Programas seleccionados para análisis",
                                       options=filtered_df["PROGRAMA ACADÉMICO"].tolist())

    # Filtrar el DataFrame según los años seleccionados
    filtered_df = filtered_df[(filtered_df["AÑO"] >= years[0]) & (filtered_df["AÑO"] <= years[1])]

    # Filtrar el DataFrame según los programas seleccionados
    if selected_programs:
        filtered_df = filtered_df[filtered_df["PROGRAMA ACADÉMICO"].isin(selected_programs)]

    # Sección 3: Visualización de Datos
    st.subheader("Visualización de Datos")

    st.title("Comparación de Admitidos entre Años por Programa Académico")

    # Sección para selección de programas
    programas = filtered_df["PROGRAMA ACADÉMICO"].unique()
    programas_seleccionados = st.multiselect(
        "Seleccione los programas académicos que desea comparar:",
        options=programas,
        default=programas
    )
    # Asegurarse de que hay datos para graficar
    if not filtered_df.empty:
        df_filtered = filtered_df[filtered_df["PROGRAMA ACADÉMICO"].isin(programas_seleccionados)]

        # Crear el gráfico usando Plotly
        fig = px.line(
            df_filtered,
            x="AÑO", y="ADMITIDOS",
            color="PROGRAMA ACADÉMICO",
            markers=True,
            labels={"AÑO": "Año", "ADMITIDOS": "Número de Admitidos", "PROGRAMA ACADÉMICO": "Programa Académico"}
        )

        # Configurar el diseño del gráfico
        fig.update_layout(
            title="Admitidos por Año para Programas Seleccionados",
            xaxis_title="Año",
            yaxis_title="Número de Admitidos",
            legend_title="Programa Académico",
            template="plotly_white"
        )

        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig, use_container_width=True)

    else:
        st.write("No hay datos para mostrar según los filtros aplicados.")

gestion_archivos2()