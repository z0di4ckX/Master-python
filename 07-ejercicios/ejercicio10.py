"""
Ejercicio 10. El programa tiene que pedir la nota de 15 alumons
y sacar por pantalla cuantos han aporbado y cuando han suspendidos. 
"""

contador = 1
aprobados = 0
suspendios = 0

numero_alumnos = int(input("Cuantos alumnos tienes?: "))

while contador <= numero_alumnos:
    nota = int(input(f"Que nota quieres ponerle al \"alumno {contador}\" ? "))

    if nota >= 5:
        aprobados += 1
    else:
        suspendios += 1

    contador += 1

print(f"Alumnos aporbados: {aprobados}")
print(f"Alumons suspensos: {suspendios}")