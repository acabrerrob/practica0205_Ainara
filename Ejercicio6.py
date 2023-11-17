
def decToBin(decimal):
    """Función que convierte un número decimal a binario.
    Parámetro: decimal = número decimal introducido por el usuario.
    Salida: número decimal convertido en binario
    """

    myBin = bin(decimal).replace('0b', '')
    return myBin

def binToDec(binario):
    """Función que convierte un número binario a decimal.
    Parámetro: binario = número binario introducido por el usuario.
    Salida: número binario convertido en decimal
    """
    
    strbin = str(binario)
    myDec = int(strbin, 2)
    return myDec

