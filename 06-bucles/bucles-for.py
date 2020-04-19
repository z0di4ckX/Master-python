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