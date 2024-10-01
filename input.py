from validate import *


def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> None:
    print(mensaje)
    intentos = 0
    while intentos < reintentos:
        numero = input("Número: ")
        numero = int(numero)
        if validate_number(numero, minimo, maximo):
            print(mensaje_error)
            intentos += 1
            if intentos == reintentos:
                return None
        else:
            print("Número válido")
            return numero


def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: float) -> None:
    print(mensaje)
    intentos = 0
    while intentos < reintentos:
        numero = input("Número: ")
        numero = float(numero)
        if validate_number(numero, minimo, maximo) and numero != float:
            print(mensaje_error)
            intentos += 1
            if intentos == reintentos:
                return None
        else:
            print("Número válido")
            return numero


def get_string(longitud: int) -> str | None:
    cadena = input("ingrese una cadena:")
    if validate_length(longitud, cadena):
        print(f"la cadena debe tener {longitud} caracteres")
        cadena = input("ingrese una cadena:")
    return cadena
