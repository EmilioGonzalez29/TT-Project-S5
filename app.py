import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import streamlit as st

car_data = pd.read_csv('./Dataset/vehicles_us.csv') # leer los datos

st.title('Análisis de datos para anuncios de venta de vehículos')

st.header('Tablas resumen')

#Filtrado de tablas para resumir datos
cars_new = car_data[car_data['condition'] == 'new'].sort_values(by='price', ascending=False).reset_index(drop=True)
cars_excellent = car_data[car_data['condition'] == 'excellent'].sort_values(by='price', ascending=False).reset_index(drop=True)
cars_good = car_data[car_data['condition'] == 'good'].sort_values(by='price', ascending=False).reset_index(drop=True)

#Creación primera casilla de verificación
build_table_new = st.checkbox('Los primeros 20 vehículos en estado "nuevo" de mayor precio')

#Representación de tablas
if build_table_new:
    #Creación de tabla
    fig = ff.create_table(cars_new.loc[:20,['price', 'model_year', 'model', 'condition', 'fuel', 'transmission']])
    fig.update_traces(textfont_size=8)
    #Representación de tabla
    st.plotly_chart(fig, use_container_width=True)

#Creación segunda casilla de verificación
build_table_excellent = st.checkbox('Los primeros 20 vehículos en estado "excelente" de mayor precio')

if build_table_excellent:
    #Creación de tabla
    fig = ff.create_table(cars_excellent.loc[:20,['price', 'model_year', 'model', 'condition', 'fuel', 'transmission']])
    fig.update_traces(textfont_size=8)
    #Representación de tabla
    st.plotly_chart(fig, use_container_width=True)

#Creación tercera casilla de verificación
build_table_good = st.checkbox('Los primeros 20 vehículos en estado "bueno" de mayor precio')

if build_table_good:
    #Creación de tabla
    fig = ff.create_table(cars_good.loc[:20,['price', 'model_year', 'model', 'condition', 'fuel', 'transmission']])
    fig.update_traces(textfont_size=8)
    #Representación de tabla
    st.plotly_chart(fig, use_container_width=True)


st.header('Visualización gráfica de datos')

#Se reemplazan valores ausentes en "model_year" y "odometer" solo para efectos del procesamiento gráfico
#Para "model_year" se utiliza el año promedio de todo el dataset para los valores ausentes, ya que se desconoce la fecha del mismo
#Para "odometer", se coloca en 0 para los valores ausentes
#Se asigna a un nuevo DataFrame, para no tener dichos cambios reflejados en el dataset original
car_data_graph = car_data
car_data_graph['model_year'] = car_data_graph['model_year'].fillna(car_data_graph['model_year'].mean().astype('int'))
car_data_graph['odometer'] = car_data_graph['odometer'].fillna(0)

st.subheader('Análisis de precios de vehículos en venta')

# crear casillas de verificación
build_histogram_1 = st.checkbox('Histograma')
build_bubble = st.checkbox('Gráfico de burbujas')

if build_histogram_1:  # si la casilla de verificación está seleccionada          
    #Escribir mensaje
    st.write('Histograma de precios según condición del vehículo')
    
    # crear un histograma
    fig = px.histogram(car_data_graph, x="price", color='condition')
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if build_bubble:  # si la casilla de verificación está seleccionada
    # escribir un mensaje
    st.write('Diagrama de burbujas para el precio versus el año del modelo, según condición del vehículo')
    st.write('Nota: El tamaño de burbuja es proporcional al kilometraje del vehículo')
            
    # crear un diagrama de burbuja
    fig = px.scatter(car_data_graph, x="model_year", y="price", size='odometer' , color='condition')
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

st.subheader('Análisis de características de vehículos en venta')

# crear casillas de verificación
build_histogram_2 = st.checkbox('Histograma de modelos de vehículos en venta')
build_histogram_3 = st.checkbox('Histograma de tipo de vehículo')

if build_histogram_2:
    #Escribir un mensaje
    st.write('Distribución de modelos de vehículos en venta según tipo de transmisión')

    fig = px.histogram(car_data_graph, x="model", color='transmission')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if build_histogram_3:
    #Escribir un mensaje
    st.write('Distribución del tipo de vehículos en venta según el tipo de combustible')

    fig = px.histogram(car_data_graph, x="type", color='fuel')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)