import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos desde un archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Crear botones para construir el histograma y el gráfico de dispersión
hist_button = st.button('Construir histograma')
scatter_button = st.button('Construir gráfico de dispersión')

# Verificar si se hizo clic en el botón de histograma
if hist_button:
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear el histograma
    fig = px.histogram(car_data, x="odometer")

    # Mostrar el gráfico Plotly
    st.plotly_chart(fig, use_container_width=True)

# Verificar si se hizo clic en el botón de gráfico de dispersión
if scatter_button:
    # Escribir un mensaje
    st.write('Creación de un diagrama de dispersión')

    # Crear el gráfico de dispersión
    fig = px.scatter(car_data)

    # Mostrar el gráfico Plotly
    st.plotly_chart(fig, use_container_width=True)