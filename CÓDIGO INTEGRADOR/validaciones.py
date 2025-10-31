# --- validaciones.py ---
# Este archivo contiene todas las funciones que validan entradas del usuario.

def validar_entero(mensaje):

    """Pide un entero al usuario y lo valida."""

    while True:
        try:
            # Pide el dato al usuario
            entrada = input(mensaje)
            # Intenta convertirlo a entero
            return int(entrada)
        except ValueError:
            # Si la conversión falla, muestra un error y repite el bucle
            print("❌ Entrada inválida. Se esperaba un valor numérico entero❗")

def validar_opcion_menu(mensaje, min_val, max_val):

    """
    Pide un entero (usando validar_entero) y valida que esté 
    dentro de un rango específico [min_val, max_val].
    """
    while True:
        
        # Reutilizamos la función base para asegurarnos de que es un entero
        num = validar_entero(mensaje)
        
        # Validamos el rango específico para el menú
        if min_val <= num <= max_val:
            return num  # El número es válido
        else:
            # Si está fuera de rango, muestra un error y repite el bucle
            print(f"❌ Opción inválida. El número debe estar entre {min_val} y {max_val}.")


def validar_rango_numerico():

    """Pide y valida un rango (mín, máx) asegurando que no sean negativos y min <= max."""

    print("\n--- INGRESO DE RANGO ---")
    while True:

        # Pide los valores mínimo y máximo usando la validación de enteros
        min_val = validar_entero("Ingrese el valor mínimo: ")
        max_val = validar_entero("Ingrese el valor máximo: ")

        # 1. Verifica si alguno de los valores es negativo.
        if min_val < 0 or max_val < 0:
            print("❌ Los valores no pueden ser negativos. Intente de nuevo❗")
            continue 

        # 2. Verifica que el mínimo no sea mayor que el máximo.
        if min_val <= max_val:
            return min_val, max_val # Si todo es correcto, devuelve los valores.
        else:
            print("❌ El valor mínimo no puede ser mayor que el máximo. Intente de nuevo❗")


def validar_string(mensaje):

    """
    Pide un string, valida que NO esté vacío y que NO contenga números.
    Permite espacios y otros caracteres (ej: "Corea del Sur").
    """
    while True:
        # Pide el dato y quita espacios en blanco de los bordes
        entrada = input(mensaje).strip()
        
        # 1. Verifica que la entrada no esté vacía
        if not entrada:
            print("❌ La entrada no puede estar vacía.")
        # 2. Verifica si algún caracter es un dígito
        elif any(char.isdigit() for char in entrada):
            print("❌ La entrada no puede contener números.")
        else:
            # Si pasa ambas validaciones, devuelve la entrada
            return entrada


def validar_texto(texto):

    """
    Pasa a minúsculas y reemplaza las vocales con acento
    por sus equivalentes sin acento.
    """
    texto = texto.lower()
    reemplazos = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
        'ü': 'u'
    }
    
    for acento, sin_acento in reemplazos.items():
        texto = texto.replace(acento, sin_acento)
    return texto