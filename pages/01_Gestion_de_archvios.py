import streamlit as st
import os

def gestion_archivos():
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

gestion_archivos()

