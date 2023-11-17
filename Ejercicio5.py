def squared(numbers):
    """Función que a partir de una lista introducida saca otra con los valores de la primera elevados al cuadrado.
    Parámetro: numbers = lista de números introducidos por el usuario.
    Salida: lista de números elevados al cuadrado.
    """
    
    squaredNumbers = []
    for x in numbers:
        squaredNumbers.append(x**2)
    return squaredNumbers