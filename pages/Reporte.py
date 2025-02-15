import streamlit as st
import pandas as pd
import datetime
import geocoder

# Configuración de la página (Debe ser lo primero en el script)
st.set_page_config(
    page_title="Registro de Operación - Cuadrillas",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Simulación de base de datos
DATA_FILE = "registro_operaciones.csv"
PROGRAMACION_FILE = "programacion_cuadrillas.csv"

# Función para obtener coordenadas
def obtener_coordenadas():
    g = geocoder.ip('me')
    return g.latlng if g.latlng else (0, 0)

# Cargar datos existentes
def cargar_datos():
    try:
        return pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Empleado", "Fecha", "Hora Inicio", "Hora Fin", "Latitud", "Longitud", "Observaciones"])

def cargar_programacion():
    try:
        return pd.read_csv(PROGRAMACION_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Cuadrilla", "Día", "Tarea", "Ubicación", "Empleado Asignado"])

# Guardar datos
def guardar_datos(df):
    df.to_csv(DATA_FILE, index=False)

# Interfaz en Streamlit
st.title("Registro de Operación - Cuadrillas")

# Página de programación
st.sidebar.title("Menú")
opcion = st.sidebar.radio("Selecciona una opción", ["Registro de Operación", "Programación Semanal"])

if opcion == "Programación Semanal":
    st.header("📋 Programación de Cuadrillas")
    df_programacion = cargar_programacion()
    if df_programacion.empty:
        st.warning("No hay programación disponible.")
    else:
        st.dataframe(df_programacion)

if opcion == "Registro de Operación":
    # Identificación del usuario
    empleado = st.text_input("Ingrese su nombre")

    # Registro de inicio de operación
    if st.button("Iniciar operación"):
        coords = obtener_coordenadas()
        inicio = datetime.datetime.now()
        st.session_state["inicio"] = inicio.strftime("%Y-%m-%d %H:%M:%S")
        st.session_state["coords"] = coords
        st.success(f"Operación iniciada en {st.session_state['inicio']} con coordenadas {coords}")

    # Registro de fin de operación
    if "inicio" in st.session_state:
        if st.button("Finalizar operación"):
            fin = datetime.datetime.now()
            df = cargar_datos()
            nuevo_registro = pd.DataFrame({
                "Empleado": [empleado],
                "Fecha": [datetime.date.today()],
                "Hora Inicio": [st.session_state["inicio"]],
                "Hora Fin": [fin.strftime("%Y-%m-%d %H:%M:%S")],
                "Latitud": [st.session_state["coords"][0]],
                "Longitud": [st.session_state["coords"][1]],
                "Observaciones": [st.text_area("Observaciones")]
            })
            df = pd.concat([df, nuevo_registro], ignore_index=True)
            guardar_datos(df)
            st.success("Operación finalizada y registrada correctamente.")

    # Mostrar datos almacenados
    if st.checkbox("Ver registros de operación"):
        df = cargar_datos()
        st.dataframe(df)
