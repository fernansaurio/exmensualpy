segundos = int(input("Inserta la cantidad de segundos: "))
horas =  segundos // 3600
segundos_faltantes = segundos % 3600
minutos = segundos_faltantes // 60
segundos_restantes_final = segundos_faltantes % 60

print(f"{segundos}segundos equivalen a:")
print(f"{horas} horas, {minutos} minutos y {segundos_restantes_final} segundos")