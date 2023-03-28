segundos = int(input("Inserta la cantidad de segundos: "))
dias = segundos // (24 * 3600)
horas =  segundos // 3600
segundos_faltantes = segundos % 3600
minutos = segundos_faltantes // 60
segundos_restantes_final = segundos_faltantes % 60

if dias == 0 and horas == 0 and minutos == 0:
    print(segundos, "segundos es equivalente a:")
    print(segundos_restantes_final, "segundos")
elif dias == 0 and horas == 0:
    print(segundos, "segundos es equivalente a:")
    print(minutos, "minutos y ", segundos_restantes_final, "Segundos")
elif dias == 0:
    print(segundos, "segundos es equivalente a:")
    print(horas, "horas ", minutos, "minutos y ", segundos_restantes_final, "segundos")
else:
    print(segundos, "segundos es equivalente a:")
    print(dias, "dias ", horas, "horas ", minutos, "minutos y ", segundos_restantes_final, "segundos" )