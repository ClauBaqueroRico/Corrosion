import streamlit as st
import login
import pandas as pd
login.generarLogin()
if 'usuario' in st.session_state:
    st.header('Programación :red[Semanal]')

# Archivo de programación
PROGRAMACION_FILE = "programacion_cuadrillas.csv"

# Función para cargar la programación de cuadrillas
def cargar_programacion():
    try:
        return pd.read_csv(PROGRAMACION_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Cuadrilla", "Día", "Tarea", "Ubicación", "Empleado Asignado"])

# Configuración de la página
st.set_page_config(
    page_title="Programación de Cuadrillas",
    page_icon="📋",
    layout="wide",
)

# Sidebar
st.sidebar.title("Menú")
opcion = st.sidebar.radio("Selecciona una opción", ["Programación Semanal"])

# Página de Programación Semanal
if opcion == "Programación Semanal":
    st.title("📋 Programación de Cuadrillas")
    
    df_programacion = cargar_programacion()
    
    if df_programacion.empty:
        st.warning("No hay programación disponible.")
    else:
        # Mostrar la programación en una tabla interactiva
        st.dataframe(df_programacion, use_container_width=True)
        
        # Filtros para buscar cuadrillas o empleados
        filtro_cuadrilla = st.selectbox("Filtrar por Cuadrilla", ["Todas"] + list(df_programacion["Cuadrilla"].unique()))
        filtro_empleado = st.text_input("Buscar por nombre de empleado")
        
        # Aplicar filtros
        df_filtrado = df_programacion
        if filtro_cuadrilla != "Todas":
            df_filtrado = df_filtrado[df_filtrado["Cuadrilla"] == filtro_cuadrilla]
        if filtro_empleado:
            df_filtrado = df_filtrado[df_filtrado["Empleado Asignado"].str.contains(filtro_empleado, case=False, na=False)]
        
        # Mostrar datos filtrados
        st.subheader("Programación Filtrada")
        st.dataframe(df_filtrado, use_container_width=True)