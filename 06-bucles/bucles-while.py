"""
# BUCLE WHILE
Estructura de control que intera o repite la ejecucion de una 
serie de instrucciones tantas veces como sea necesario, 
hasta que deje de cumplirse la condicion. 

while condicion:
    bloque de instruciones
    actualizacion del contador.

"""

contador = 1

while contador <= 100:
    print(f"Estoy en el numero: {contador}")
    contador += 1

print("=============================")

contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    contador += 1

print(muestrame)


print("============ Ejemplo 2 ============")

numero_usario = int(input("De que numero quiere la tabla?: "))

if numero_usario < 1:
    numero_usario = 1

print(f"##### Tabala del {numero_usario} ####")

contador = 1
while contador <= 10:
    print(f"{numero_usario} X {contador} = {numero_usario*contador}")
    contador += 1
else:
    print("Tabla terminada")