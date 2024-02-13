import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('./Dataset/vehicles_us.csv') # leer los datos

st.header('Análisis de datos para anuncios de venta de vehículos')
#hist_button = st.button('Crear histograma') #Creación de botón

# crear casillas de verificación
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un diagrama de dispersión')

if build_histogram:  # si la casilla de verificación está seleccionada
    # escribir un mensaje
    st.write('Creación de un histograma para el kilometraje de los coches en venta anunciados')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:  # si la casilla de verificación está seleccionada
    # escribir un mensaje
    st.write('Creación de un diagrama de dispersión para el kilometraje vs precio de los coches')
            
    # crear un diagrama de dispersión
    fig = px.scatter(car_data, x="odometer", y="price", color='price')
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
            

