""" 
Una variables es un contenedor de informacion
que dentro guardara un dato, se pueden crear
muchas variables y que cada una tenga un dato distinto.
"""

# Crear variable y darle un valor
texto = "Master en python"
texto2 = "con juan lopez"
numero = 45
decimal = 4.2

# mostrar valor de los variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print("----------------")

# Sustituir el valor de algunos variables / reasignar valores
numero = 88
decimal = 6.2

print(numero)
print(decimal)

print("---------------------")
# Concatenacion
nombre = "Victor"
apellidos = "Robles"
web = "victorroblesweb.com"

print(nombre + " " + apellidos + " " + web)
print(f"{nombre} {apellidos} - {web}")
print("Hola me llamo {} {} y mi web es: {}".format(nombre, apellidos, web))