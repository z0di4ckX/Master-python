"""
Ejercicio 7. Hacer un programa que muestre todos los numero impares
entre dos numero que decida el usario.
"""

numero1 = int(input("Introduce un numero: "))
numero2 = int(input("Introduce el siguente numero: "))

if numero1 < numero2:

    for x in range(numero1, (numero2 + 1)):

        if x %2 == 0:
            print(f"{x} es par")
        else:
            print(f"{x} es impar")
else:
    print("El numero 1 debe ser meyor a numero 2")