'''
Variables locales: Se definen dentro de la funcion y no se puede usar fuera de ella,
solo estan disponible dentro. A no ser que hagamo un return.

Variables gobales: son las que se declaran fuera de una funcion y estan disponibles dentro y fuera de ellas.
'''

 # Variable global
 frase = "Ni los genios son tan genios"
 print(frase)

#variable local
 def holaMundo():
     frase = "hola mundo"
     print("Dentro de la funcion: ")
     print(frase)
     year = 2021
     print(year)

    global website
    website = "juanruiz.com"
    print("Dentro: ", website)

     return "Dato devuelto" +  str(year)

print(holaMundo())
print("Fuera: ", website)