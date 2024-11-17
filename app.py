import streamlit as st

def iniciar_programa():
    """
    # Asigna el sistema como variable de instancia y en session_state para persistencia
    if 'controlador' not in st.session_state:
        st.session_state.sistema = #Nombre del controlador
    """
    # Set page title, icon, layout wide (more used space in central area) and sidebar initial state
    st.set_page_config(page_title="Aplicación de Gestión de Reservas", page_icon="🕹️", layout="wide",
                       initial_sidebar_state="collapsed")
    st.write("Usa el menú de la barra lateral para navegar entre las secciones de la aplicación.")


if __name__ == "__main__":
    iniciar_programa()