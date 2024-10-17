# Diccionario de 5 palabras cada una con un significado.
# El usuario podra: Añadir, Modificar, Eliminar y Buscar
# Si la palabra no se encuentra en el diccionario preguntara si desea agregarla

# El diccionario se guardara en un archivo de texto llamado "A10Diccionario.txt"
# El archivo "A10Diccionario.txt" podra ser leido y podra ser modificado

def leer_diccionario(archivo):
    diccionario = {}
    try:
        with open(archivo, 'r') as f:
            for linea in f:
                # Elimina espacios en blanco al inicio o al final de la línea
                linea = linea.strip()
                # Ignorar líneas vacías
                if not linea:
                    continue
                # Asegurarse de que la línea contiene el carácter ":"
                if ':' in linea:
                    clave, significado = linea.split(':', 1)
                    diccionario[clave.strip()] = significado.strip()
                else:
                    print(f"Formato incorrecto en la línea: {linea}")
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe.")
    return diccionario

def guardar_diccionario(archivo, diccionario):#guardará el diccionario en UTF-8 para español latino
    with open(archivo, 'w', encoding='utf-8') as f:
        for clave, significado in diccionario.items():
            f.write(f"{clave}:{significado}\n")

def agregar_palabra(diccionario):
    clave = input("Ingresa la clave de la palabra: ")
    significado = input("Ingresa el significado de la palabra: ")
    diccionario[clave] = significado
    print("Palabra agregada correctamente.")
    #Guardar el diccionario en el archivo
    guardar_diccionario("A10Diccionario.txt", diccionario)

def modificar_palabra(diccionario):
    clave = input("Ingresa la clave de la palabra que deseas modificar: ")
    if clave in diccionario:
        significado = input("Ingresa el nuevo significado de la palabra: ")
        diccionario[clave] = significado
        print("Palabra modificada correctamente.")
    else:
        print("La palabra no existe en el diccionario.")
    #Guardar el diccionario en el archivo
    guardar_diccionario("A10Diccionario.txt", diccionario)

def eliminar_palabra(diccionario):
    clave = input("Ingresa la clave de la palabra que deseas eliminar: ")
    if clave in diccionario:
        del diccionario[clave]
        print("Palabra eliminada correctamente.")
        #Guardar el diccionario en el archivo
        guardar_diccionario("A10Diccionario.txt", diccionario)
    else:
        print("La palabra no existe en el diccionario.")

def buscar_palabra(diccionario):
    clave = input("Ingresa la clave de la palabra que deseas buscar: ")
    if clave in diccionario:
        print(f"Significado de '{clave}': {diccionario[clave]}")
    else:
        print("La palabra no existe en el diccionario. ¿Deseas agregarla?(s/n)")
        respuesta = input()
        if respuesta.lower() == 's':
            significado = input("Ingresa el significado de la palabra: ")
            diccionario[clave] = significado
            print("Palabra agregada correctamente.")
            #Guardar el diccionario en el archivo
            guardar_diccionario("A10Diccionario.txt", diccionario)
        else:
            print("La palabra no existe en el diccionario.")

def imprimir_diccionario(diccionario):
    for clave, significado in diccionario.items():
        print(f"{clave}: {significado}")

def main():
    archivo = "A10Diccionario.txt"
    diccionario = leer_diccionario(archivo)
    while True:
        print("______________________________")
        print("|1. Agregar palabra          |")
        print("|2. Modificar palabra        |")
        print("|3. Eliminar palabra         |")
        print("|4. Buscar palabra           |")
        print("|5. Imprimir diccionario     |")
        print("|6. Salir                    |")
        print("______________________________")
        opcion = int(input("Ingresa una opción: "))
        if opcion == 1:
            agregar_palabra(diccionario)
        elif opcion == 2:
            modificar_palabra(diccionario)
        elif opcion == 3:
            eliminar_palabra(diccionario)
        elif opcion == 4:
            buscar_palabra(diccionario)
        elif opcion == 5:
            imprimir_diccionario(diccionario)
        elif opcion == 6:
            break
        else:
            print("Opción inválida")
    print("Gracias por usar el programa")
    guardar_diccionario(archivo, diccionario)

if __name__ == "__main__":
    main()

