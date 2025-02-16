import streamlit as st
import pandas as pd
import login  # Módulo de autenticación

# Configuración de la página
st.set_page_config(
    page_title="Tablero de Programación",
    page_icon="📋",
    layout="wide",
)

# Archivo de programación
PROGRAMACION_FILE = "programacion_cuadrillas.csv"

# Función para cargar la programación de cuadrillas
def cargar_programacion():
    try:
        return pd.read_csv(PROGRAMACION_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Cuadrilla", "Día", "Tarea", "Ubicación", "Empleado Asignado"])

# Función de inicio de sesión
login.generarLogin()
if 'usuario' not in st.session_state:
    st.warning("Por favor, inicie sesión para acceder a esta página.")
    st.stop()

# Interfaz en Streamlit
st.title("📊 Tablero de Programación Semanal")

# Selector de semana
semanas_disponibles = ["Semana 1", "Semana 2", "Semana 3", "Semana 4"]  # Simulación de semanas
semana_seleccionada = st.selectbox("Seleccione la semana", semanas_disponibles)

# Cargar datos de programación
st.subheader(f"Resumen de la {semana_seleccionada}")
df_programacion = cargar_programacion()

if df_programacion.empty:
    st.warning("No hay programación disponible para esta semana.")
else:
    # Contar órdenes por empleado
    resumen_empleados = df_programacion["Empleado Asignado"].value_counts().reset_index()
    resumen_empleados.columns = ["Empleado", "Órdenes Asignadas"]
    st.dataframe(resumen_empleados, use_container_width=True)
