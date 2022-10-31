#Leer los numeros del usuario,hasta que el usuario ingrese el 0
#Luego mostrar la suma de todos los numeros ingresados
suma=0

while(True):
    A = int(input("Ingrese numeros o de lo contrario [salir con '0'] : "))
    suma = suma + A
    if(A==0):
        break
print("Esta es la suma de los numeros ingresados : ",suma)