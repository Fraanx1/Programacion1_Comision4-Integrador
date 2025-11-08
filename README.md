# 🌍 Gestión de Datos de Países en Python

Este es el Trabajo Práctico Integrador (TPI) de **Programación 1** de la Tecnicatura Universitaria en Programación de la UTN-FRM. Es una aplicación de consola diseñada para gestionar, consultar y analizar un conjunto de datos de países del mundo.

## 👥 Integrantes del Equipo

* **Franco Rios**
* **Fabrizio Simon**

## 📺 Video de Demostración

Para una demostración visual y completa del funcionamiento del sistema en acción (sin necesidad de leer el código), puede ver el siguiente video:

▶️ https://drive.google.com/file/d/159xptCLiZePUjutym4sVBiTSjlipLE3Y/view?usp=sharing

---

## ✨ Descripción del Programa

La aplicación es un sistema de gestión de información sobre países. Su objetivo principal es aplicar los conceptos fundamentales de la programación estructurada y el manejo de datos en Python.

El sistema lee los datos de los países desde un archivo `paises.csv` y los carga en memoria. Una vez cargados, ofrece un menú interactivo en consola para realizar diversas operaciones de consulta, filtrado y análisis estadístico. El proyecto pone un fuerte énfasis en la **modularización** (separando la lógica en distintos archivos), la **validación de entradas** (para crear un programa robusto que no falle ante entradas incorrectas) y el uso de **estructuras de datos** adecuadas (listas y diccionarios).

### 🗂️ Estructura de Datos

El núcleo del sistema es la forma en que almacena la información. Se utiliza una **lista principal**, donde cada elemento de esta lista es un **diccionario** que representa a un país.

Esta estructura (una **Lista de Diccionarios**) fue elegida por su claridad y flexibilidad.

Cada diccionario de país tiene las siguientes claves:

* `nombre` (string): El nombre oficial del país. (Ej: "Argentina")
* `poblacion` (int): El número total de habitantes. (Ej: 45376763)
* `superficie` (float): El área total en kilómetros cuadrados. (Ej: 2780400.00)
* `continente` (string): El continente al que pertenece. (Ej: "América")

---

## 🚀 Funcionalidades Principales

El menú de opciones permite al usuario realizar un conjunto completo de tareas de gestión de datos:

1.  **📥 Cargar Datos (Opción 1):**
    * Lee el archivo `paises.csv`.
    * Omite la cabecera (primera línea).
    * Procesa cada línea, convirtiendo población a `int` y superficie a `float`.
    * Crea un diccionario por cada país y lo añade a la lista principal.
    * Incluye manejo de errores para líneas con formato incorrecto o tipos de datos inválidos.

2.  **🔎 Búsqueda por Nombre (Opción 2):**
    * Solicita al usuario que ingrese un texto (el nombre o parte del nombre de un país).
    * Realiza una búsqueda por **coincidencia parcial**. (Ej: "arg" encontrará "Argentina").
    * La búsqueda es **insensible a mayúsculas y acentos** para mejorar la experiencia de usuario.

3.  **🌎 Filtros (Opciones 3, 4 y 5):**
    * **Por Continente (Opción 3):** Solicita un nombre de continente y muestra solo los países que pertenecen a él. También es insensible a mayúsculas y acentos.
    * **Por Rango de Población (Opción 4):** Pide un valor **mínimo** y un **máximo** de población. Muestra todos los países cuya población esté dentro de ese rango (inclusivo).
    * **Por Rango de Superficie (Opción 5):** Pide un valor **mínimo** y un **máximo** de superficie y filtra de manera similar a la población.

4.  **🔀 Ordenamiento (Opción 6):**
    * Permite al usuario reordenar la lista completa de países.
    * Pregunta por qué campo desea ordenar: `Nombre`, `Población` o `Superficie`.
    * Pregunta el orden: `Ascendente` (A-Z, menor a mayor) o `Descendente` (Z-A, mayor a menor).
    * Muestra la lista recién ordenada.

