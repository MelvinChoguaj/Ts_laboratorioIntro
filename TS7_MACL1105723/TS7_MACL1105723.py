#Introduccion a la programación
#21/09/2023
#Melvin Choguaj
#Aprender a programar utilizando

print("Melvin Alejandro Choguaj Letona")
z=(1)

while z ==1:
    print("¿Desea generar una tabla de multiplicar con un numero?")
    print("1: si")
    print("2: no, salir")
    op=input()
    op=int(op)

    if op==1:

        x=input("Ingrese un numero del 1 al 10")
        x=int(x)
        y=1
        y=int(y)
        if x >10:
            print("El numero ingresado es mayor a 10")

        elif x<1:
            print("El numero ingresado es menor a 1")

        else: 
            for y in range(1,11):

                print(str(x)+"x"+str(y)+"="+str(x*y))
    
    else:
        break
