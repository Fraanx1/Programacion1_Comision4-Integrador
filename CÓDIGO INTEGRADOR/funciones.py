# --- funciones.py ---
# Este archivo contiene la lógica principal de la aplicación (manipulación de datos).

# Importamos las funciones necesarias del archivo de validaciones
from validaciones import validar_rango_numerico, validar_string, validar_texto

def cargar_datos(nombre_archivo_csv):

    """
    Lee y procesa el archivo CSV de países.
    Convierte cada línea en un diccionario y maneja errores.
    """
    paises = []
    
    try:
        # Abre el archivo en modo lectura ('r') con codificación 'utf-8'
        with open(nombre_archivo_csv, 'r', encoding='utf-8') as archivo:
            # Saltea la primera línea (cabecera)
            next(archivo) 
            
            # Itera sobre cada línea restante del archivo
            for i, linea in enumerate(archivo):
                num_linea = i + 2 # (i arranca en 0, +1 por cabecera, +1 por ser índice)
                
                try:
                    # Limpia y separa la línea por comas
                    datos = [d.strip() for d in linea.split(',')]
                    
                    # 1. Valida que la línea tenga exactamente 4 campos
                    if len(datos) != 4:
                        print(f"""⚠️ Línea {num_linea} ({linea.strip()}): Error de formato. Se omitirá.""")
                        continue
                        
                    # 2. Crea el diccionario convirtiendo los tipos de datos
                    pais = {
                        'nombre': datos[0],
                        'poblacion': int(datos[1]), 
                        'superficie': float(datos[2]), 
                        'continente': datos[3]
                    }
                    # 3. Agrega el diccionario válido a la lista
                    paises.append(pais)

                except ValueError:
                    # Captura error si int() o float() fallan
                    print(f"""⚠️ Línea {num_linea}: Error de conversión (población o superficie). Se omitirá.""")
                except Exception:
                    # Captura cualquier otro error inesperado en la línea
                    print(f"""⚠️ Línea {num_linea}: Error desconocido al procesar. Se omitirá.""")
    
    except FileNotFoundError:
        # Captura error si el archivo 'paises.csv' no existe
        print(f"""❌ ERROR CRÍTICO: No se encontró el archivo '{nombre_archivo_csv}'.""")
    except Exception:
        # Captura cualquier otro error al intentar abrir el archivo (ej. permisos)
        print("❌ ERROR CRÍTICO: Fallo general al acceder al archivo CSV.")
        
    return paises


def buscar_por_nombre(paises):

    """Busca países por coincidencia parcial de nombre"""

    if not paises:
        print("ℹ️ No hay datos de países cargados.")
        return
        
    # Pide y valida un string de búsqueda (no vacío, sin números)
    busqueda_input = validar_string("Ingrese el nombre (o parte) del país a buscar: ")

    # Normaliza la búsqueda
    busqueda_norm = validar_texto(busqueda_input)

    # Filtra la lista de países usando comprensión de listas
    resultados = [
        pais for pais in paises 
        if busqueda_norm in validar_texto(pais['nombre'])
    ]
            
    if resultados:
        print("\n✅ Resultados de la búsqueda:")
        mostrar_paises(resultados)
    else:
        print(f"ℹ️ No se encontraron países que contengan '{busqueda_input}'.")


def filtrar_por_continente(paises):

    """Filtra países por nombre de continente, ignorando acentos."""

    # Pide y valida el nombre del continente
    continente_input = validar_string("Ingrese el continente a filtrar: ")
    
    # Normaliza la entrada del usuario
    continente_norm = validar_texto(continente_input)
    
    
    # Filtra la lista comparando datos normalizados
    resultados = [
        pais for pais in paises 
        if validar_texto(pais['continente']) == continente_norm
    ]
    return resultados


def filtrar_por_rango(paises, clave):

    """Filtra países por un rango numérico (población o superficie)."""

    if not paises:
        print("ℹ️ No hay datos de países para filtrar.")
        return []
        
    # Pide y valida el rango (mínimo y máximo)
    min_val, max_val = validar_rango_numerico()
    
    # Filtra la lista según la clave ('poblacion' o 'superficie')
    resultados = [
        pais for pais in paises
        if min_val <= pais[clave] <= max_val
    ]
    return resultados


def ordenar_paises(paises):

    """Ordena la lista de países por nombre, población o superficie (asc o desc)."""

    if not paises:
        print("ℹ️ No hay datos para ordenar.")
        return
        
    # Valida la clave de ordenamiento
    while True:
        opcion = input("Ordenar por (N)ombre, (P)oblación, (S)uperficie: ").strip().upper()
        if opcion in ('N', 'P', 'S'):
            break
        print("❌ Opción de ordenamiento inválida. Use N, P o S.")
        
    # Asigna la clave de diccionario correcta
    clave_ordenamiento = {'N': 'nombre', 'P': 'poblacion', 'S': 'superficie'}.get(opcion)
    
    # Valida el orden (Ascendente/Descendente)
    while True:
        orden = input("Orden (A)scendente o (D)escendente: ").strip().upper()
        if orden in ('A', 'D'):
            break
        print("❌ Opción de orden inválida. Use A o D.")

    # Determina el valor booleano para 'reverse'
    reverso = True if orden == 'D' else False
    
    # Ordena la lista usando la función sorted() y una lambda
    paises_ordenados = sorted(paises, key=lambda pais: pais[clave_ordenamiento], reverse=reverso)
    
    print(f"\n✅ Países ordenados por '{clave_ordenamiento}' ({'Descendente' if reverso else 'Ascendente'}):")
    # Muestra la lista ordenada
    mostrar_paises(paises_ordenados)


