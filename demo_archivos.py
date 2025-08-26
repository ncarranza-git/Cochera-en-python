# archivo=open("demo.txt","a",encoding="utf-8") # Abre el archivo.
# archivo.write("Hola mundo! \n") # Si el archivo no existe, lo crea. Si ya existe, agrega contenido al final sin borrar lo anterior.
# archivo.close() Cierra el archivo.

# archivo=open("demo.txt","r",encoding="utf-8") # Abre el archivo en modo lectura
# texto=archivo.readlines() #  Lee todas las líneas del archivo y las guarda en una lista
# print(texto[1]) # Muestra la segunda línea del archivo (los índices empiezan en 0)
# print(type(texto)) # Muestra que texto es de tipo list
# archivo.close() # Cierra el archivo

# archivo=open("demo.txt","w",encoding="utf-8") # Abre el archivo en modo escritura (write). 
    # Si el archivo ya existe, borra todo el contenido anterior.
# lista=["A","B","C","D","E"] # Define la lista con sus valores
# for elemento in lista:
#     archivo.write(elemento+"\n") # El bucle escribe cada elemento de la lista en una línea del archivo.
# archivo.close() # Cierra el archivo 

lista=["A","B","C","D","E"]
with open("demo.txt","a",encoding="utf-8") as archivo: 
    for elemento in lista: 
        archivo.write(elemento+"\n")

archivo = open("demo.txt", "r", encoding="utf-8") # Lee solo la primera línea y la guarda en texto.
texto = archivo.readline()
for i in range(1,4): # lee tres líneas más (líneas 2, 3 y 4) y las imprime.
    print(archivo.readline())
# print(texto)
# print(texto[2])
# print(type(texto))
archivo.close()


# "a"	Agrega contenido sin borrar lo anterior.
# "w"	Escribe desde cero, borra lo anterior.
# "r"	Solo lectura.
# readlines()	Lee todo y devuelve una lista de líneas.
# readline()	Lee una sola línea (la siguiente disponible).
# with open(...) as archivo:	Maneja automáticamente la apertura y cierre.