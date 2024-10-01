def validate_number(numero, mínimo, máximo):
    return numero < mínimo or numero > máximo


def validate_length(cadena, longitud_esperada):
    return len(cadena) != longitud_esperada
