import math

def circleArea(radio) :
    """Función que calcula el area de un círculo.
    Parámetro: radio = número real positivo correspondiente al radio del círculo.
    Salida: el área del circulo especificado."""
    return math.pi * radio**2



def cylinderVolume(radio, altura) :
    """Función que calcula el volumen de un cilindro.
    Parámetro: radio = número real positivo correspondiente al radio del círculo.
                altura = número real positivo correspondiente a la altura del cilindro.
    Salida: el volumen del cilindro especificado."""
    return altura * circleArea(radio)