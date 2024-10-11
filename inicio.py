import streamlit as st
import login as login
import altair as alt
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Corrosion Interna", page_icon="📶", layout="wide")
df = pd.read_csv('df.csv')
# Crear columnas para los logos
col1, col2, col3 = st.columns([1, 6, 1])  # Ajusta los anchos de las columnas como prefieras

# Colocar el logo en la columna izquierda
with col1:
    st.markdown(
        """
        <div style="background-color: #f0f0f0; padding: 10px;">
            <img src="LogoBV-White.png" width="150">
        </div>
        """,
        unsafe_allow_html=True
    )

# Colocar el logo en la columna derecha
with col3:
    st.image("Cenit_Logo.png", width=150)  # Ajusta el tamaño según sea necesario

# El header del login centrado
col2.header('Bienvenido :blue[porfavor navegue en el panel izquierdo]')

# Llamar la función de login
# Verificar si el usuario ha iniciado sesión
if 'usuario' in st.session_state:
    if 'df' not in st.session_state:
        st.session_state.df = df  # Inicializar df en session_state

    st.subheader('KPI Generales')

    edited_df = pd.DataFrame({
        'Date Submitted': pd.date_range(start='3/1/2024', periods=100, freq='M'),
        'Status': ['Open', 'Closed', 'Pending'] * 33 + ['Open'],
        'Priority': ['High', 'Medium', 'Low'] * 33 + ['High']
    })

    # Mostrar métricas
    st.header("Statistics")

    col1, col2, col3 = st.columns(3)
    num_open_tickets = len(st.session_state.df[st.session_state.df.Status == "Open"])
    col1.metric(label="Number of open tickets", value=num_open_tickets, delta=10)
    col2.metric(label="First response time (hours)", value=5.2, delta=-1.5)
    col3.metric(label="Average resolution time (hours)", value=16, delta=2)

    # Mostrar gráficos
    st.write("##### Atención realizada por mes")
    status_plot = (
        alt.Chart(edited_df)
        .mark_bar()
        .encode(
            x="month(Date Submitted):O",
            y="count():Q",
            xOffset="Status:N",
            color="Status:N",
        )
        .configure_legend(
            orient="bottom", titleFontSize=14, labelFontSize=14, titlePadding=5
        )
    )
    st.altair_chart(status_plot, use_container_width=True, theme="streamlit")

    st.write("##### Atención realizada según prioridad")
    priority_plot = (
        alt.Chart(edited_df)
        .mark_arc()
        .encode(theta="count():Q", color="Priority:N")
        .properties(height=300)
        .configure_legend(
            orient="bottom", titleFontSize=14, labelFontSize=14, titlePadding=5
        )
    )
    st.altair_chart(priority_plot, use_container_width=True, theme="streamlit")

    
    # Agregar el tablero embebido de Power BI
    # power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiZDAyYTkyODUtZjNlYi00YWRmLThmOTgtNjQwMjRiYTkxNWNlIiwidCI6ImE2YjRmOTliLWQ1NzItNDFhYy05MDExLTRkMzAyNTBiYjkyYiIsImMiOjR9"  # Reemplaza con tu URL de Power BI
    #st.components.v1.iframe(power_bi_url, width=800, height=600, scrolling=True)
