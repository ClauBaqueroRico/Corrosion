import streamlit as st
import pandas as pd
from datetime import datetime
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Corrosion Interna Cenit",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cargamos fecha actual
today = datetime.today().strftime("%Y")

# Cargamos librerías de MaterializeCSS, Material Icons y Font Awesome
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">', unsafe_allow_html=True)
st.markdown('<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">', unsafe_allow_html=True)
st.markdown('<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css" rel="stylesheet">', unsafe_allow_html=True)

# HTML content
html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enlaces a Archivos Power BI</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 90%;
            margin: auto;
            overflow: hidden;
        }
        header {
            background: #333;
            color: #fff;
            padding-top: 30px;
            min-height: 70px;
            border-bottom: #77aadd 3px solid;
        }
        header h1 {
            text-align: center;
            text-transform: uppercase;
            margin: 0;
            font-size: 24px;
        }
        .link-section {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
            margin-top: 20px;
        }
        .link-box {
            background: #fff;
            padding: 20px;
            margin: 10px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 45%;
            box-sizing: border-box;
        }
        .link-box h2 {
            text-align: center;
            color: #333;
        }
        .link-item {
            padding: 10px;
            border-bottom: 1px #ccc dotted;
        }
        .link-item:last-child {
            border-bottom: none;
        }
        .link-item a {
            color: #333;
            text-decoration: none;
            font-weight: bold;
        }
        .link-item a:hover {
            color: #77aadd;
        }
        .embed-container {
            margin-top: 50px; /* Ajusta el margen superior según sea necesario */
            text-align: center;
        }
        .embed-container iframe {
            width: 100%; /* Ajusta el ancho del iframe según sea necesario */
            height: 600px; /* Ajusta la altura del iframe según sea necesario */
        }
        @media (max-width: 768px) {
            .link-box {
                width: 100%;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>Contrato 8000009037  Servicios de Atención Integral de la Amenaza de Corrosión en Equipos Estáticos de la Infraestructura de Transporte de Hidrocarburos</h1>
    </header>
    <div class="container">
        <div class="link-section">
            <div class="link-box">
                <h2>Planeación y Seguimiento</h2>
                <div class="link-item">
                    <a href="https://forms.office.com/Pages/ResponsePage.aspx?id=FNT6_6O2Mk-pvULSj8gR8dSPcBsCbEhJgdkPK01vntFURU9EMVg5V1UwWFpJRjA2NTJUTk5CSUVWNSQlQCN0PWcu" target="_blank">Reporte Diario Operativo</a>
                </div>
                <div class="link-item">
                    <a href="https://app.powerbi.com/reportEmbed?reportId=46dd64bd-1da5-4d0a-87db-1057534d3d41&autoAuth=true&ctid=fabd047c-ff48-492a-8bbb-8f98b9fb9cca" target="_blank">Tablero de Control Administrativo</a>
                </div>
                <!-- Agrega más enlaces aquí -->
            </div>
            <div class="link-box">
                <h2>Corrosión Interna</h2>
                <div class="link-item">
                    <a href="https://app.powerbi.com/reportEmbed?reportId=155a48bb-acbb-4034-b589-9cddb7552176&autoAuth=true&ctid=fffad414-b6a3-4f32-a9bd-42d28fc811f1" target="_blank">Informe de Corrosión Interna</a>
                </div>
                <div class="link-item">
                    <a href="http://example.com/corrosioninterna2" target="_blank">Informe de Corrosión Interna 2</a>
                </div>
                <!-- Agrega más enlaces aquí -->
            </div>
            <div class="link-box">
                <h2>Corrosión Externa</h2>
                <div class="link-item">
                    <a href="https://app.bureauveritas.com.co/URPCv2/Account/Login" target="_blank">Gestión de Corrosión</a>
                </div>
                <div class="link-item">
                    <a href="https://app.powerbi.com/reportEmbed?reportId=b9f01638-88f8-4ba3-9592-31fb5baa966a&autoAuth=true&ctid=fffad414-b6a3-4f32-a9bd-42d28fc811f1" target="_blank">Informe de Corrosión Externa 2</a>
                </div>
                <!-- Agrega más enlaces aquí -->
            </div>
            <div class="link-box">
                <h2>Analítica</h2>
                <div class="link-item">
                    <a href="https://app.powerbi.com/reportEmbed?reportId=2b7a9563-6e29-476b-a930-df9c56bf4f8a&autoAuth=true&ctid=fffad414-b6a3-4f32-a9bd-42d28fc811f1" target="_blank">Informe de Analítica Illis</a>
                </div>
                <div class="link-item">
                    <a href="http://example.com/analitica2" target="_blank">Informe de Analítica 2</a>
                </div>
                <!-- Agrega más enlaces aquí -->
            </div>
        </div>
    </div>
    <div class="embed-container">
        <h2>KPI_**</h2>
        <iframe title="Dash-PDT-BV_Actualizado 2024" width="1140" height="600" src="https://app.powerbi.com/reportEmbed?reportId=564bbf3b-941b-4530-943f-bc59a228559b&autoAuth=true&ctid=fffad414-b6a3-4f32-a9bd-42d28fc811f1" frameborder="0" allowFullScreen="true"></iframe>
    </div>
</body>
</html>
"""

# Render the HTML content
components.html(html_content, height=800)

