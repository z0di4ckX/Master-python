"""
Ejercicio 9. Hacer un programa que pida numeros al usario 
indefinidamente hasta meter el numero 111
"""

contador = 1
while contador < 100:
    numero = int(input("Introduce el numero: "))

    if numero == 111:
        break
    else: 
        print(f"Has introducido el {numero}")