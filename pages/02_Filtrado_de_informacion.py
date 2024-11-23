import streamlit as st
import pandas as pd
import plotly.express as px



def filtrado_de_info(controlador):
    # Sección 1: Filtrado de Información
    st.subheader("Filtrado de programas por palabras clave")
    keyword = st.text_input("Buscar programas por palabras clave")

    # Sección 2: Parámetros de Análisis
    st.subheader("Parámetros de análisis")
    years = st.slider("Seleccione el rango de años", min_value=2020, max_value=2023, value=(2020, 2021))

    # Botón para realizar la búsqueda
    if st.button("Realizar primera búsqueda"):
        controlador.procesar_datos(years[0], years[1], keyword)
        st.session_state["busqueda_realizada"] = True  # Marcar como realizada

    # Verificar si ya se realizó la búsqueda
    if st.session_state.get("busqueda_realizada", False):
        # Obtener el DataFrame
        df = controlador.get_df()
        df_unique = df.drop_duplicates(subset=["CÓDIGO SNIES DEL PROGRAMA"])

        # Título de la aplicación
        st.title("Selección de Programas para Análisis")

        # Subtítulo
        st.subheader("Seleccione los programas que desea incluir en el análisis")

        # Crear lista para almacenar programas seleccionados
        selected_programs = []

        # Mostrar tabla con checkboxes para cada programa
        for index, row in df_unique.iterrows():
            if st.checkbox(f"{row['PROGRAMA ACADÉMICO']} - {row['INSTITUCIÓN DE EDUCACIÓN SUPERIOR (IES)']} - {row['PRINCIPAL O SECCIONAL']}"
                           f" (Código SNIES: {row['CÓDIGO SNIES DEL PROGRAMA']} Departameto: {row['DEPARTAMENTO DE DOMICILIO DE LA IES']} Municipio: {row['MUNICIPIO DE DOMICILIO DE LA IES']})", key=index):
                selected_programs.append(row.to_dict())

        # Mostrar los programas seleccionados
        if selected_programs:
            st.subheader("Programas Seleccionados (Incluyendo Semestres)")

            # Filtrar el DataFrame original por los programas seleccionados
            criterios = [(df['CÓDIGO SNIES DEL PROGRAMA'] == p['CÓDIGO SNIES DEL PROGRAMA'])
                         for p in selected_programs]
            filtro = pd.concat(criterios, axis=1).any(axis=1)
            df_filtrado = df[filtro]

            # Mostrar el DataFrame filtrado en la tabla
            st.write(df_filtrado)

            if st.button("Actualizar datos"):
                controlador.set_df(df_filtrado)

            # Botón para exportar la selección
            if st.button("Exportar Selección a Excel"):
                df_filtrado.to_excel("programas_seleccionados.xlsx", index=False)
                st.success("¡Archivo Excel generado con éxito!")


filtrado_de_info(st.session_state.controlador)