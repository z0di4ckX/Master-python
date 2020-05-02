"""
FUNCIONES:
Una funcion es un conjunto de instruciones agrupada bajo
un nombre concreto que pueden reutilizarse invocando a 
la funcion tantas veces como sea necesario.

def nombre_De_Mi_Funcion(parametro):
    #BLOQUE / CONJUTO DE INSTRUCIONES

nombre_De_Mi_Funcion(mi_parametro)
"""
# Ejemplo 1
print("############ Ejemplo 1 ############")

def muestra_nombre():
    print("Victor")
    print("Paco")
    print("Juna")
    print("Carlos")
    print("Miquel")
    print("\n")


# Invocar Funcion
muestra_nombre()

# Ejemplo 2 parametros
print("############ Ejemplo 2 ############")

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))

def mostrar_tu_nombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Y eres mayor de edad")

mostrar_tu_nombre(nombre, edad)

# Ejemplo 3 
print("############ Ejemplo 3 ############")

numero = int(input("Introduce un numero: "))

def tabla(numero):
    print(f"Tabla de multiplicar del numero: {numero}")

    for contador in range(11):
        operacion = numero*contador
        print(f"{numero} X {contador} = {operacion}")
    
    print("\n")

tabla(numero)
