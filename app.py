import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('files/datasets/input/vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear el histograma
    fig = px.histogram(car_data, x="odometer")

    # Mostrar el gráfico Plotly
    st.plotly_chart(fig, use_container_width=True)