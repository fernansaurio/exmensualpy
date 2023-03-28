segundos = int(input("Inserta la cantidad de segundos: "))
dias = segundos // (24 * 3600)
horas =  segundos // 3600
segundos_faltantes = segundos % 3600
minutos = segundos_faltantes // 60
segundos_restantes_final = segundos_faltantes % 60

print(segundos, "segundos es equivalente a:")
print(dias, "dias ", horas, "horas ", minutos, "minutos y ", segundos_restantes_final, "segundos" )