# Actividad8, consta de lo siguiente:
# Uso de diccionario - Un diccionario de alumnos con sus respectivas notas,
# El usuario podra añadir, modificar y quitar las respectivas notas.
# La informacion del diccionario se guardara en un archivo de texto.

import os


def buscar_alumno(diccionario):  # Toma la informacion en alumno.txt
    nombre = input("Ingresa el nombre del alumno: ")
    if nombre in diccionario:
        print("La nota del alumno es:", diccionario[nombre])
    else:
        print("El alumno no existe")


def mostrar_alumnos(diccionario):  # Toma la informacion en A8Alumnos.txt e imprime el diccionario
    with open("A8Alumnos.txt", "r") as f:
        for line in f:
            if line.strip():
                info = line.split(",")
                diccionario[info[0]] = float(info[1])
    for clave, valor in diccionario.items():
        print(clave, valor)

def main():
    diccionario = {}
    while True:
        print("______________________________")
        print("|1. Mostrar todos los alumnos|")
        print("|2. Buscar un alumno         |")
        print("|3. Salir                    |")
        print("______________________________")
        opcion = int(input("Ingresa una opción: "))
        if opcion == 1:
            mostrar_alumnos(diccionario)
        elif opcion == 2:
            buscar_alumno(diccionario)
        elif opcion == 3:
            break
        else:
            print("Opción inválida")
    print("Gracias por usar el programa")


if __name__ == "__main__":
    main()
