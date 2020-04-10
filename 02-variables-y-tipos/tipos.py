# Tipos de datos en python

nada = None
cadena = "Hola soy juan del pueblo"
entero = 22
flotante = 44.2
booleano = True
lista = [12, 23, 111, 200]
listaString = [22, "treinta", 30, "cuarenta"]
tuplaNoCambia = ("Master", "en", "python")
diccionario = {
    "nombre": "Victor",
    "apellidos": "Robles",
    "curos": "Master en Python"
}
rango = range(8)
datos_byte = b"Probando"

# imprimir la variables
print(nada)

# Mostrar typo de datos
print(type(nada))

# Convertir de un tipo de dato a otro

texto = "Hola soy un texto"
numerito = str(33)
print(texto + " " + numerito)

numerito = int(33)
print(type(numerito))

numerito = float(33)
print(type(numerito))