import streamlit as st
import pandas as pd
import datetime
import geocoder
import login  # Módulo de autenticación

# Configuración de la página
st.set_page_config(
    page_title="Registro de Operación - Cuadrillas",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Función de inicio de sesión
login.generarLogin()
if 'usuario' not in st.session_state:
    st.warning("Por favor, inicie sesión para acceder a esta página.")
    st.stop()

# Archivo de datos
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
st.title("📊 Registro de Operación y Programación")

# Registro de inicio de operación
st.subheader("🕒 Registro de Operación")
km_inicio = st.number_input("Kilometraje de inicio", min_value=0.0, step=0.1)
if st.button("Registrar Inicio de Operación"):
    coords = obtener_coordenadas()
    inicio = datetime.datetime.now()
    st.session_state["inicio"] = inicio.strftime("%Y-%m-%d %H:%M:%S")
    st.session_state["coords"] = coords
    st.session_state["km_inicio"] = km_inicio
    st.success(f"Inicio registrado en {st.session_state['inicio']} con coordenadas {coords}")

# Selector de semana
semanas_disponibles = ["Semana 1", "Semana 2", "Semana 3", "Semana 4"]
semana_seleccionada = st.selectbox("Seleccione la semana", semanas_disponibles)

# Cargar datos de programación
df_programacion = cargar_programacion()
if df_programacion.empty:
    st.warning("No hay programación disponible para esta semana.")
else:
    # Selector de empleado
    empleados_disponibles = df_programacion["Empleado Asignado"].unique()
    empleado_seleccionado = st.selectbox("Seleccione su nombre", empleados_disponibles)
    
    # Filtrar programación por empleado
    df_empleado = df_programacion[df_programacion["Empleado Asignado"] == empleado_seleccionado]
    st.subheader(f"Órdenes de trabajo asignadas a {empleado_seleccionado}")
    st.dataframe(df_empleado, use_container_width=True)
    
    # Registro de ejecución
    st.subheader("📌 Reporte de Ejecución")
    orden_seleccionada = st.selectbox("Seleccione la orden a reportar", df_empleado["Tarea"])
    estado_ejecucion = st.radio("Estado de ejecución", ["Ejecutado", "No ejecutado"])
    inconveniente = None
    notas = ""
    
    if estado_ejecucion == "No ejecutado":
        inconveniente = st.radio("¿Hubo inconveniente?", ["Sí", "No"])
        if inconveniente == "Sí":
            notas = st.text_area("Describa el inconveniente")
    
    km_fin = st.number_input("Kilometraje de fin", min_value=st.session_state.get("km_inicio", 0.0), step=0.1)
    
    if st.button("Guardar Reporte"):
        reporte = {
            "Empleado": empleado_seleccionado,
            "Orden": orden_seleccionada,
            "Estado": estado_ejecucion,
            "Inconveniente": inconveniente if inconveniente else "N/A",
            "Notas": notas,
            "KM Inicio": st.session_state.get("km_inicio", 0.0),
            "KM Fin": km_fin,
            "Fecha": datetime.date.today(),
            "Hora Inicio": st.session_state.get("inicio", "N/A"),
            "Hora Fin": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Latitud": st.session_state["coords"][0],
            "Longitud": st.session_state["coords"][1]
        }
        st.session_state.setdefault("reportes", []).append(reporte)
        st.success("Reporte guardado con éxito.")
    
    if "reportes" in st.session_state and st.session_state["reportes"]:
        df_reportes = pd.DataFrame(st.session_state["reportes"])
        st.subheader("📜 Reportes Generados")
        st.dataframe(df_reportes, use_container_width=True)

# Botón para regresar al menú principal
if st.button("🔙 Volver al Menú Principal"):
    st.experimental_rerun()
