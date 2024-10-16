#Actividad4, consta de lo siguiente:
#Uso de for - preguntar por una tabla de
#multiplicar y mandarla a imprimir, se debe pedir igual hasta donde quiere su tabla de multiplicar

def multiplicar():
    a = int(input("Ingresa la tabla de multiplicar: "))
    b = int(input("Ingresa hasta donde quieres la tabla: "))
    for i in range(1, b+1):
        print(a, "x", i, "=", a*i)

multiplicar()
