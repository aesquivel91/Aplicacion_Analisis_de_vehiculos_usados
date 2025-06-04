import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header('Análisis de anuncios de venta de vehículos en EE.UU.')

# -------------------------
# Usando BOTONES
# -------------------------

# Histograma de odómetro
hist_button = st.button('Mostrar histograma de odómetro')

if hist_button:
    st.write('Creación de un histograma para la columna "odometer"')
    fig_hist = px.histogram(car_data, x="odometer", nbins=40,
                            title='Distribución de kilometraje (odómetro)')
    st.plotly_chart(fig_hist, use_container_width=True)

# Gráfico de dispersión: año vs precio
scatter_button = st.button('Mostrar gráfico de dispersión Año vs Precio')

if scatter_button:
    st.write('Creación de un gráfico de dispersión entre "model_year" y "price"')
    fig_scatter = px.scatter(car_data, x="model_year", y="price",
                             title='Relación entre Año del Modelo y Precio',
                             opacity=0.6, trendline='ols')
    st.plotly_chart(fig_scatter, use_container_width=True)

# -------------------------
# Usando CHECKBOXES
# -------------------------
build_hist = st.checkbox('Construir histograma de odómetro')
if build_hist:
    st.write('Histograma basado en el kilometraje')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Construir gráfico de dispersión Año vs Precio')
if build_scatter:
    st.write('Gráfico de dispersión entre año del modelo y precio')
    fig = px.scatter(car_data, x='model_year', y='price', trendline='ols')
    st.plotly_chart(fig, use_container_width=True)
