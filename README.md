 #🌍 Gestión de Datos de Países en Python**
Este es el Trabajo Práctico Integrador (TPI) de **Programación 1** de la Tecnicatura Universitaria en Programación de la UTN.

### **✨ Descripción del Programa**

La aplicación es un sistema de gestión de información sobre países. Su objetivo principal es aplicar los conceptos de estructuras de datos (**listas y diccionarios**), modularización con **funciones**, y técnicas de **filtrado, ordenamiento y estadísticas**.

El sistema lee los datos de los países desde un **archivo CSV** y ofrece un menú interactivo en consola para realizar diversas operaciones.

**Cada país se representa con los siguientes datos:**

  * **Nombre** (*string*)
  * **Población** (*int*)
  * **Superficie en $km^{2}$** (*int*)
  * **Continente** (*string*)

-----

### **🚀 Funcionalidades Principales**

El menú de opciones permite al usuario realizar las siguientes tareas:

  * **Búsqueda:** Buscar un país por nombre (coincidencia parcial o exacta).
  * **Filtros:**
      * Por **Continente**.
      * Por **Rango de Población**.
      * Por **Rango de Superficie**.
  * **Ordenamiento:** Ordenar la lista de países por **Nombre**, **Población** o **Superficie** (ascendente o descendente).
  * **Estadísticas:**
      * País con **mayor y menor población**.
      * **Promedio de población**.
      * **Promedio de superficie**.
      * **Cantidad de países por continente**.
  * **Validaciones:** El programa incluye manejo de errores y validación para entradas inválidas, búsquedas sin resultados y errores de formato en el CSV.

### **🛠️ Instrucciones de Uso**

1.  **Requisitos:** Asegúrate de tener instalado **Python 3.x**.
2.  **Archivos:** El proyecto debe contener el archivo principal del código Python (`main.py` o similar) y el **archivo CSV** con el dataset base de países.
3.  **Interacción:** El sistema presentará un menú de opciones. Simplemente ingresa el número de la opción deseada y sigue las indicaciones en pantalla.

-----

### **🖥️ Ejemplos de Entradas y Salidas**

*(Aquí debes incluir ejemplos concretos de cómo se ve el menú y los resultados de algunas operaciones. Puedes usar capturas de pantalla o texto simulado)*.

**Ejemplo 1: Menú Principal**

```
*** GESTOR DE PAÍSES ***

1. Buscar país por nombre
2. Filtrar países
3. Ordenar países
4. Mostrar estadísticas
5. Salir

Ingrese su opción: 
```

**Ejemplo 2: Filtrar por Continente**

  * **Entrada:** Opción 2 (Filtrar), luego Continente, y se ingresa "América".
  * **Salida (Simulada):**

| Nombre | Población | Superficie ($km^2$) | Continente |
| :--- | :--- | :--- | :--- |
| Argentina | 45376763 | 2780400 | América |
| Brasil | 213993437 | 8515767 | América |
| ... | ... | ... | ... |

### **👥 Integrantes del Equipo**

Este trabajo fue desarrollado por:

  * **Franco Rios**
  * **Fabrizio Simon**

Link del video: https://drive.google.com/file/d/1kXj6A9gH7CTLGU2eb5UPyc6rlOEKK6tc/view?usp=drive_link
