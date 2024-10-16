#Actividad7, consta de lo siguiente:
#Uso de tuplas - se crea una tupla la cual es [10,20,30]
# y el usuario deberá de adivinar cual es el valor de la tupla.
#el valor de la tupla es 20

def adivinar():
    tupla = (10,20,30)
    while True:
        print("La tupla actual es:", tupla)
        print("Adivina el valor de la tupla")
        valor = int(input())
        if valor == 20:
            print("¡Felicidades, adivinaste el valor de la tupla!")
            break
        else:
            print("Intenta de nuevo")

if __name__ == "__main__":
    adivinar()



