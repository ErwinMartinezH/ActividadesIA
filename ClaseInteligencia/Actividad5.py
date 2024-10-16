#Actividad5, consta de lo siguiente:
#Uso de while - que se vayan sumando los números que se vayan ingresando,
# se irá preguntando si quiere ir agregando y al final se manda el resultado de la suma.

def main():
    suma = 0
    while True:
        n = int(input("Ingresa un numero (0 para terminar): "))
        if n == 0:
            break
        suma += n
    print("La suma es:", suma)

if __name__ == "__main__":
    main()