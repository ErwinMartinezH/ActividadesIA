#Actividad9, consta de lo siguiente:
#Uso de diccionario - Un diccionario que contenga todos los estados de México
# y en cada uno de ellos contenga 3 municipios,
# y que el usuario pueda buscar un estado con sus municipios,
# pueda añadir un municipio a un estado y pueda eliminar un municipio de un estado

#El diccionario se guardara en un archivo de texto llamado "A9Estados.txt"

## Función para leer el archivo y convertirlo a un diccionario
def leer_estados_archivo(archivo):
    estados_municipios = {}
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
                    estado, municipios_str = linea.split(':', 1)
                    municipios = [m.strip() for m in municipios_str.split(',')]
                    estados_municipios[estado.strip()] = municipios
                else:
                    print(f"Formato incorrecto en la línea: {linea}")
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe.")
    return estados_municipios

# Función para guardar el diccionario en el archivo
def guardar_estados_archivo(archivo, estados_municipios):
    with open(archivo, 'w') as f:
        for estado, municipios in estados_municipios.items():
            f.write(f"{estado}: {', '.join(municipios)}\n")

# Función para buscar un estado y mostrar sus municipios
def buscar_estado(estados_municipios, estado):
    estado = estado.strip()
    if estado in estados_municipios:
        print(f"Municipios de {estado}: {', '.join(estados_municipios[estado])}")
    else:
        print(f"El estado {estado} no está en la lista.")

# Función para añadir un municipio a un estado
def agregar_municipio(estados_municipios, estado, municipio):
    estado = estado.strip()
    municipio = municipio.strip()
    if estado in estados_municipios:
        if municipio not in estados_municipios[estado]:
            estados_municipios[estado].append(municipio)
            print(f"Municipio {municipio} añadido al estado {estado}.")
        else:
            print(f"El municipio {municipio} ya existe en {estado}.")
    else:
        print(f"El estado {estado} no está en la lista.")

# Función para eliminar un municipio de un estado
def eliminar_municipio(estados_municipios, estado, municipio):
    estado = estado.strip()
    municipio = municipio.strip()
    if estado in estados_municipios:
        if municipio in estados_municipios[estado]:
            estados_municipios[estado].remove(municipio)
            print(f"Municipio {municipio} eliminado del estado {estado}.")
        else:
            print(f"El municipio {municipio} no está en {estado}.")
    else:
        print(f"El estado {estado} no está en la lista.")

# Ejemplo de uso
archivo = 'A9Estados.txt'

# Cargar el archivo en un diccionario
estados_municipios = leer_estados_archivo(archivo)

# Menú interactivo
while True:
    print("\n1. Buscar estado")
    print("2. Añadir municipio")
    print("3. Eliminar municipio")
    print("4. Guardar y salir")
    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        estado = input("Introduce el nombre del estado: ")
        buscar_estado(estados_municipios, estado)

    elif opcion == '2':
        estado = input("Introduce el nombre del estado: ")
        municipio = input("Introduce el nombre del municipio a añadir: ")
        agregar_municipio(estados_municipios, estado, municipio)

    elif opcion == '3':
        estado = input("Introduce el nombre del estado: ")
        municipio = input("Introduce el nombre del municipio a eliminar: ")
        eliminar_municipio(estados_municipios, estado, municipio)

    elif opcion == '4':
        guardar_estados_archivo(archivo, estados_municipios)
        print("Cambios guardados. Saliendo...")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")


