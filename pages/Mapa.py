import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster
import numpy as np
import login  # Asegúrate de que este módulo esté definido correctamente.

# Configuración de la página
st.set_page_config(
    page_title="Visor de Cuadrillas Gstión de Corrosión",
    page_icon="🌐",
    layout='wide',
    initial_sidebar_state="expanded"
)

# Función de inicio de sesión
login.generarLogin()

# Verificar si el usuario ha iniciado sesión
if 'usuario' not in st.session_state:
    st.warning("Por favor, inicie sesión para acceder a esta página.")
    st.stop()

st.header('Visor de Mapas Corrosion - Colombia')

# Generar datos de prueba
def crear_dataframe_cuadrillas():
    num_cuadrillas = 100
    np.random.seed(42)

    nombres = [f'Cuadrilla {i}' for i in range(num_cuadrillas)]
    # Ajustando latitudes y longitudes para Colombia
    latitudes = np.random.uniform(low=4.0, high=13.0, size=num_cuadrillas)  # Rango de latitudes en Colombia
    longitudes = np.random.uniform(low=-78.0, high=-66.0, size=num_cuadrillas)  # Rango de longitudes en Colombia
    ratings = np.random.uniform(low=1, high=5, size=num_cuadrillas)
    review_counts = np.random.randint(low=1, high=1000, size=num_cuadrillas)
    direcciones = [f'Dirección {i}' for i in range(num_cuadrillas)]

    df_cuadrillas = pd.DataFrame({
        'name': nombres,
        'latitude': latitudes,
        'longitude': longitudes,
        'rating': ratings,
        'review_count': review_counts,
        'full_address': direcciones
    })

    return df_cuadrillas

# Crear el DataFrame de cuadrillas
dfCuadrillas = crear_dataframe_cuadrillas()
dfCuadrillas['review_count'] = dfCuadrillas['review_count'].fillna(1)

# Crear las pestañas
tab1, tab2, tab3, tab4 = st.tabs(['Mapa Plotly', 'Mapa Choropleth', 'Mapa Folium', 'Datos'])

# Pestaña 1: Mapa Plotly
with tab1:    
    parMapa = st.selectbox('Tipo Mapa', options=["open-street-map", "carto-positron", "carto-darkmatter"])        
    parTamano = st.checkbox('Tamaño por cantidad de reviews')
    
    if parTamano:
        fig = px.scatter_mapbox(dfCuadrillas, lat='latitude', lon='longitude', 
                                color='rating', hover_name='name', hover_data=['review_count', 'full_address'],
                                zoom=5, size='review_count', height=600)  # Ajuste de zoom
    else:
        fig = px.scatter_mapbox(dfCuadrillas, lat='latitude', lon='longitude', 
                                color='rating', hover_name='name', hover_data=['review_count', 'full_address'],                                 
                                zoom=5, height=600)  # Ajuste de zoom
    
    fig.update_layout(mapbox_style=parMapa)
    st.plotly_chart(fig, use_container_width=True)

# Pestaña 2: Mapa Choropleth
with tab2:
    df = px.data.gapminder().query("year==2007 & country == 'Colombia'")    
    fig = px.choropleth(df, locations="iso_alpha",
                        color="lifeExp", 
                        hover_name="country", 
                        color_continuous_scale=px.colors.sequential.Plasma)
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df)

# Pestaña 3: Mapa Folium
with tab3:
    parTipoMapa = st.radio('Tipo de marcadores', options=['Cluster', 'Individuales'], horizontal=True)
    m = folium.Map(location=[4.5709, -74.2973], zoom_start=5)  # Ubicación central de Colombia
    
    if parTipoMapa == 'Cluster':
        marker_cluster = MarkerCluster().add_to(m)

    for index, row in dfCuadrillas.iterrows():        
        marker = folium.Marker(        
                location=[row['latitude'], row['longitude']],
                popup=row['name'],
                icon=folium.Icon(color="red", icon="ok-sign"),
            )
        if parTipoMapa == 'Cluster':
            marker.add_to(marker_cluster)
        else:
            marker.add_to(m)
    
    folium.plugins.Fullscreen(
        position="topright",
        title="Pantalla completa",
        title_cancel="Cancelar",
        force_separate_button=True,
    ).add_to(m)
    
    out = st_folium(m, height=600, use_container_width=True)
    st.write(out)

# Pestaña 4: Datos
with tab4:
    st.dataframe(dfCuadrillas, use_container_width=True)
