"""
Ejercicio 8. Cuanto es el X por ciento del X numero?
    - 20% de 150
"""

numero = int(input("Introduce el numero: "))
porcentaje = int(input(f"Que porcentaje quieres sacar del {numero} ?: "))

operacion = (numero * (porcentaje/100))

print(f"El {porcentaje}% de {numero} es {operacion}")