5.  **📊 Estadísticas (Opción 7):**
    * Calcula y muestra un resumen descriptivo de los datos cargados:
        * País con **mayor** y **menor** población.
        * País con **mayor** y **menor** superficie.
        * **Promedio** de población (total de habitantes / N° de países).
        * **Promedio** de superficie (total de km² / N° de países).
        * Un conteo de **cuántos países** hay por cada continente.

6.  **📚 Mostrar Todos (Opción 8):**
    * Imprime en pantalla la lista completa de países (tal como esté ordenada en ese momento) en un formato de tabla claro y legible.

7.  **🛡️ Validaciones:**
    * El programa no se detiene si el usuario ingresa una letra en lugar de un número.
    * Valida que los rangos numéricos sean lógicos (mínimo <= máximo).
    * Maneja búsquedas y filtros que no devuelven resultados, informando al usuario.

---

## 🛠️ Instrucciones de Uso

### Requisitos Previos

* Tener instalado **Python 3.x** en su sistema.

### 📂 Archivos Necesarios

Para que el programa funcione, asegúrese de tener la siguiente estructura de archivos en la misma carpeta:

```

/Proyecto
├── 📄 main.py         (Archivo principal para ejecutar)
├── 📄 funciones.py     (Módulo con la lógica del programa)
├── 📄 validaciones.py (Módulo con las funciones de validación)
└── 📄 paises.csv       (El archivo con la base de datos)

````

### 🏃 Ejecución

1.  Abra una terminal, `cmd` o `powershell` en su sistema operativo.
2.  Navegue usando el comando `cd` hasta la carpeta donde se encuentran los archivos del proyecto.
3.  Una vez en la carpeta correcta, ejecute el siguiente comando para iniciar el programa:

```bash
python main.py
````

4.  ¡Listo\! Se desplegará el menú principal y podrá comenzar a interactuar con el sistema.

-----

## 🖥️ Ejemplos de Entradas y Salidas

### Menú Principal

Al ejecutar el programa, se presentará el siguiente menú:

```
╭─────────────────────────────────────────────────────╮
│                                                     │
│         🌍 GESTIÓN MUNDIAL DE PAÍSES 🌍              │
│               UTN - Programación 1                  │
│                                                     │
├─────────────────────────────────────────────────────┤
│ [1] 📥  Cargar Datos (CSV)                           │
│ [2] 🔎  Buscar por Nombre                            │
│ [3] 🌎  Filtrar por Continente                       │
│ [4] 👥  Filtrar por Población                        │
│ [5] 🗺   Filtrar por Superficie                      │
│ [6] 🔀  Ordenar Países                              │
│ [7] 📊  Ver Estadísticas                             │
│ [8] 📚  Mostrar Lista Completa                       │
├─────────────────────────────────────────────────────┤
│ [0] ❌  Salir del Programa                           │
╰─────────────────────────────────────────────────────╯
➡️  Seleccione una opción (0-8):
```

### Ejemplo 1: Cargar y Buscar

1.  Usuario ingresa `1` (Cargar Datos).
      * *Salida:* `✅✍️ Se cargaron 195 países exitosamente.`
2.  Usuario ingresa `2` (Buscar por Nombre).
      * *Entrada:* `Ingrese el nombre (o parte) del país a buscar: argen`
      * *Salida:*

<!-- end list -->

```
✅ Resultados de la búsqueda:

| Nombre                                   | Población (hab) | Superficie (km²) | Continente |
|------------------------------------------|-----------------|------------------|------------|
| Argentina                                |      45,376,763 |     2,780,400.00 | América    |
----------------------------------------------------------------------------------------------
```

### Ejemplo 2: Estadísticas

1.  Usuario ingresa `7` (Ver Estadísticas).
      * *Salida:*

<!-- end list -->

```
--- 📊 ESTADÍSTICAS GLOBALES 📊 ---
🌎 Total de países cargados: 195
------------------------------
🥇 País con MAYOR Población: China (1,439,323,776 hab.)
🥉 País con MENOR Población: Ciudad del Vaticano (801 hab.)
🏞️ País con MAYOR Superficie: Rusia (17,098,246.00 km²)
🏜️ País con MENOR Superficie: Ciudad del Vaticdano (0.49 km²)
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
```

```
```
