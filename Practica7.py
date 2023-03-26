segundos = int(input("Inserta la cantidad de segundos: "))
horas =  segundos // 3600
segundos_faltantes = segundos % 3600
minutos = segundos_faltantes // 60
segundos_restantes_final = segundos_faltantes % 60

print(segundos, "segundos es equivalente a:")
print(horas, "horas ", minutos, "minutos y ", segundos_restantes_final, "segundos" )