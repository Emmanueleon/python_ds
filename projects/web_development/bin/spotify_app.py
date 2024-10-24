# Importación de paquetes
import pandas as pd
import plotly.express as px
import streamlit as st


# Función para cargar datos con caché
@st.cache_data
def cargar_datos():
    return pd.read_csv("../data/spotify_songs.csv")


# Lectura de dataframe
spotify_df = cargar_datos()

# Título de la página
st.header("Proyecto sprint 6")


# Botón histograma ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
st.header("Histograma de la popularidad")

# crear un botón
if st.button("Construir histograma para tu conjunto de datos"):

    st.write("Creando histograma...")

    # Validar si la columna existe en el dataframe
    if "track_popularity" in spotify_df.columns:

        # Crea el histograma
        hist_fig = px.histogram(spotify_df,
                                x="track_popularity",
                                title="Distribución de la Popularidad de las Canciones")

        # mostrar un gráfico Plotly interactivo
        st.plotly_chart(hist_fig, use_container_width=True)

    else:
        st.error(
            "No se encuentra la columna `track_popularity` en el conjunto de datos")


# Botón gráfico dispersión ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
st.header("Gráfico de dispersión")

# Checkbox para mostrar el scatter plot
if st.checkbox('Construir un scatter'):

    st.write('Creando gráfico de dispersión...')

    # Validar que las columnas existan en el dataframe
    if "energy" in spotify_df.columns and "track_popularity" in spotify_df.columns and "playlist_genre" in spotify_df.columns:

        # Crear gráfico de dispersión
        scatter_fig = px.scatter(spotify_df,
                                 x="energy",
                                 y="track_popularity",
                                 color="playlist_genre",
                                 facet_col="playlist_genre",
                                 opacity=0.2,
                                 title="Relación entre popularidad y energía por género",
                                 labels={
                                     "energy": "Energía", "track_popularity": "Popularidad de la canción"},
                                 trendline="ols")

        # Mostrar el gráfico Plotly interactivo
        st.plotly_chart(scatter_fig, use_container_width=True)

    else:
        st.error(
            "No se encuentran las columnas necesarias para crear el gráfico de dispersión.")
