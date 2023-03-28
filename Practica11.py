metros_cubicos = int(input("Ingrese la cantidad de metros cúbicos consumidos: "))

if metros_cubicos <= 0:
    print("Error")
elif metros_cubicos <= 18:
    cantidad_pagar = 6
elif metros_cubicos <= 28:
    cantidad_pagar = 6 + (metros_cubicos - 18) * 0.45
else:
    cantidad_pagar = 6 + 4.5 + (metros_cubicos - 28) * 0.65

print("La cantidad a pagar es de:", cantidad_pagar, "dólares")
