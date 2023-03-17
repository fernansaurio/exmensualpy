kw = float(0.158)
print("Elige el valor a convertir")
print("1. kw")

type1 = (input(''))

print("Escribe los kw a pagar:")
precio = (float(input('')))

if type1 == '1':
    result = (precio * kw)

print("El precio a pagar es", result)