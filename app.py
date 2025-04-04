import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("vehicles_us.csv")  # leer los datos

st.header("Análisis de datos de coches usados")  # encabezado de la aplicación
st.subheader("Visualización de datos de coches usados")  # subtítulo de la aplicación

build_histogram = st.checkbox(
    "Construir histograma"
)  # crear una casilla de verificación

if build_histogram:  # al hacer clic en la casilla
    st.write(
        "Creación de un histograma para ver la cantidad de coches por precio"
    )  # escribir un mensaje
    fig = px.histogram(car_data, x="price")  # crear un histograma
    st.plotly_chart(
        fig, use_container_width=True
    )  # mostrar un gráfico Plotly interactivo

build_scatter = st.checkbox("Construir un diagrama de dispersion")

if build_scatter:
    st.write(
        "Creación de un diagrama de dispersión para ver la relación entre el precio y el año del modelo"
    )  # escribir un mensaje
    fig = px.scatter(
        car_data, x="price", y="model_year"
    )  # crear un diagrama de dispersión
    st.plotly_chart(
        fig, use_container_width=True
    )  # mostrar un gráfico Plotly interactivo
