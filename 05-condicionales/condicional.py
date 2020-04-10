# Condicionales

"""
    1. Condicional: if

    Si se_cumple_esta_condicion:
        Ejecutuar grupo de intrucciones
    Si no:
        Se ejecuta otro grupo de instrucciones

    if condicion:
        intrucciones
    else:
        otras instrucciones

    2. Operadores de comparacion

        == igual
        != diferente
        < menor que
        > mayor que
        <=  menor o igual que
        >= mayour o igual que
"""

# Ejemplo 1
print("#########  EJEMPLO 1 #################")

color = "rojo"
# color = "Verde"
# color = input("Adivina cual es mi color favorito: ")

if color == "rojo":
    print("Enhorabuena!!")
    print("Mi color favorito es ROJO")
else:
    print("Color incorrecto!!")

# Ejemplo 2
print("\n#########  EJEMPLO 2 #################")

year = 2020
# year = int(input("En que anos estamos: "))

if year >= 2021:
    print("Estamos de 2021 en adelante!!")
else:
    print("Es un ano aterior a 2021")


# Ejemplos 3
print("\n#########  EJEMPLO 3 #################")

nombre = "Victor Robles"
ciudad = "Barcelona"
continente = "Europa"
edad = 55
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad!!")

    if continente != "Europa":
        print("El usario No es Europes")
    else:
        print(f"Es Europeo y de {ciudad}")

else:
    print(f"{nombre} NO es mayor de edad.")
