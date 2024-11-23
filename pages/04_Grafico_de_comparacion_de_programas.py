import streamlit as st
import pandas as pd
import plotly.express as px

from src.Settings import STR_CODIGO_SNIES, STR_METODOLOGIA, STR_PROGRAMA_ACADEMICO, STR_NOMBRE_IES, STR_TIPO_IES, \
    STR_DEPARTAMENTO, STR_MUNICIPIO, STR_NIVEL_FORMACION, STR_ADMITIDOS, STR_GRADUADOS, STR_INSCRITOS, STR_MATRICULADOS, \
    STR_PRIMER_CURSO


def graficas_comparacion(controlador):

    df = controlador.get_df()

    if df is not None:
        print(df)




graficas_comparacion(st.session_state.controlador)