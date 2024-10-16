#Actividad 3, consta de lo siguiente:
# Uso de if/else - Pedira una edad y verificara si es mayor de 18 años o no.
#si es mayor de 18 años, se le dira que es mayor de edad.
#si no es mayor de 18 años, se le dira que es menor de edad.
#si es mayor de 59 años, se le dira que es un adulto mayor.

def main():
    print("Por favor ingrese su edad")
    age = int(input())
    if age >= 18:
        print("Ya no usas pañales, excelente :)")
    elif age >= 59:
        print("Chales, ya deberias usar pañales :(")
    else:
        print("Tambien usas pañales, no te preocupes :D")

if __name__ == "__main__":
    main()