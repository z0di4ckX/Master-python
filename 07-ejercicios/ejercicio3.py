"""
Ejercicio 3. Escribir un programa que muestre los cuadrados 
(un numero multiplicado por si mismo) de los 60 primeros numero
naturales. Resolver con "for" y "while".
"""

contador = 0

while contador <= 60:
    cuadrado = contador*contador
    print(f"El cuadrado {contador} es {cuadrado}")
    contador += 1