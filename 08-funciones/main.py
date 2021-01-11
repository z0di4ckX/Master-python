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
'''
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


# Ejemplo 3.1
print("############# Ejemplo 3.1 #########")
for number_tablas in range(1, 11): 
    tabla(number_tablas)  
'''
# Ejemplo 4 
print("############ Ejemplo 4 ############")

# Parametros opcionales

def get_empleado(nombre_del_empleado, dni = None):
    print("EMPLEADO")
    print(f"Nombre: {nombre_del_empleado}")

    if dni != None:
        print(f"ID: {dni}")

get_empleado("Victor Robles", 423245)

# Ejemplo 5, returns o devolver datos

print("\n############ Ejemplo 5 ############")

def saludame(nombres):

    saludo = f"Hola un saludo a {nombres}"

    return(saludo)

print(saludame("Victor"))

# Ejemplo 6
print("\n############ Ejemplo 6 ############")

def calculadora(numero1, numero2, basicos = False):
    
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    divi = numero1 / numero2

    cadena = ""

    if basicos != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicacion: " + str(multi)
        cadena += "\n"
        cadena += "division: " + str(divi)

    return(cadena)

print(calculadora(54, 3))

# Ejemplo 7
print("\n############ Ejemplo 7 ############")

def getNombre(nombre):
    texto = f"El nombre del usario: {nombre}"
    return texto

def getApellido(apellido):
    texto = f"El apellido del usario: {apellido}"
    return texto

def getDevulveTodo(nombre, apellido):
    texto = getNombre(nombre) + "\n" + getApellido(apellido)
    return texto

print(getDevulveTodo("Victor", "Ruz"))