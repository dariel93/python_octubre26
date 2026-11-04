import datetime as dt
import streamlit

"""print(f"fecha de hoy: {dt.date.today()}")
print(f"hora acutal: {dt.datetime.now()}")
f_posterior=dt.datetime.now()+dt.timedelta(days=20,hours=60)

print(f_posterior)

fechahora_actual=dt.datetime.now()
print(f"La fecha y hora actuales {dt.datetime.strftime(fechahora_actual,'%d/%m/%y - %H:%M')}")

fecha1="10/11/2003"
fecha2="25/04/2002"
fecha1=dt.datetime.strptime(fecha1,"%d/%m/%Y")
fecha2=dt.datetime.strptime(fecha2,"%d/%m/%Y")
if fecha1<fecha2:
    print(f"la mas antigua es {fecha1}")
else:
    print(f"la mas antigua es {fecha2}")"""
    
# Ejercicio 1

cursos=[
    {"denominacion":"Python y datos","calificaciones":[5.6,7.8,3.3,7.2],"fecha_fin":"10/03/2026"},
    {"denominacion":"Inglés científico","calificaciones":[8.2,7.8,6.3,4.2,9.0],"fecha_fin":"22/07/2026"},
    {"denominacion":"Spring e hibernate","calificaciones":[5.8,4.3,7.5],"fecha_fin":"04/12/2025"},
    {"denominacion":"Programador cerficado","calificaciones":[7.8,6.6,4.8,5.3,7.7],"fecha_fin":"30/09/2025"}  
] 

# Nombre del curso con la nota media mas alta

mejor_curso = ""
mejor_media = 0

for curso in cursos:
    suma = 0
    for nota in curso["calificaciones"]:
        suma = suma + nota
    media = suma/len(curso["calificaciones"])
    if media>mejor_media:
        mejor_media=media
        mejor_curso=curso["denominacion"]

streamlit.write(f"Nombre del curso con la nota media más alta: {mejor_curso}")
streamlit.write(f"Nota media:", mejor_media)
    
# Nombre del curso que finalizo antes

"""curso_anterior = ""
fecha_anterior = ""

for curso in cursos:
    fecha = curso["fecha_fin"]

    dia = int(fecha[0:2])
    mes = int(fecha[3:5])
    anio = int(fecha[6:10])

    if fecha_anterior == "":
        fecha_anterior = fecha
        curso_anterior = curso["denominacion"]
    else:
        dia_anterior = int(fecha_anterior[0:2])
        mes_anterior = int(fecha_anterior[3:5])
        anio_anterior = int(fecha_anterior[6:10])

        if anio < anio_anterior:
            fecha_anterior = fecha
            curso_anterior = curso["denominacion"]
        elif anio == anio_anterior and mes < mes_anterior:
            fecha_anterior = fecha
            curso_anterior = curso["denominacion"]
        elif anio == anio_anterior and mes == mes_anterior and dia < dia_anterior:
            fecha_anterior = fecha
            curso_anterior = curso["denominacion"]

print("Nombre del curso que finalizó antes:", curso_anterior)
print("Fecha de finalización:", fecha_anterior)"""

