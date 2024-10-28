# Análisis de tarifas Megaline

## Descripción del proyecto

Como analista para el operador de telecomunicaciones Megaline, tu tarea es analizar dos tarifas de prepago, Surf y Ultimate, para determinar cuál genera más ingresos.

Usarás datos de 500 clientes que incluyen información sobre llamadas, mensajes de texto y tráfico de datos en 2018.

### Descripción de las Tarifas

#### Surf

- Pago mensual: $20
- Incluye: 500 minutos, 50 SMS, 15 GB de datos
- Exceso:
  - Minuto: $0.03
  - SMS: $0.03
  - GB de datos: $10

#### Ultimate

- Pago mensual: $70
- Incluye: 3000 minutos, 1000 SMS, 30 GB de datos
- Exceso:
  - Minuto: $0.01
  - SMS: $0.01
  - GB de datos: $7

### Objetivo

El objetivo de este proyecto es evaluar el comportamiento de los clientes y determinar cuál tarifa de Megaline es más rentable.

El proyecto busca realizar un análisis preliminar sobre el comportamiento de los clientes para determinar qué tarifa de prepago, en promedio, contribuye más a los ingresos de la empresa. Para ello, se llevará a cabo un análisis estadístico que considera:

- La cantidad de llamadas y mensajes de texto realizados por cada cliente.
- El volumen de datos consumidos.
- Los ingresos generados por cada cliente según la tarifa utilizada.

Este análisis ayudará a Megaline a evaluar y ajustar sus estrategias de precios y publicidad.

## Conjunto de Datos

El conjunto de datos consta de cinco archivos CSV que contienen información sobre usuarios, llamadas realizadas, mensajes de texto, tráfico de datos y tarifas:

- `users`: Información sobre los usuarios.
- `calls`: Datos sobre las llamadas realizadas.
- `messages`: Datos sobre los mensajes de texto enviados.
- `internet`: Datos sobre el tráfico de datos.
- `plans`: Información sobre las tarifas.

### Diccionario de datos

A continuación se muestra un diccionario de datos que enumera las columnas de cada tabla y describe los datos que contienen.

**Tabla `users`**: Información sobre los usuarios.

- `user_id`: Identificador único
- `first_name`: Nombre
- `last_name`: Apellido
- `age`: Edad
- `reg_date`: Fecha de suscripción
- `churn_date`: Fecha de baja
- `city`: Ciudad
- `plan`: Nombre de la tarifa

**Tabla `calls`**: Datos sobre las llamadas realizadas.

- `id`: Identificador único
- `call_date`: Fecha de llamada
- `duration`: Duración (minutos)
- `user_id`: Identificador del usuario

**Tabla `messages`**: Datos sobre los mensajes de texto enviados.

- `id`: Identificador único
- `message_date`: Fecha del SMS
- `user_id`: Identificador del usuario

**Tabla `internet`**: Datos sobre el tráfico de datos.

- `id`: Identificador único
- `mb_used`: Datos usados (MB)
- `session_date`: Fecha de la sesión
- `user_id`: Identificador del usuario

**Tabla `plans`**: Información sobre las tarifas.

- `plan_name`: Nombre de la tarifa
- `usd_monthly_fee`: Pago mensual (USD)
- `minutes_included`: Minutos incluidos
- `messages_included`: SMS incluidos
- `mb_per_month_included`: Datos incluidos (MB)
- `usd_per_minute`: Precio por minuto extra
- `usd_per_message`: Precio por SMS extra
- `usd_per_gb`: Precio por GB extra

## Instrucciones para el Proyecto

### Paso 1: Cargar y Explorar los Datos

- Rutas de archivos:
  - `/datasets/megaline_calls.csv`
  - `/datasets/megaline_internet.csv`
  - `/datasets/megaline_messages.csv`
  - `/datasets/megaline_plans.csv`
  - `/datasets/megaline_users.csv`

### Paso 2: Preparación de Datos

- Convertir tipos de datos y corregir errores.
- Calcular:
  - Número de llamadas y minutos usados por mes.
  - Cantidad de SMS enviados por mes.
  - Volumen de datos por mes.
  - Ingresos mensuales por usuario, considerando el plan y el exceso.

### Paso 3: Análisis de Datos

- Describir el comportamiento de los clientes.
- Calcular media, varianza y desviación estándar.
- Crear histogramas y describir distribuciones.

### Paso 4: Pruebas de Hipótesis

- Comparar ingresos promedio entre tarifas.
- Comparar ingresos en Nueva York-Nueva Jersey vs. otras regiones.
- Formulación y prueba de hipótesis, especificando el valor alfa.

### Paso 5: Conclusiones

- Resumir los hallazgos y recomendaciones.

## Estructura del Repositorio

El repositorio está organizado en los siguientes directorios y archivos:

- `datasets/` : Contiene los archivos CSV con los datos.
- `notebooks/` : Contiene el Jupyter Notebook con el análisis.
- `scripts/` : Scripts de Python para el procesamiento y análisis de datos.
- `README.md` : Este archivo con la descripción del proyecto.