def mostrar_estadisticas(paises):

    """Calcula y muestra estadísticas descriptivas sobre los datos."""

    if not paises:
        print("ℹ️ No hay datos de países cargados para calcular estadísticas.")
        return
    
    cantidad_paises = len(paises)
    if cantidad_paises == 0:
        print("ℹ️ No hay países en la lista para calcular estadísticas.")
        return

    # --- 1. Cálculos de Máximos y Mínimos ---
    
    # Población
    pais_mayor_pob = max(paises, key=lambda p: p['poblacion'])
    pais_menor_pob = min(paises, key=lambda p: p['poblacion'])
    
    
    # Superficie
    pais_mayor_sup = max(paises, key=lambda p: p['superficie'])
    pais_menor_sup = min(paises, key=lambda p: p['superficie'])

    
    # --- 2. Promedios ---
    total_poblacion = sum(pais['poblacion'] for pais in paises)
    total_superficie = sum(pais['superficie'] for pais in paises)
    
    promedio_poblacion = total_poblacion / cantidad_paises
    promedio_superficie = total_superficie / cantidad_paises

    # --- 3. Cantidad por Continente ---
    conteo_continentes = {}
    for pais in paises:
        continente = pais['continente']
        # .get(continente, 0) obtiene el valor actual o 0 si no existe
        conteo_continentes[continente] = conteo_continentes.get(continente, 0) + 1

    # --- Impresión de resultados ---
    print("\n--- ESTADÍSTICAS GLOBALES ---")
    print(f"🌎 Total de países cargados: {cantidad_paises}")
    print("-" * 30)
    
    # Población
    print(f"🥇 País con MAYOR Población: {pais_mayor_pob['nombre']} ({pais_mayor_pob['poblacion']:,} hab.)")
    print(f"🥉 País con MENOR Población: {pais_menor_pob['nombre']} ({pais_menor_pob['poblacion']:,} hab.)")

    # Superficie
    print(f"🏞️ País con MAYOR Superficie: {pais_mayor_sup['nombre']} ({pais_mayor_sup['superficie']:,.2f} km²)")
    print(f"🏜️ País con MENOR Superficie: {pais_menor_sup['nombre']} ({pais_menor_sup['superficie']:,.2f} km²)")
    
    print("-" * 30)
    
    # Promedios
    print(f"📊 Promedio de Población: {promedio_poblacion:,.0f} hab.") 
    print(f"🗺️ Promedio de Superficie: {promedio_superficie:,.2f} km²")
    print("-" * 30)
    
    # Conteo
    print("🌍 Cantidad de Países por Continente:")
    # Usamos sorted() para mostrar los continentes alfabéticamente
    for continente, cantidad in sorted(conteo_continentes.items()):
        print(f" - {continente}: {cantidad} países")


def mostrar_paises(lista_paises):

    """Imprime una lista de países en formato de tabla con formato de miles."""

    if not lista_paises:
        # Si la lista está vacía, no imprime nada.
        # El main() o la función que llama se encargan de
        # imprimir "No se encontraron resultados".
        return
        
    # Imprime la cabecera de la tabla
    print("\n| Nombre                                   | Población (hab) | Superficie (km²) | Continente |")
    print("|------------------------------------------|-----------------|------------------|------------|")
    
    # Itera sobre cada país en la lista
    for pais in lista_paises:
        # Formatea los números para mejor legibilidad
        pob_fmt = f"{pais['poblacion']:,}" 
        sup_fmt = f"{pais['superficie']:,.2f}"
        
        # Imprime la fila con alineación
        print(f"| {pais['nombre']:<40} | {pob_fmt:>15} | {sup_fmt:>16} | {pais['continente']:<10} |")
    
    # Imprime la línea final de la tabla
    print("-" * 94)

def mostrar_menu():

    """Muestra el menú de opciones del sistema con un estilo estético y único."""
    
    # --- Definición de Bordes (Ajustados a 53 de ancho) ---
    borde_sup = "╭" + "─" * 53 + "╮"  # <-- Cambiado de 52 a 53
    borde_inf = "╰" + "─" * 53 + "╯"  # <-- Cambiado de 52 a 53
    borde_medio = "├" + "─" * 53 + "┤"  # <-- Cambiado de 52 a 53
    linea_vacia = "│" + " " * 53 + "│"  # <-- Cambiado de 52 a 53
    
    # --- Título ---
    print("\n" + borde_sup)
    print(linea_vacia)
    print("│" + "🌍 GESTIÓN MUNDIAL DE PAÍSES 🌍".center(51) + "│") #
    print("│" + "UTN - Programación 1".center(53) + "│") 
    print(linea_vacia)
    print(borde_medio)

    # --- Opciones del Menú ---
    print(f"│ {'[1] 📥  Cargar Datos (CSV)':<50} │")
    print(f"│ {'[2] 🔎  Buscar por Nombre':<49}  │")
    print(f"│ {'[3] 🌎  Filtrar por Continente':<49}  │")
    print(f"│ {'[4] 👥  Filtrar por Población':<49}  │")
    print(f"│ {'[5] 🗺   Filtrar por Superficie':<50}  │")
    print(f"│ {'[6] 🔀  Ordenar Países':<49}  │")
    print(f"│ {'[7] 📊  Ver Estadísticas':<49}  │")
    print(f"│ {'[8] 📚  Mostrar Lista Completa':<49}  │")
    print(borde_medio)
    
    # --- Opción de Salir ---
    print(f"│ {'[0] ❌  Salir del Programa':<50} │")
    print(borde_inf)