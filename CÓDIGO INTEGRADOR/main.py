# --- main.py ---
# Este es el archivo principal que ejecuta el programa.
# Su única responsabilidad es manejar el menú y llamar a las funciones.

# Importa el módulo 'funciones' (lógica) y le da el alias 'fn'
import funciones as fn

# Importa el módulo 'validaciones' y le da el alias 'val'
import validaciones as val

def main():

    """Función principal: Controla el flujo de la aplicación."""
    
    # Define el nombre del archivo a cargar
    nombre_archivo_csv = "paises.csv"

    # Inicializa la lista principal de datos (vacía al inicio)
    datos_paises = []
    
    # Bucle principal del menú (se repite hasta que opcion == 0)
    while True:
        # 1. Muestra el menú de opciones
        fn.mostrar_menu()
        
        # 2. Pide y valida la opción del usuario
        opcion = val.validar_opcion_menu("➡️  Seleccione una opción (0-8): ", 0, 8)
        print() 
 
        # 3. Lógica principal (evalúa la opción)
        if opcion == 0:
            # Opción 0: Salir

            print("👋 Saliendo del sistema de Gestión de Datos de Países... ¡Hasta pronto!")
            break
        
        elif opcion == 1:
            # Opción 1: Cargar datos

            datos_paises = fn.cargar_datos(nombre_archivo_csv)
            if datos_paises:
                print(f"✅✍️ Se cargaron {len(datos_paises)} países exitosamente.")
        
        # 4. Control: Verifica si los datos están cargados para las opciones 2-8
        elif not datos_paises and opcion != 1:
            print("⚠️ Debe ejecutar la opción 1 (Cargar datos) antes de realizar cualquier consulta.")
        
        # 5. Funcionalidades (requieren datos cargados)
        elif opcion == 2:
            # Opción 2: Buscar por nombre

            fn.buscar_por_nombre(datos_paises)
            
        elif opcion == 3:
            # Opción 3: Filtrar por continente
            
            resultados = fn.filtrar_por_continente(datos_paises)
            if resultados:
                fn.mostrar_paises(resultados)
            else:
                print("ℹ️ No se encontraron países para ese continente.")
            
        elif opcion == 4:
            # Opción 4: Filtrar por población

            resultados = fn.filtrar_por_rango(datos_paises, 'poblacion')
            if resultados:
                fn.mostrar_paises(resultados)
            else:
                print("ℹ️ No se encontraron países en ese rango de población.")
            
        elif opcion == 5:
            # Opción 5: Filtrar por superficie

            resultados = fn.filtrar_por_rango(datos_paises, 'superficie')
            if resultados:
                fn.mostrar_paises(resultados)
            else:
                print("ℹ️ No se encontraron países en ese rango de superficie.")
            
        elif opcion == 6:
            # Opción 6: Ordenar países

            fn.ordenar_paises(datos_paises)
            
        elif opcion == 7:
            # Opción 7: Mostrar estadísticas

            fn.mostrar_estadisticas(datos_paises)
            
        elif opcion == 8:
            # Opción 8: Mostrar todos

            print("\n--- LISTADO COMPLETO DE PAÍSES ---")
            fn.mostrar_paises(datos_paises)
            

# main() solo se ejecuta cuando corres este archivo (main.py) directamente.
if __name__ == "__main__":
    main()