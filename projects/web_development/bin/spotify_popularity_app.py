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
# Crear el botón
if st.button("Construir histograma para tu conjunto de datos"):

    # Escribe un mensaje interactivo
    st.write("Creando histrograma...")

    # Validar que la columna exista
    if "track_popularity" in spotify_df.columns:

        # Crea el histograma
        hist_fig = px.histogram(spotify_df,
                                x="track_popularity",
                                title="Distribución de la Popularidad de las Canciones")

        # Mostrar un gráfico Plotly interactivo
        st.plotly_chart(hist_fig, use_container_width=True)

    else:
        st.error(
            "No se encuentra la columna `track_popularity` en el conjunto de datos")


# Botón gráfico dispersión ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Crear el checkbox
if st.checkbox("Construir el gráfico de dispersión para tu conjunto de datos")

  # Escribe un mensaje interactivo
  st.write('Creando gráfico de dispersión....')

   # Validar que la columna exista
   if "energy" in spotify_df.columns and "track_popularity" in spotify_df.columns and "playlist_genre" in spotify_df.columns:

        # Crea el scatterplot
        scatter_fig = px.scatter(spotify_df,
                                 x="energy", y="track_popularity",
                                 color="playlist_genre", opacity=0.2,
                                 facet_col="playlist_genre",
                                 title="Relación popularidad y la energía por género",
                                 labels={
                                     "energy": "Energía", "track_popularity": "Popularidad de la canción"},
                                 trendline="ols")

        # Mostrar un gráfico Plotly interactivo
        st.plotly_chart(scatter_fig, use_container_width=True)

    else:
        st.error(
            "No se encuentran las columnas para crear el gráfico de dispersión.")
