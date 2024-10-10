import streamlit as st
import login as login

st.header('Bienvenido :blue[porfavor ingrese sus credenciales]')
login.generarLogin()
if 'usuario' in st.session_state:
    st.subheader('Información página principal')