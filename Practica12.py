v1 = float(input("Introduce tu primer número: "))
v2 = float(input("Introduce tu segundo número: "))

opcion = 0
while True:
    print("""Dime, ¿qué quieres hacer?

    1) Sumar los dos números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) Cambiar los números elegidos
    5) Terminar""")

    opcion = int(input("Elige una opción: ") )     

    if opcion == 1:
        print(" ")
        print("RESULTADO: La suma de",v1,"+",v2,"es igual a",v1+v2)
    elif opcion == 2:
        print(" ")
        print("RESULTADO: La resta de",v1,"-",v2,"es igual a",v1-v2)
    elif opcion == 3:
        print(" ")
        print("RESULTADO: El producto de",v1,"*",v2,"es igual a",v1*v2)
    elif opcion == 4:
        v1 = float(input("Introduce tu primer número: ") )
        v2 = float(input("Introduce tu segundo número: ") )
    elif opcion == 5:
        break
    else:
        print("Opción incorrecta")
