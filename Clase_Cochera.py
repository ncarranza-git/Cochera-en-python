from Clase_Vehiculo import Vehiculo
from datetime import datetime
from Clase_Escribir_txt import Escribir
from Clase_Escribir_txt import Leer
from Clase_Escribir_txt import Eliminar
# from Clase_Estacionamiento import Estacionamiento


class Cochera:
    def __init__(self, ubicaciones, precio_x_hora):
        self.precio_x_hora = precio_x_hora
        self.cant_ubicaciones = ubicaciones
        self.precio_x_dia = precio_x_hora * 0.8
        self.lugares = { }
        self.ubicaciones = { }
        txt = Leer("Cochera_Registro.txt")
        print(txt)

        for i in range (1, self.cant_ubicaciones+1):
            if len(txt) == 0:
                self.lugares[str(i)] = False
            else:
                for linea in txt:
                    
                    print(linea)
                    linea_ubicacion = int(linea[1]) # Convierte la línea en lista
                    # print("i: ", i )
                    # print("linea: ", linea)
                    # print("linea ubicacion: ", linea_ubicacion)
                    # print(linea[0:18])
                    if i == linea_ubicacion:
                        print("match!")
                        self.lugares[str(i)] = {"vehiculo":Vehiculo(linea[2], linea[3].strip()),
                                                "ingreso": datetime(int(linea[0].split("-")[0]),
                                                                    int(linea[0].split("-")[1]),
                                                                    int(linea[0].split("-")[2]),
                                                                    int(linea[0].split("-")[3]),
                                                                    int(linea[0].split("-")[4]))
                                            }
                        break
                    else: 
                        self.lugares [str(i)]=False

        print(self.lugares)
        pass
    
    def ingresar_vehiculo(self):
        # print("Bienvenido al Estacionamiento")
        dominio = input("Ingrese el dominio del vehiculo: ").upper()
        tipo_vehiculo = input("Indique el tipo de vehiculo: ").upper()
        # hora_ingreso = int(input("La hora de ingreso es: "))
        lista = []
        hora_ingreso = datetime.now()
        vehiculo = Vehiculo(dominio, tipo_vehiculo) #Construir un objeto de la clase vehiculo.
        # numero_plazas = int(input("Indique la cantidad de plazas del vehiculo: "))
        ubicacion = input(f"Igrese la ubicación (1-{self.cant_ubicaciones}): ")
        # numero_plazas = int(input("Indique la cantidad de plazas del vehiculo: "))
        print(f"Se ingresó el vehiculo {vehiculo.dominio}, tipo: {vehiculo.tipo_vehiculo} en la ubicación: {ubicacion} a las {hora_ingreso} hs.")
        if self.lugares[ubicacion] is False: #Si la ubicacion esta libre...
            self.lugares[ubicacion] = {"vehiculo": vehiculo, #Guarda la variable vehiculo en la clave vehiculo
                                        "ingreso": hora_ingreso} #Guarda la variable hora de ingreso en la clave ingreso
            self.lugares[ubicacion] = {"vehiculo": vehiculo, #Guarda la variable vehiculo en la clave vehiculo
                                        "ingreso": datetime.now()} #Guarda la variable hora de ingreso en la clave ingreso con datetime
            
            registro = ",".join([self.lugares[ubicacion]["ingreso"].strftime("%Y-%m-%d-%H-%M"),
            ubicacion,self.lugares[ubicacion]["vehiculo"].dominio, self.lugares[ubicacion]
            ["vehiculo"].tipo_vehiculo]) + "\n"
            Escribir("Cochera_Registro.txt", registro)
            print(self.lugares)
        else:
            print(f"La ubicacion {ubicacion} está ocupada")
            print("------------")
        # numero_plazas = int(input("Indique la cantidad de plazas del vehiculo: "))
   
    def retirar_vehiculo(self):
        print("Indique los datos del vehículo que desea retirar")
        dominio_buscado = input("Ingrese el dominio del vehículo: ").upper()
        Eliminar("Cochera_Registro.txt", dominio_buscado)
        for i in range( 1, self.cant_ubicaciones+1):
            if self.lugares[str(i)] != False:
                if self.lugares[str(i)]["vehiculo"].dominio == dominio_buscado: # Si el dominio buscado coincide con alguno guardado...
                    ingreso = self.lugares[str(i)]["ingreso"] # Busco la variable hora de ingreso en el diccionario y la guardo en otra variable
                    self.calcular_total(ingreso)
                    self.lugares[str(i)] = False

                    # print(Vehiculo(dominio_buscado))
                # elif self.lugares[str(i)]["vehiculo"].dominio != dominio_buscado:
                #     print("No se encontró el dominio buscado ")
    
    def mostrar_vehiculos(self):
        for i in range(1, self.cant_ubicaciones+1):
            if self.lugares[str(i)] == False:
                print(f"{str(i)} - LIBRE")
            else:
                print(f"{str(i)} - Dominio: {self.lugares[str(i)]["vehiculo"].dominio}") # Muestro el dominio que ocupa el lugar
    pass

    def calcular_total(self, ingreso):
        hora_salida = datetime.now()
        diferencia = (hora_salida - ingreso).seconds / 3600 # Calculo las horas de estacionamient
        print(f"La hora de ingreso es: {ingreso}")
        print(diferencia)
        if diferencia <= 1:
            monto_a_pagar = self.precio_x_hora # Si el tiempo es menor a una hora, debe abonar una hora minimo
        elif diferencia >= 24:
            monto_a_pagar = self.precio_x_dia * diferencia
        else:
            monto_a_pagar = diferencia * self.precio_x_hora # Calculo el monto que se debe pagar
        print(f"La cantidad de horas es de: {diferencia} hs\nEl monto a pagar es de ${monto_a_pagar}")
        # Modificar para cobrar precios diferentes segun el tipo de vehiculo
    # pass