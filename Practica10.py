import pandas as pd

ISSS = 0.03
AFP = 0.0725

def calcular_descuentos(sueldo):
    if sueldo <= 0:
        raise ValueError("El sueldo debe ser mayor que cero.")
    elif sueldo <= 472.01:
        descuento_retencion = 0
    elif sueldo <= 895.24:
        descuento_retencion = sueldo * 0.1
    elif sueldo <= 2038.10:
        descuento_retencion = sueldo * 0.2
    else:
        descuento_retencion = sueldo * 0.3

    descuento_ISSS = sueldo * ISSS
    descuento_AFP = sueldo * AFP
    total_descuentos = descuento_ISSS + descuento_AFP + descuento_retencion
    sueldo_neto = sueldo - total_descuentos
    
    return [descuento_retencion, descuento_ISSS, descuento_AFP, total_descuentos, sueldo_neto]

sueldo = float(input('Ingrese el sueldo: '))

try:
    descuentos = calcular_descuentos(sueldo)
    tabla = pd.DataFrame({
        'Sueldo': [sueldo],
        'Retención': [descuentos[0]],
        'Sueldo - ISSS': [descuentos[1]],
        'Sueldo - AFP': [descuentos[2]],
        'Total del descuento': [descuentos[3]],
        'Total del sueldo': [descuentos[4]],
    })

    print(tabla)
    
except ValueError as error:
    print("Error")