pulg_cm = float(2.54)
cm_pulg = float(0.3937007874015748031496062992126)
print("Elige el valor a convertir")
print("1. Centimetros")
print("2. Pulgadas")

type1 = (input(''))

print("Escribe la cantidad a convertir")
val = (float(input('')))

if type1 == '1':
    result = (val * cm_pulg)
elif type1 == '2':
    result = (val * ulg_cm)
else:
    print("Valor invalido")

print("El resultado de la conversion es", result)
