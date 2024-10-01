def mostrar_total(lista: list) -> int:
    contador = 0
    for i in range(len(lista)):
        contador += 1
    return contador


def listar_numeros(lista: list) -> None:
    for i in range(len(lista)):
        print(lista[i])


def listar_pares(lista: list) -> None:
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            print(lista[i])


def posicion_impares(lista: list) -> None:
    posicion = 0
    for i in range(len(lista)):
        if lista[i] % 2 != 0:
            posicion = i
            print(posicion)
