def sumar_pares(lista: list) -> int:
    suma = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            suma += lista[i]
    return suma


def mayor_impares(lista: list) -> int:
    maximo = 0
    for i in range(len(lista)):
        if lista[i] % 2 != 0:
            if lista[i] > maximo:
                maximo = lista[i]
    return maximo


def listar_pares(lista: list) -> None:
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            print(lista[i])
