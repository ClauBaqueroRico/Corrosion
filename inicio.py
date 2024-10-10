import streamlit as st
import login as login

# Configuración de la página
st.set_page_config(page_title="Corrosion Interna", page_icon="📊", layout="wide")

# Crear columnas para los logos
col1, col2, col3 = st.columns([1, 6, 1])  # Ajusta los anchos de las columnas como prefieras

# Colocar el logo en la columna izquierda
with col1:
    st.image("LogoBV-White.png", width=150)  # Ajusta el tamaño según sea necesario

# Colocar el logo en la columna derecha
with col3:
    st.image("Cenit_Logo.png", width=150)  # Ajusta el tamaño según sea necesario

# El header del login centrado
col2.header('Bienvenido :blue[porfavor navegue en el panel izquierdo]')

# Llamar la función de login
login.generarLogin()

# Verificar si el usuario ha iniciado sesión
if 'usuario' in st.session_state:
    st.subheader('Información página principal')
    
    # Agregar el tablero embebido de Power BI
    # power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiZDAyYTkyODUtZjNlYi00YWRmLThmOTgtNjQwMjRiYTkxNWNlIiwidCI6ImE2YjRmOTliLWQ1NzItNDFhYy05MDExLTRkMzAyNTBiYjkyYiIsImMiOjR9"  # Reemplaza con tu URL de Power BI
    st.components.v1.iframe(power_bi_url, width=800, height=600, scrolling=True)
