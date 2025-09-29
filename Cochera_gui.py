import tkinter 
from tkinter import *
from Clase_Vehiculo import Vehiculo



class CocheraGUI():
    def __init__(self, cochera):
        self.cochera = cochera # Creo el objeto 
        self.top = tkinter.Tk() # Crea la ventana principal
        self.top.geometry("600x600") # Define el ancho y el alto de la ventana
        self.top.title("Cochera") # Define el titulo de la ventana
        self.top.configure(background = "white") # Define el color de fondo de la ventana

        # Elementos de la ventana
        # Creo los botones y le asigno los comandos para ingresar a sus respectivas ventanas
        self.boton1=tkinter.Button(self.top,text="Ingresar vehiculo", command=self.ventana_ingresar_vehiculo) 
        self.boton1.pack()
        self.boton2=tkinter.Button(self.top,text="Retirar vehiculo", command=self.ventana_retirar_vehiculo)
        self.boton2.pack()
        self.boton3=tkinter.Button(self.top,text="Mostrar vehiculos", command=self.ventana_mostrar_vehiculos)
        self.boton3.pack()
        self.boton4=tkinter.Button(self.top,text="Salir",command=self.top.destroy)
        self.boton4.pack()

        self.top.mainloop()

    # Creo la funcion de ventana ingresar para cargar los datos del vehiculo a guardar
    def ventana_ingresar_vehiculo(self):
        self.ventana_ingresar = tkinter.Toplevel() # Crea la ventana secundaria para ingresar un vehiculo
        self.ventana_ingresar.geometry("500x250") # Defino el tamaño de la ventana
        self.ventana_ingresar.title("Ventana Ingresar Vehiculo") # Defino el nombre de la ventana

        # Defino la etiqueta donde indica el campo a completar
        tkinter.Label(self.ventana_ingresar, text='Dominio').grid(row=0)
        tkinter.Label(self.ventana_ingresar, text='Tipo de vehiculo').grid(row=1)
        tkinter.Label(self.ventana_ingresar, text='Ubicación').grid(row=2)

        # Defino los campos en donde se deben ingresar los datos del vehiculo a guardar
        self.entry_dominio = tkinter.Entry(self.ventana_ingresar)
        self.entry_dominio.grid(row=0, column=1, padx=10, pady=10)
        self.entry_tipo_vehiculo = tkinter.Entry(self.ventana_ingresar)
        self.entry_tipo_vehiculo.grid(row=1,column=1, padx=10, pady=10 )
        self.entry_ubicacion = tkinter.Entry(self.ventana_ingresar)
        self.entry_ubicacion.grid(row=2, column=1, padx=10, pady=10)
        # self.cochera.ingresar_vehiculo(self.nuevo_vehiculo, self.entry_ubicacion.get())

        # Creo los botones para confirmar los datos, y para salir de la ventana
        self.boton_salir_de_ingresar = tkinter.Button(self.ventana_ingresar, text="Salir", command=self.ventana_ingresar.destroy)
        self.boton_salir_de_ingresar.grid(row=7, column=2, padx=10, pady=10)
        self.boton_confirmar_datos = tkinter.Button(self.ventana_ingresar, text="Confirmar", command=lambda:self.confirmar_datos())
        self.boton_confirmar_datos.grid(row=7, column= 1, padx=10, pady=10)
        self.ventana_ingresar.mainloop()

    # Creo una funcion confirmar para reemplazar los valores y vincular el GUI con clase cochera 
    def confirmar_datos(self):
        dominio = self.entry_dominio.get().upper() # Guardo el entry en la variable dominio
        tipo_vehiculo = self.entry_tipo_vehiculo.get().upper() # Guardo el entry en la variable tipo vehiculo
        ubicacion = self.entry_ubicacion.get()

        vehiculo = Vehiculo(dominio, tipo_vehiculo) # Creo el nuevo objeto con los nuevos valores
        # Ejecuto la funcion ingresar vehiculo
        self.cochera.ingresar_vehiculo(vehiculo, ubicacion)
        print("Se cargaron los datos")
    
    # Creo la funcion de la ventana retirar para cargar los datos de un vehiculo y eliminarlo
    def ventana_retirar_vehiculo(self):
        self.ventana_retirar = tkinter.Toplevel()
        self.ventana_retirar.geometry("500x250") 
        self.ventana_retirar.title("Ventana Retirar Vehiculo") 

        # Defino la etiqueta donde indica el campo a completar
        tkinter.Label(self.ventana_retirar, text='Dominio').grid(row=0)

        # Defino el campo para ingresar el dominio a eliminar
        self.entry_dominio_eliminar = tkinter.Entry(self.ventana_retirar)
        self.entry_dominio_eliminar.grid(row=0, column=1, padx=10, pady=10)

        # Creo el boton para eliminar el vehiculo con el dominio ingresado, y para salir de la ventana
        self.boton_eliminar = tkinter.Button(self.ventana_retirar, text="Eliminar", command=lambda:self.eliminar_datos())
        self.boton_eliminar.grid(row=5, column=1, padx=10, pady=10)
        self.boton_salir_de_retirar = tkinter.Button(self.ventana_retirar, text="Salir", command=self.ventana_retirar.destroy)
        self.boton_salir_de_retirar.grid(row=5, column=3, padx=10, pady=10)

        self.ventana_retirar.mainloop()

    # Creo una funcion eliminar para reemplazar los valores y vincular el GUI con clase cochera 
    def eliminar_datos(self):
        dominio_buscado = self.entry_dominio_eliminar.get().upper() # Guardo el entry en la variable a buscar
        self.cochera.retirar_vehiculo(dominio_buscado) # Ejecuto la funcion retirar vehiculo


    # Creo la funcion de la ventana para mostrar los vehiculos actuales en la cochera
    def ventana_mostrar_vehiculos(self):
        self.ventana_mostrar = tkinter.Toplevel()
        self.ventana_mostrar.geometry("500x250")
        self.ventana_mostrar.title("Ventana Mostrar Vehiculos")

        # Textos
        self.txt1 = tkinter.Label(self.ventana_mostrar, text='Vehiculos actuales en la cochera:').grid(row=0)
        self.txt2 = tkinter.Label(self.ventana_mostrar, text="Ubicación-Dominio-Tipo-Hora de Ingreso").grid(row=1)

        texto = self.cochera.mostrar_vehiculos() # Guardo en variable la funcion que muestra mi sql
        txt = tkinter.Label(self.ventana_mostrar, text=texto)
        txt.grid(row=3, column=0, padx=10, pady=10)

        # Creo un boton para salir de la ventana
        self.boton_salir_de_mostrar = tkinter.Button(self.ventana_mostrar, text="Salir", command=self.ventana_mostrar.destroy)
        self.boton_salir_de_mostrar.grid(row=4, column=3, padx=10, pady=10)

        self.ventana_mostrar.mainloop()


        