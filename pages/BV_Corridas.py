import streamlit as st
from datetime import datetime
import login

# Configuración de la página
st.set_page_config(
    page_title="Informacion Corrosion Integral",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cargar el sistema de login
login.generarLogin()

# Verificar si el usuario ha iniciado sesión
if 'usuario' not in st.session_state:
    st.warning("Por favor, inicie sesión para acceder a esta página.")
    st.stop()

# Cargar la fecha actual
today = datetime.today().strftime("%Y")

# Títulos y estilo
st.subheader('Servicios de Atención Integral de la Amenaza de Corrosión en Equipos Estáticos de la Infraestructura de Transporte de Hidrocarburos')

# Contenedor principal
st.title("Links de interés y tableros de control")

# Sección de enlaces con dos columnas
sections = {
    "Planeación y Seguimiento": [
        ("Reporte Diario Operativo", "https://forms.office.com/Pages/ResponsePage.aspx?id=FNT6_6O2Mk-pvULSj8gR8dSPcBsCbEhJgdkPK01vntFURU9EMVg5V1UwWFpJRjA2NTJUTk5CSUVWNSQlQCN0PWcu"),
        ("Tablero de Control Administrativo", "https://app.powerbi.com/view?r=eyJrIjoiNTk1MDIwMmMtYjEzZi00NDkwLTk2ZDItZjQyYjM1Mzc3NjEyIiwidCI6ImE2YjRmOTliLWQ1NzItNDFhYy05MDExLTRkMzAyNTBiYjkyYiIsImMiOjR9")
    ],
    "Corrosión Interna": [
        ("Informe de Corrosión Interna", "http://example.com/corrosioninterna2"),
        ("Informe de Corrosión Interna 2", "http://example.com/corrosioninterna2")
    ],
    "Corrosión Externa": [
        ("Gestión de Corrosión", "https://app.bureauveritas.com.co/URPCv2/Account/Login"),
        ("Informe de Corrosión Externa 2", "http://example.com/corrosioninterna2")
    ],
    "Analítica": [
        ("Informe de Analítica Illis", "https://app.powerbi.com/view?r=eyJrIjoiZTgwMWE2MDYtZjEwNS00MWYwLWJkNDItZmRjYjg5NWJkMGQwIiwidCI6ImE2YjRmOTliLWQ1NzItNDFhYy05MDExLTRkMzAyNTBiYjkyYiIsImMiOjR9"),
        ("Informe de Analítica 2", "http://example.com/analitica2")
    ]
}

# Dividir la interfaz en dos columnas
col1, col2 = st.columns(2)

for index, (title, links) in enumerate(sections.items()):
    if index % 2 == 0:
        with col1:
            st.markdown(f"### {title}")
            for link_text, link_url in links:
                st.markdown(f"- [{link_text}]({link_url})")
    else:
        with col2:
            st.markdown(f"### {title}")
            for link_text, link_url in links:
                st.markdown(f"- [{link_text}]({link_url})")

# Sección de Estrategia y enlace a "Otros"
st.markdown("### Estrategia")
st.markdown("[🔐 Estrategia Consolidada](https://app.powerbi.com/view?r=eyJrIjoiZDAyYTkyODUtZjNlYi00YWRmLThmOTgtNjQwMjRiYTkxNWNlIiwidCI6ImE2YjRmOTliLWQ1NzItNDFhYy05MDExLTRkMzAyNTBiYjkyYiIsImMiOjR9)")

# Enlace a "Otros"
st.markdown("[( https://telemetria.detektorgps.com/telemetria_v2/index.php) Detektor")
