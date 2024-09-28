
import mysql.connector as mysql_conn


def create_connection(host, user, password, database):
   
    try:
        
        conn = mysql_conn.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        
        cursor = conn.cursor()
        print("Se ha conectado exitosamente a la base de datos")
        return conn, cursor
    
    except mysql_conn.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        exit(1)