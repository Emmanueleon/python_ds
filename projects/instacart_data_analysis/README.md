# Análisis de Datos de Instacart
Este proyecto analiza los hábitos de compra de los clientes de Instacart utilizando un conjunto de datos modificado. El objetivo es limpiar los datos, realizar un análisis exploratorio y extraer información útil a través de visualizaciones y estadísticas descriptivas.

## Descripción del Proyecto
Instacart es una plataforma de entregas de comestibles donde los clientes pueden registrar pedidos para recibirlos en sus domicilios. Este proyecto utiliza datos proporcionados por Instacart durante una competición en Kaggle en 2017, con algunas modificaciones para fines de análisis y aprendizaje.

El análisis incluye:

- Limpieza y preprocesamiento de datos.
- Análisis exploratorio de datos (EDA) para identificar patrones y tendencias.
- Visualización de datos para comunicar hallazgos importantes.

## Conjunto de Datos
El conjunto de datos consta de cinco archivos CSV que contienen información sobre pedidos, productos, pasillos y departamentos:

- instacart_orders.csv: Información sobre cada pedido realizado en Instacart.
- products.csv: Detalles de los productos disponibles.
- order_products.csv: Información sobre los productos incluidos en cada pedido.
- aisles.csv: Detalles sobre las categorías de pasillo.
- departments.csv: Información sobre los departamentos de productos.

## Estructura del Proyecto

instacart-data-analysis/
│
├── data/
│   ├── instacart_orders.csv
│   ├── products.csv
│   ├── order_products.csv
│   ├── aisles.csv
│   └── departments.csv
│
├── notebooks/
│   └── instacart_analysis.ipynb
│
├── results/
│   └── analysis_results.md
│
├── README.md

El notebook contiene todos los pasos necesarios para cargar, limpiar y analizar los datos. Sigue las celdas en orden para reproducir los análisis y visualizaciones. Al completar el análisis, deberías ser capaz de:

- Identificar patrones de compra según la hora del día y el día de la semana.
- Determinar los productos más comprados y aquellos que son más frecuentemente reordenados.
- Analizar los comportamientos de los clientes con respecto a la frecuencia de pedidos y los productos seleccionados.
