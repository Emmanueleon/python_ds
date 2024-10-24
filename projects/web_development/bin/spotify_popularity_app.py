# Importación de paquetes
import pandas as pd
import plotly.express as px
import streamlit as st


# Lectura de dataframe
spotify_df = pd.read_csv("data/spotify_songs.csv")


# Título de la página
st.header("Proyecto sprint 6")


# Botones del programa

# Botón histograma ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
st.header("Histograma de la popularidad")

# crear un botón
if st.button("Construir histograma para tu conjunto de datos"):

    # Escribe un mensaje interactivo
    st.write("Creando histrograma...")

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
# st.header("Botón gráfico dispersión")

# build_scatter= st.checkbox('Construir un scatter')
# if build_scatter:
#    # escribir un mensaje
#    st.write('Creación de un scatter....')
#
    # crear un histograma
#    scatter_fig = px.scatter(spotify_df,
#                             x="energy",
#                             y="track_popularity",
#                             color="playlist_genre",
#                             facet_col="playlist_genre",
#                             opacity=0.2,
#                             title="Relación popularidad y la energía por género",
#                            labels={"energy": "Energía", "track_popularity": "Popularidad de la canción"},
#                             trendline="ols")
#
    # mostrar un gráfico Plotly interactivo
#    st.plotly_chart(scatter_fig, use_container_width=True)
