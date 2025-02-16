import streamlit as st
import pandas as pd
import login  # Módulo de autenticación

# Configuración de la página (Debe ser la primera instrucción después de importar módulos)
st.set_page_config(
    page_title="Tablero de Programación",
    page_icon="📋",
    layout="wide",
)

# Función de inicio de sesión
login.generarLogin()
if 'usuario' not in st.session_state:
    st.warning("Por favor, inicie sesión para acceder a esta página.")
    st.stop()

# Archivo de programación
PROGRAMACION_FILE = "programacion_cuadrillas.csv"

# Función para cargar la programación de cuadrillas
def cargar_programacion():
    try:
        return pd.read_csv(PROGRAMACION_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Cuadrilla", "Día", "Tarea", "Ubicación", "Empleado Asignado"])

# Interfaz en Streamlit
st.title("📊 Tablero de Programación Semanal")

# Selector de semana
semanas_disponibles = ["Semana 1", "Semana 2", "Semana 3", "Semana 4"]  # Simulación de semanas
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
    
    km_inicio = st.number_input("Kilometraje de inicio", min_value=0.0, step=0.1)
    km_fin = st.number_input("Kilometraje de fin", min_value=km_inicio, step=0.1)
    
    if st.button("Guardar Reporte"):
        reporte = {
            "Empleado": empleado_seleccionado,
            "Orden": orden_seleccionada,
            "Estado": estado_ejecucion,
            "Inconveniente": inconveniente if inconveniente else "N/A",
            "Notas": notas,
            "KM Inicio": km_inicio,
            "KM Fin": km_fin
        }
        st.session_state.setdefault("reportes", []).append(reporte)
        st.success("Reporte guardado con éxito.")
    
    if "reportes" in st.session_state and st.session_state["reportes"]:
        df_reportes = pd.DataFrame(st.session_state["reportes"])
        st.subheader("📜 Reportes Generados")
        st.dataframe(df_reportes, use_container_width=True)