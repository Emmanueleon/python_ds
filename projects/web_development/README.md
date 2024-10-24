## Descripción del proyecto

---

Este proyecto presenta un análisis interactivo de casi 30,000 canciones obtenidas de la API de Spotify. Utilizando **Streamlit** como plataforma web, los usuarios pueden explorar datos de canciones en función de sus características como popularidad, energía y género, entre otras. La aplicación permite visualizar estos datos mediante gráficos.
Actualmente, la aplicación está en desarrollo, pero se espera una versión más robusta con nuevas funcionalidades y mejoras en la experiencia de usuario.

Puedes acceder a la aplicación a través del siguiente enlace en Render: [spotify_app](https://sprint6-tt-spotify.onrender.com)

## Objetivo

---

El objetivo principal de este proyecto es desarrollar una aplicación web que proporcione una plataforma interactiva donde los usuarios puedan explorar las características de canciones que se encuentran en Spotify.

Además de analizar las características musicales y de popularidad de las canciones, la aplicación web permite a los usuarios:

- **Visualizar** gráficos interactivos sobre la popularidad, energía y otros atributos musicales de las canciones.
- **Explorar** cómo distintos géneros y subgéneros influyen en la popularidad y energía de las canciones.
- **Filtrar** canciones por atributos como el género, la danceabilidad, el tempo y más.
- **Crear** gráficos personalizados de dispersión y de histogramas para obtener insights específicos.

Este análisis y visualización interactiva ayudan a identificar patrones comunes y características musicales clave, proporcionando información valiosa tanto para usuarios comunes, como para artistas, productores y curadores de playlists.

## Estructura del Proyecto

La estructura del proyecto está organizada de la siguiente manera:

ds_python/
│
├── projects/
│ └── web_development/
│ ├── bin/ # Scripts ejecutables para la aplicación
│ ├── data/ # Archivos de datos crudos y procesados
│ ├── notebooks/ # Jupyter Notebooks para análisis
│ ├── streamlit/ # Aplicación de Streamlit y sus configuraciones
│ ├── requirements.txt # Dependencias necesarias para el proyecto
│ ├── .gitignore # Archivos y directorios ignorados por

## Conjunto de Datos

---

Este proyecto utiliza un conjunto de datos obtenido de la API de Spotify a través del paquete `spotifyr`. El conjunto incluye casi 30,000 canciones, y contiene tanto características musicales como información sobre la popularidad de cada canción. La base de datos fue creada por Joakim Arvidsson y fue descargada a través de [Kaggle](https://www.kaggle.com/datasets/joebeachcapital/30000-spotify-songs/data).

### Diccionario de Datos

A continuación se detalla el diccionario de datos con las variables presentes en el dataset:

| Variable                   | Tipo      | Descripción                                                                                                                                         |
| -------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `track_id`                 | character | ID único de la canción                                                                                                                              |
| `track_name`               | character | Nombre de la canción                                                                                                                                |
| `track_artist`             | character | Artista de la canción                                                                                                                               |
| `track_popularity`         | double    | Popularidad de la canción (0-100) donde un valor más alto es mejor                                                                                  |
| `track_album_id`           | character | ID único del álbum                                                                                                                                  |
| `track_album_name`         | character | Nombre del álbum                                                                                                                                    |
| `track_album_release_date` | character | Fecha de lanzamiento del álbum                                                                                                                      |
| `playlist_name`            | character | Nombre de la playlist                                                                                                                               |
| `playlist_id`              | character | ID de la playlist                                                                                                                                   |
| `playlist_genre`           | character | Género de la playlist                                                                                                                               |
| `playlist_subgenre`        | character | Subgénero de la playlist                                                                                                                            |
| `danceability`             | double    | Medida de la capacidad de una canción para bailar. Va de 0.0 (menos bailable) a 1.0 (más bailable)                                                  |
| `energy`                   | double    | Energía de la canción. Medida de 0.0 a 1.0 donde valores altos representan canciones más rápidas, ruidosas y activas.                               |
| `key`                      | double    | Tonalidad estimada de la canción en formato numérico, donde 0 = C, 1 = C♯/D♭, 2 = D, etc. Si no se detectó tonalidad, el valor es -1.               |
| `loudness`                 | double    | Volumen promedio de la canción en decibelios (dB). Valores típicos van entre -60 y 0 dB.                                                            |
| `mode`                     | double    | Modalidad de la canción (mayor o menor). 1 representa mayor, y 0 representa menor.                                                                  |
| `speechiness`              | double    | Detecta la presencia de palabras habladas en una pista. Va de 0.0 a 1.0, donde valores más cercanos a 1.0 indican más palabras habladas.            |
| `acousticness`             | double    | Medida de confianza sobre si la canción es acústica. Un valor de 1.0 indica alta confianza de que es una pista acústica.                            |
| `instrumentalness`         | double    | Predice si una pista no contiene voces. Valores por encima de 0.5 sugieren que es instrumental.                                                     |
| `liveness`                 | double    | Detecta la presencia de audiencia en la grabación. Valores por encima de 0.8 sugieren que la pista probablemente se grabó en vivo.                  |
| `valence`                  | double    | Medida de la positividad musical de la canción. Un valor de 0.0 indica negatividad (tristeza, enojo) y 1.0 indica positividad (felicidad, euforia). |
| `tempo`                    | double    | Tempo general de la canción en pulsaciones por minuto (BPM).                                                                                        |
| `duration_ms`              | double    | Duración de la canción en milisegundos.                                                                                                             |
