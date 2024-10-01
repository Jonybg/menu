from array_generales import *
from especificas import *
from input import *
lista = []
while True:
    opcion = input("1. Ingresar numeros\n2. Mostrar la cantidad de números positivos y negativos\n3. Mostrar la sumatoria de los números pares\n4. Informar el mayor de los números impares\n5. Listar todos los números ingresados\n6. Listar todos los números pares\n7. Listar los números de las posiciones impares\n8. Salir ")
    match opcion:
        case "1":
            numero = get_int(
                "ingrese un numero(entre -1000 y 1000)", "error", -1000, 1000, 10)
            lista = lista + [numero]
            print(f"Numero {numero} agregado")
        case "2":
            resultado_total = mostrar_total(lista)
            print(f"La cantidad de numeros ingresados, tanto positivos como negativos es de {
                  resultado_total}")
        case "3":
            resultado_suma_pares = sumar_pares(lista)
            print(f"La suma de numeros pares es de: {resultado_suma_pares}")
        case "4":
            resultado_mayor_impares = mayor_impares(lista)
            print(f"El mayor de los impares es de {resultado_mayor_impares}")
        case "5":
            print("La lista de numeros son los siguientes:")
            listar_numeros(lista)
        case "6":
            print("La lista de numeros pares son los siguientes:")
            listar_pares(lista)
        case "7":
            print("La posicion de los numeros impares son las siguientes:")
            posicion_impares(lista)
        case "8":
            print("saliendo...")
            break
        case _:
            print("No eligio una opcion correcta")
    continuar = input("Desea continuar? (s/n): ")
    if continuar != "s" and continuar != "S":
        print("Saliendo....")
        break
