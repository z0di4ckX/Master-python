"""
Ejercicio 2. Escribir un script que nos muestre por pantalla 
todos los numero pares del 1 al 120
"""

for contador in range(1, 121):
    if contador%2 == 0:
        print(f"{contador} es par")
    """
    else:
        print(f"{contador} es impar")
    """