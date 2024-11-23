import streamlit as st
import os
from src.Settings import *

def gestion_archivos(lista_archivos_extra, ruta_directorio):
    # Sección 1: Carga de Archivos
    st.title("Gestion de archivos")

    input_folder = BASE_PATH  # Asegúrate de que la carpeta existe

    # Utilizamos esta lista para imprimir los archivos cargados al SNIES EXTRACTOR
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
    #FIXME: Hacer el cambio para acceder a la ruta verdadera donde estan los archivos extra
    if uploaded_file is not None:
        ruta_archivo = BASE_PATH + "/" + uploaded_file.name
        lista_archivos_extra.append(ruta_archivo)
        with open(ruta_archivo, "wb") as nuevo_archivo:
            nuevo_archivo.write(uploaded_file.getbuffer())

    if st.button("Desea borrar los archivos adicionales?"):
        for ruta in lista_archivos_extra:
            os.unlink(ruta)
        lista_archivos_extra.clear()

gestion_archivos(st.session_state.lista_archivos_extra, st.session_state.ruta_directorio)

