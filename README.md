🌍 Gestión de Datos de Países en Python

Este es el Trabajo Práctico Integrador (TPI) de Programación 1 de la Tecnicatura Universitaria en Programación de la UTN-FRM.

👥 Integrantes del Equipo

Franco Rios

Fabrizio Simon

📺 Video de Demostración

Para una demostración completa del funcionamiento del sistema (sin lectura de código), puede ver el siguiente video:

▶️ [ENLACE A SU VIDEO AQUÍ] (Sugerencia: Súbanlo a YouTube como "No listado" o a Google Drive con enlace público)

✨ Descripción del Programa

La aplicación es un sistema de gestión de información sobre países. Su objetivo principal es aplicar los conceptos de estructuras de datos (listas y diccionarios), modularización con funciones, y técnicas de filtrado, ordenamiento y estadísticas.

El sistema lee los datos de los países desde un archivo paises.csv y ofrece un menú interactivo en consola para realizar diversas operaciones.

Estructura de Datos

Cada país se representa como un diccionario con las siguientes claves:

nombre (string)

poblacion (int)

superficie (float)

continente (string)

🚀 Funcionalidades Principales

El menú de opciones permite al usuario realizar las siguientes tareas:

Cargar Datos: Lee el archivo paises.csv y carga los datos en memoria.

Búsqueda: Buscar un país por nombre (coincidencia parcial, insensible a mayúsculas y acentos).

Filtros:

Por Continente.

Por Rango de Población (mínimo y máximo).

Por Rango de Superficie (mínimo y máximo).

Ordenamiento: Ordenar la lista de países por Nombre, Población o Superficie (ascendente o descendente).

Estadísticas: Calcular y mostrar:

País con mayor y menor población/superficie.

Promedio de población y superficie.

Cantidad de países por continente.

Mostrar Todos: Imprime la lista completa de países cargados.

Validaciones: El programa incluye manejo de errores para entradas inválidas, búsquedas sin resultados y errores de formato en el CSV.

🛠️ Instrucciones de Uso

Requisitos

Python 3.x

Archivos Necesarios

Asegúrese de tener los siguientes archivos en la misma carpeta:

/Proyecto
├── main.py
├── funciones.py
├── validaciones.py
└── paises.csv


Ejecución

Abra una terminal o línea de comandos.

Navegue hasta la carpeta del proyecto.

Ejecute el siguiente comando:

python main.py


🖥️ Ejemplos de Entradas y Salidas

Menú Principal

Al ejecutar el programa, se presentará el siguiente menú:

╭─────────────────────────────────────────────────────╮
│                                                     │
│         🌍 GESTIÓN MUNDIAL DE PAÍSES 🌍              │
│               UTN - Programación 1                  │
│                                                     │
├─────────────────────────────────────────────────────┤
│ [1] 📥  Cargar Datos (CSV)                           │
│ [2] 🔎  Buscar por Nombre                            │
│ [3] 🌎  Filtrar por Continente                       │
│ [4] 👥  Filtrar por Población                        │
│ [5] 🗺   Filtrar por Superficie                      │
│ [6] 🔀  Ordenar Países                              │
│ [7] 📊  Ver Estadísticas                             │
│ [8] 📚  Mostrar Lista Completa                       │
├─────────────────────────────────────────────────────┤
│ [0] ❌  Salir del Programa                           │
╰─────────────────────────────────────────────────────╯
➡️  Seleccione una opción (0-8): 


Ejemplo 1: Cargar y Buscar

Usuario ingresa 1 (Cargar Datos).

Salida: ✅✍️ Se cargaron 195 países exitosamente.

Usuario ingresa 2 (Buscar por Nombre).

Entrada: Ingrese el nombre (o parte) del país a buscar: argen

Salida:

✅ Resultados de la búsqueda:

| Nombre                                   | Población (hab) | Superficie (km²) | Continente |
|------------------------------------------|-----------------|------------------|------------|
| Argentina                                |      45,376,763 |     2,780,400.00 | América    |
----------------------------------------------------------------------------------------------


Ejemplo 2: Estadísticas

Usuario ingresa 7 (Ver Estadísticas).

Salida:

--- ESTADÍSTICAS GLOBALES ---
🌎 Total de países cargados: 195
------------------------------
🥇 País con MAYOR Población: China (1,439,323,776 hab.)
🥉 País con MENOR Población: Ciudad del Vaticano (801 hab.)
🏞️ País con MAYOR Superficie: Rusia (17,098,246.00 km²)
🏜️ País con MENOR Superficie: Ciudad del Vaticano (0.49 km²)
------------------------------
📊 Promedio de Población: 39,709,388 hab.
🗺️ Promedio de Superficie: 694,402.04 km²
------------------------------
🌍 Cantidad de Países por Continente:
 - África: 54 países
 - América: 35 países
 - Asia: 48 países
 - Europa: 49 países
 - Oceanía: 9 países

