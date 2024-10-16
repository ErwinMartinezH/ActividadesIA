#Actividad6, consta de lo siguiente:
#Arreglos - a una lista de número [10,20,30,40,50] le tienes que poder agregar,
# quitar y modificar (tu decides como pero en si harás un while, if, etc.)

def main():
    lista = [10,20,30,40,50]
    while True:
        print("Lista actual:", lista)
        print("1. Agregar un valor a la lista")
        print("2. Quitar un valor de la lista")
        print("3. Modificar un valor de la lista")
        print("4. Salir")
        opcion = int(input("Ingresa una opción: "))
        if opcion == 1:
            valor = int(input("Ingresa el valor que deseas agregar: "))
            lista.append(valor)
        elif opcion == 2:
            valor = int(input("Ingresa el valor que deseas quitar: "))
            if valor in lista:
                lista.remove(valor)
            else:
                print("El valor no se encuentra en la lista")
        elif opcion == 3:
            valor = int(input("Ingresa el valor que deseas modificar: "))
            if valor in lista:
                indice = lista.index(valor)
                nuevo_valor = int(input("Ingresa el nuevo valor: "))
                lista[indice] = nuevo_valor
            else:
                print("El valor no se encuentra en la lista")
        elif opcion == 4:
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()

