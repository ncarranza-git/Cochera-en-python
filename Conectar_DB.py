import pymysql
import getpass

# Connect to the database
def conectar(ip,usuario,puerto):
    connection = pymysql.connect(host=ip,
                                user=usuario,
                                password=getpass.getpass("Ingrese la contraseña: "),
                                port=puerto,
                                database='db_cochera',
                                cursorclass=pymysql.cursors.DictCursor)
    print("Conectado a la DB!\n--------------------------------")
    return connection

#Crear tabla, definiendo los campos
def crear_tabla(conexion_db, tabla_vehiculos):
    cursor = conexion_db.cursor()
    sql = f""" CREATE TABLE IF NOT EXISTS {tabla_vehiculos} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        dominio VARCHAR (50) NOT NULL,
        tipo_vehiculo VARCHAR (50) NOT NULL,
        ubicacion VARCHAR (50) NOT NULL,
        fecha_y_hora_ingreso DATETIME
    );
    """
    cursor.execute(sql)
    print("Se creo la tabla correctamente!!")
    

def escribir_db(conexion_db, tabla_vehiculos, dominio, tipo_vehiculo, ubicacion, hora_ingreso):
    cursor = conexion_db.cursor()
    sql = f"""INSERT INTO {tabla_vehiculos} 
             (dominio, tipo_vehiculo, ubicacion, fecha_y_hora_ingreso)
             VALUES (%s, %s, %s, %s)"""
    cursor.execute(sql, (dominio, tipo_vehiculo, ubicacion, hora_ingreso))
    conexion_db.commit()
    print("Se cargaron los datos correctamente en la DB!!")


def eliminar_datos(conexion_db, tabla_vehiculos, dominio_buscado):
    cursor = conexion_db.cursor()
    sql = f""" DELETE FROM {tabla_vehiculos} 
            WHERE dominio = %s
    """
    cursor.execute(sql, (dominio_buscado))
    conexion_db.commit()
    print(f"Se elimino el vehiculo con dominio: {dominio_buscado} correctamente")
    
def mostrar_tabla(conexion_db,tabla_vehiculos):
     with conexion_db.cursor() as cursor:
            sql = f"SELECT * FROM {tabla_vehiculos}"
            cursor.execute(sql)
            resultado = cursor.fetchall()
            print(resultado)
            return resultado
        

# conexion=conectar('127.0.0.1','root',3306)
# crear_tabla(conexion, "tabla_vehiculos")
# escribir_db(conexion, "dominio", "tipo_vehiculo", "ubicacion", "hora_ingreso")
# info=mostrar_tabla(conexion,"Vehiculos")