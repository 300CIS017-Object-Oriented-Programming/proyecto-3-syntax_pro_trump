import streamlit as st
import pandas as pd
import plotly.express as px

def graficas_anios(controlador):

    df_original = controlador.get_df()

    keyword = st.selectbox("Archivos disponibles",
                           options=["ADMITIDOS", "GRADUADOS", "INSCRITOS", "MATRICULADOS", "PRIMER CURSO"])

    if keyword:
        # Identificar dinámicamente las columnas relevantes para la palabra clave seleccionada
        columnas_relevantes = [col for col in df_original.columns if keyword in col]

        if not columnas_relevantes:
            st.warning(f"No se encontraron datos para '{keyword}'.")
        else:
            # Incluir las columnas clave adicionales
            columnas_relevantes = ["CÓDIGO SNIES", "PROGRAMA ACADÉMICO"] + columnas_relevantes
            df_filtrado = df_original[columnas_relevantes]

            # Reorganizar el DataFrame en formato largo
            df_long = pd.melt(
                df_filtrado,
                id_vars=["CÓDIGO SNIES", "PROGRAMA ACADÉMICO"],
                value_vars=columnas_relevantes[2:],
                var_name=f"AÑO_{keyword}",
                value_name=keyword
            )

            # Extraer el año del nombre de la columna
            df_long["AÑO"] = df_long[f"AÑO_{keyword}"].str.extract("(\d{4})").astype(int)

            # Eliminar la columna temporal "AÑO_{keyword}"
            df_long.drop(columns=[f"AÑO_{keyword}"], inplace=True)

            # Título de la página
            st.title(f"Comparación de {keyword} entre Años por Programa Académico")

            # Crear identificadores únicos para cada programa académico basado en CÓDIGO SNIES
            df_long["IDENTIFICADOR"] = df_long["PROGRAMA ACADÉMICO"] + " (SNIES: " + df_long["CÓDIGO SNIES"].astype(
                str) + ")"

            # Selección de programas académicos
            programas = df_long["IDENTIFICADOR"].unique()
            programas_seleccionados = st.multiselect(
                "Seleccione los programas académicos que desea comparar:",
                options=programas,
                default=programas
            )

            # Filtrar el DataFrame según la selección del usuario
            if programas_seleccionados:
                df_filtered = df_long[df_long["IDENTIFICADOR"].isin(programas_seleccionados)]

                # Crear el gráfico
                fig = px.line(
                    df_filtered,
                    x="AÑO",
                    y=keyword,
                    color="IDENTIFICADOR",
                    markers=True,
                    labels={
                        "AÑO": "Año",
                        keyword: f"Número de {keyword}",
                        "IDENTIFICADOR": "Programa Académico"
                    },
                    title=f"Comparación de {keyword} entre Años"
                )

                # Mostrar el gráfico en Streamlit
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("Seleccione al menos un programa académico para visualizar el gráfico.")
    else:
        st.warning("Seleccione algo")

graficas_anios(st.session_state.controlador)