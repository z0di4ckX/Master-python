""" 
#For

for variable in elemento_interactivo (lista, rango, etc)
    BLOQUE DE INSTRUCIONES

"""

contador = 0
resultado = 0

for contador in range(0, 10):
    print("Voy por el " + str(contador))

    resultado += contador

print(f"El resultado es: {resultado}")


# Ejemplo con tablas de multiplicar
print("\n########## EJEMPLO ##################")

numero_usario = int(input("De que numero quieres la tabla de multipicar: "))

if numero_usario < 1:
    numero_usario = 1

print(f"#### Tabla de multiplicar del numero {numero_usario} ####")

for numero_tabla in range(1, 11):
    print(f"{numero_usario} X {numero_tabla} = {numero_usario*numero_tabla}")
else:
    print("Tabla finalizada!!")