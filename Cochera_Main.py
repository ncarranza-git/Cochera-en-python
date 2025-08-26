from Clase_Cochera import Cochera

validacion = False

cochera1 = Cochera(5, 3500)
# print("Bienvenidos al estacionamiento!! A continuación están las opciones")
# print("1: Ingresar un vehículo")
# print("2: Retirar un vehículo")
# print("3: Mostrar lugares")
# print("4: Salir del menú")

while validacion == False:
    print("Bienvenidos al estacionamiento!! A continuación están las opciones")
    print("1: Ingresar un vehículo")
    print("2: Retirar un vehículo")
    print("3: Mostrar lugares")
    print("4: Salir del menú")

    opcion = int(input("Indique la opcion que desea realizar: "))

    if opcion == 1:
        cochera1.ingresar_vehiculo()
        validacion = False
    elif opcion == 2:
        cochera1.retirar_vehiculo()
        validacion = False
    elif opcion == 3:
        cochera1.mostrar_vehiculos()
    elif opcion == 4:
        print("Salió del menú.")
        validacion = True
        pass