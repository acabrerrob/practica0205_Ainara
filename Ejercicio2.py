def factorial(number) :
     """Función recursiva que devuelve el factorial de un número.
    Parámetro: number = número entero positivo.
    Salida: un número entero positivo que es el factorial del número introducido.
    """
     if number == 0 :
         return 1
     else :
         return number * factorial(number-1)
   
def factorialIt (n):
    """Función que devuelve el factorial de un número.
    Parámetro: n = número entero positivo.
    Salida: un número entero positivo que es el factorial del número introducido.
    """
    
    if n == 0 or n == 1:
        return 1
    else:
        myNum = 1
        while n > 1:
            myNum *= n
            n-=1
        return myNum
