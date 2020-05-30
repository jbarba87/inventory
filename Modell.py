
import sqlite3
import Producto

path = 'inventario'

class Modell:

    def ingresar_producto_db(alumno):
        try:
            conn = sqlite3.connect(path)
        except:
            print("Error al conectar con la DB")
        c = conn.cursor()

        nombre = producto.getnombre()
        categoria = producto.getcategoria()
        precio = producto.getprecio()
        stock = producto.getstock()

        sql_command = "insert into productos (nombre, categoria, precio, stock) values ('{}', '{}', '{}', '{}', '{}')".format (nombre, categoria, precio, stock)

        c.execute(sql_command)
        conn.commit()
        conn.close()


    def actualizar_producto_db(alumno):
        try:
            conn = sqlite3.connect(path)
        except:
            print("Error al conectar con la DB")
        c = conn.cursor()

        nombre = producto.getnombre()
        categoria = producto.getcategoria()
        precio = producto.getprecio()
        stock = producto.getstock()

        sql_command = "update productos set nombre='{}', categoria='{}', precio='{}', stock='{}' where id = '{}'".format (nombre, categoria, precio, stock, id)
        c.execute(sql_command)
        conn.commit()
        conn.close()


    def borrar_producto_db(alumno):
        try:
            conn = sqlite3.connect(path)
        except:
            print("Error al conectar con la DB")
        c = conn.cursor()

        id = alumno.getid()

        sql_command = "delete from productos where id = '{}'".format(id)
        c.execute(sql_command)
        conn.commit()
        conn.close()



    def listar_producto_db():
        
        try:
            conn = sqlite3.connect(path)
        except:
            print("Error al conectar con la DB")

        c = conn.cursor()

        #c.execute("select * from productos;")
        c.execute("select * from PRODUCTOS_CAT;")
        record = c.fetchall()        
        
        conn.close()

        return record
