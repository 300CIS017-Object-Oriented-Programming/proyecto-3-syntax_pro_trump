import streamlit as st
import atexit
from src.GestorArchivos import eliminarArchivos
from src.SNIESController import SNIESController

def iniciar_programa():
    # Asigna el sistema como variable de instancia y en session_state para persistencia
    if 'controlador' not in st.session_state:
        st.session_state.controlador = SNIESController()

    if 'lista_archivos' not in st.session_state:
        st.session_state.lista_archivos_extra = []

    # Set page title, icon, layout wide (more used space in central area) and sidebar initial state
    st.set_page_config(page_title="SNIES_EXTRACTOR", page_icon="🕹️", layout="wide",
                       initial_sidebar_state="collapsed")
    st.write("Usa el menú de la barra lateral para navegar entre las secciones del SNIES EXTRACTOR\nHecho Por Syntax Error.")


if __name__ == "__main__":
    iniciar_programa()