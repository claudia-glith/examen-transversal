import utilidades

while True:
    print("/nmenu:")
    print("1. asignar sueldos aleatorios")
    print("2. clasificar sueldos ")
    print("3. ver estadisticas")
    print("4. reporte de sueldos")
    print("5. salir del programa")

    opcion =input("seleccione una opcion:")

if opcion =="1":
    utilidades.asignar_sueldos()
elif opcion =="2":
    utilidades.clasificar_sueldos()
elif opcion =="3":
    utilidades.ver_estadisticas()
elif opcion =="4":
    utilidades.reporte_sueldos()
elif opcion =="5":
    print("finalizando programa...")
    print("desarrollado por Claudia Pinchuleo")
    print("rut 17.839.756-7")
    break

    else:
        print("opcion no valida,por favor seleccione nuevamente")

