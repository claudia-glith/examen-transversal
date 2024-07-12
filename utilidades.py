import random 
import csv
import math

trabajadores =["Juan Perez","Maria Garcia","Carlos lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez",
               "Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]
sueldos=[]

def asignar_sueldos():
    global sueldos 
    sueldos = [random.randint(300000, 2500000)for_in range (10)]
    print("sueldos asignados correctamente.")

def clsificar_sueldos()
    clsificaciones=[]
    for sueldo in sueldos:
        if sueldo < 1000000:
            clasificaciones.append("bajo")
        elif sueldo < =2000000:
            clasificaciones.append("medio")
        else:
            clasificaciones.append("alto")

    for trabajador,sueldo,clasificacion in zip (trabajadores,sueldos,clasificaciones):
        print(f"{trabajador}:${sueldo}-{clsificacion}")

def ver_estadisticas():
    if not sueldos :
        print("primero debe asignar los sueldos .")
        return

    sueldo_mas_alto=int(round(max(sueldos)))
    promedio_sueldos =int(round(sub(sueldos)/len(sueldos)))
media_geometrica=int(round(math.exp(sum(math.log(sueldo)for sueldo in sueldos)/len (sueldos))))

print(f"sueldo mas alto:${sueldo_mas_alto}")
print(f"sueldo mas bajo:${sueldo_mas bajo}")
print(f"promedio de sueldos:${promedio_sueldos:.2f}")
print(f"media geometrica de sueldos:${media_geometrica:.2f}")

def reporte_sueldos():
    reporte =[]
    for trabajador,sueldo in zip(trabajdores,sueldos):
        descuento_salud=int(round(sueldo *0.07))
        descuento_afp=int(round(sueldo *0.12))
        sueldo liquido=int(round(sueldo - descuento_salud - descuento_afp))
        reporte.append((trabajador,sueldo,descuento_salud,descuento_afp, sueldo liquido))

    for fila in reporte:print(f"{fila[0]:<20}${fila[1]:<10}${fila[2]:<10}${fila[3]:<10}${fila[4]:<10}")

    with open ("reporte_sueldos.csv",mode="w",newline="")as file:
        writer =csv.writer(file)
        writer.writerow(["nombre empleado","sueldo base","descuento salud","descuento afp","sueldo liquido"])
        for fila in reporte:
            writer.writerow(fila)

    print("reporte de sueldos exportado a ´reporte_sueldo.csv´.")