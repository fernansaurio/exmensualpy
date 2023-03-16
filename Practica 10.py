import pandas as pd
Itramo = float(0.01)
IItramo = float(472.1)
IIItramo = float(895.25)
IVtramo = float(2038.11)
ISSS = float(0.03)
AFP = float(0.0725)

des2 = float(0.1)
des3 = float(0.2)
des4 = float(0.3)

sueldo=float(input("escribe tu sueldo: $ "))

if sueldo <Itramo:
 print("No hay isr")
elif sueldo <IItramo:
    resultadodes = (sueldo * des2)
elif sueldo <IIItramo:
    resultadodes = (sueldo * des3)
elif sueldo <IVtramo:

    resultadodes = (sueldo * des4)


resultadoISSS = (sueldo * ISSS)
resultadoAFP = (sueldo * AFP)
resultadototal= (resultadodes+resultadoISSS+resultadoAFP)
total = float(sueldo-resultadototal)

tabla = pd.DataFrame({'--': ['Sueldo', 'Sueldo - ISSS', 'Sueldo - AFP', 'Total del descuento', 'Total del sueldo'],
                      '--': [sueldo, resultadoISSS, resultadoAFP, resultadototal, total],})

print(tabla)
