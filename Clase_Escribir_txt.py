
def Escribir (ecribir_Lugares, registro): #String
    archivo=open("Cochera_Registro.txt","a",encoding="utf-8") # Abre el archivo.
    archivo.writelines(registro) # Si el archivo no existe, lo crea. Si ya existe, agrega contenido al final sin borrar lo anterior.
    archivo.close()
    # Escribir ("Cochera_Registro.txt", registro= " ")

def Leer(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:  # Abre y asegura el cierre automático
        texto = archivo.readlines()  # Lee todas las líneas en una lista
        cochera = []
        for linea in texto:
            aux = linea.split(",")
            cochera.append(aux)
        return cochera

def Eliminar(nombre_archivo, dominio):
   nuevo_registro = Leer(nombre_archivo)
   for registro in nuevo_registro:
        if registro[2] == dominio:
            print(f"Se quitó el registro con dominio {dominio}")  
            nuevo_registro.remove(registro)
        elif registro[2] != dominio:
             print("No se encontró el dominio dentro del registro")

        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            for lista in nuevo_registro:
                registro = ",".join(lista).strip()
                archivo.write(registro+"\n")

