nombre = "Victor Robes"

#Funcion general
print(type(nombre))

# Detectar el tipado
comprobar = isinstance(nombre, str)

if comprobar:
    print("Esa variable es un string")
else:
    print("Esa variable no es una string")

if not isinstance(nombre, float):
    print("La variable no es un numero con decimales")

# Limpiar espacios
frase = "   mi contendio   "
print(frase)
print(frase.strip())