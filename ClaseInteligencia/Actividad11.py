#Actividad 11, consta de lo siguiente:
#Agenda telefónica - Un diccionario que contenga todos los nombres de personas y sus respectivos telefonos, ligados a un ID,
# El usuario podra añadir, modificar, quitar y buscar los respectivos contactos
# El diccionario se guardara en un archivo de texto llamado "A11Agenda.txt"

# Función para leer el archivo y convertirlo a un diccionario
def leer_agenda(archivo):
    agenda = {}
    try:
        with open(archivo, 'r') as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                if ':' in linea:
                    id, nombre, telefono = linea.split(':', 2)
                    agenda[id.strip()] = (nombre.strip(), telefono.strip())
                else:
                    print(f"Formato incorrecto en la línea: {linea}")
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe. Creando un archivo nuevo...")
        open(archivo, 'w').close()
    return agenda

# Función para guardar el diccionario en el archivo
def guardar_agenda(archivo, agenda):
    with open(archivo, 'w') as f:
        for id, (nombre, telefono) in agenda.items():
            f.write(f"{id}:{nombre}:{telefono}\n")

# Función para buscar un contacto en el diccionario
def buscar_agenda(agenda):
    busqueda = input("Ingresa el ID, nombre o teléfono del contacto que deseas buscar: ").strip()
    encontrado = False

    # Búsqueda exacta de ID
    if busqueda in agenda:
        nombre, telefono = agenda[busqueda]
        print(f"ID: {busqueda}\nNombre: {nombre}\nTeléfono: {telefono}\n")
        encontrado = True
    else:
        # Búsqueda por coincidencia parcial en nombre o teléfono
        for id, (nombre, telefono) in agenda.items():
            if busqueda.lower() in nombre.lower() or busqueda == telefono:
                print(f"ID: {id}\nNombre: {nombre}\nTeléfono: {telefono}\n")
                encontrado = True

    if not encontrado:
        print("El contacto no existe en la agenda.")
        if input("¿Deseas agregarlo? (s/n): ").strip().lower() == "s":
            agregar_agenda(agenda)

# Función para agregar un contacto al diccionario
def agregar_agenda(agenda):
    id = str(len(agenda) + 1)
    nombre = input("Ingresa el nombre del contacto: ").strip()
    telefono = input("Ingresa el número celular del contacto (10 dígitos): ").strip()
    while not telefono.isdigit() or len(telefono) != 10:
        print("Número inválido. Debe tener 10 dígitos.")
        telefono = input("Ingresa el número celular del contacto (10 dígitos): ").strip()
    agenda[id] = (nombre, telefono)
    print("Contacto agregado correctamente.")
    guardar_agenda("A11Agenda.txt", agenda)

# Función para modificar un contacto en el diccionario
def modificar_agenda(agenda):
    busqueda = input("Ingresa el ID o el teléfono del contacto que deseas modificar: ").strip()
    encontrado = False

    # Búsqueda por ID exacto
    if busqueda in agenda:
        modificar_contacto(busqueda, agenda)
        encontrado = True
    else:
        # Búsqueda por coincidencia exacta de teléfono
        for id, (nombre, telefono) in agenda.items():
            if busqueda == telefono:
                modificar_contacto(id, agenda)
                encontrado = True
                break

    if not encontrado:
        print("El contacto no existe en la agenda.")

# Subfunción para realizar la modificación del contacto
def modificar_contacto(id, agenda):
    nombre, telefono = agenda[id]
    opcion = input("Ingresa 1 para modificar el nombre o 2 para modificar el teléfono: ").strip()
    if opcion == "1":
        nuevo_nombre = input("Ingresa el nuevo nombre del contacto: ").strip()
        agenda[id] = (nuevo_nombre, telefono)
        print("Nombre modificado correctamente.")
    elif opcion == "2":
        nuevo_telefono = input("Ingresa el nuevo teléfono del contacto (10 dígitos): ").strip()
        while not nuevo_telefono.isdigit() or len(nuevo_telefono) != 10:
            print("Número inválido. Debe tener 10 dígitos.")
            nuevo_telefono = input("Ingresa el nuevo teléfono del contacto (10 dígitos): ").strip()
        agenda[id] = (nombre, nuevo_telefono)
        print("Teléfono modificado correctamente.")
    else:
        print("Opción inválida.")
    guardar_agenda("A11Agenda.txt", agenda)

# Función para eliminar un contacto del diccionario
def eliminar_agenda(agenda):
    busqueda = input("Ingresa el ID o el teléfono del contacto que deseas eliminar: ").strip()
    encontrado = False

    # Búsqueda por ID exacto
    if busqueda in agenda:
        confirmacion = input(f"¿Estás seguro de que deseas eliminar el contacto {agenda[busqueda][0]}? (s/n): ").strip().lower()
        if confirmacion == "s":
            del agenda[busqueda]
            print("Contacto eliminado correctamente.")
            guardar_agenda("A11Agenda.txt", agenda)
        else:
            print("Eliminación cancelada.")
        encontrado = True
    else:
        # Búsqueda por coincidencia exacta de teléfono
        for id, (nombre, telefono) in agenda.items():
            if busqueda == telefono:
                confirmacion = input(f"¿Estás seguro de que deseas eliminar el contacto {nombre}? (s/n): ").strip().lower()
                if confirmacion == "s":
                    del agenda[id]
                    print("Contacto eliminado correctamente.")
                    guardar_agenda("A11Agenda.txt", agenda)
                else:
                    print("Eliminación cancelada.")
                encontrado = True
                break

    if not encontrado:
        print("El contacto no existe en la agenda.")

# Función principal
def agenda_telefonica():
    agenda = leer_agenda("A11Agenda.txt")
    while True:
        print("\nAgenda Telefónica")
        print("1. Buscar Contacto")
        print("2. Agregar Contacto")
        print("3. Modificar Contacto")
        print("4. Eliminar Contacto")
        print("5. Salir")
        opcion = input("Ingresa una opción (1-5): ").strip()
        if opcion == "1":
            buscar_agenda(agenda)
        elif opcion == "2":
            agregar_agenda(agenda)
        elif opcion == "3":
            modificar_agenda(agenda)
        elif opcion == "4":
            eliminar_agenda(agenda)
        elif opcion == "5":
            guardar_agenda("A11Agenda.txt", agenda)
            print("Agenda guardada correctamente. Saliendo...")
            break
        else:
            print("Opción inválida. Por favor, ingresa un número entre 1 y 5.")

# Ejecuta la función principal
agenda_telefonica()
