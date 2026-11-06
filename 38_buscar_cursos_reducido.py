import datetime as dt
import streamlit as st
cursos=[
    {"denominacion":"Python y datos","calificaciones":[5.6,7.8,3.3,7.2],"fecha_fin":"10/03/2026"},
    {"denominacion":"Inglés científico","calificaciones":[8.2,7.8,6.3,4.2,9.0],"fecha_fin":"22/07/2026"},
    {"denominacion":"Spring e hibernate","calificaciones":[5.8,4.3,7.5],"fecha_fin":"04/12/2025"},
    {"denominacion":"Programador cerficado","calificaciones":[7.8,6.6,4.8,5.3,7.7],"fecha_fin":"30/09/2025"}  
]
#Nombre del curso con la nota media más alta
#Nombre del curso que finalizó antes
#lo mas reducida posible

menor=min(cursos, key=lambda c:dt.datetime.strptime(c["fecha_fin"],"%d/%m/%Y"))
print(f"El curso más antiguo es {menor["denominacion"]}")
    
mayor = max(cursos, key=lambda c:sum(c["calificaciones"]) / len(c["calificaciones"]))
print(f"El curso con la media más alta es {mayor}")