"""
Ejercicio 3. Escribir un programa que muestre los cuadrados 
(un numero multiplicado por si mismo) de los 60 primeros numero
naturales. Resolver con "for" y "while".
"""

# WHILE

contador = 0

while contador <= 60:
    cuadrado = contador*contador
    print(f"El cuadrado {contador} es {cuadrado}")
    contador += 1


print("#######################################")

# FOR

for numero in range(61):
    cuadrado = numero*numero
    print(f"El cuadrado {numero} es {cuadrado}")