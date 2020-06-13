
import sqlite3
import Producto

path = 'inventario.db'

class Modell:

    def ingresar_producto_db(producto):
        try:
            conn = sqlite3.connect(path)
        except:
            print("Error al conectar con la DB")
        c = conn.cursor()

        nombre = producto.getnombre()
        categoria = producto.getcategoria()
        precio = producto.getprecio()
        stock = producto.getstock()

        sql_command = "insert into PRODUCTOS (NOMBRE, ID_CATEGORIA, COSTO, STOCK) values ('{}', '{}', '{}', '{}')".format (nombre, categoria, precio, stock)

        try:
            c.execute(sql_command)
            conn.commit()
        except:
            conn.close()
            return -1   # Aqui deberia retornar el error
        
        conn.close()
        return 1



    def actualizar_producto_db(id_producto, producto):
        try:
            conn = sqlite3.connect(path)
        except:
            print("Error al conectar con la DB")
        c = conn.cursor()

        nombre = producto.getnombre()
        categoria = producto.getcategoria()
        precio = producto.getprecio()
        stock = producto.getstock()

        sql_command = "update PRODUCTOS set NOMBRE='{}', ID_CATEGORIA='{}', COSTO='{}', STOCK='{}' where id = '{}'".format (nombre, categoria, precio, stock, id_producto)

        c.execute(sql_command)
        conn.commit()
        conn.close()
        return 1


    def borrar_producto_db(id):
        try:
            conn = sqlite3.connect(path)
        except:
            print("Error al conectar con la DB")
        c = conn.cursor()

        #nombre = producto.getnombre()

        sql_command = "delete from PRODUCTOS where ID = '{}'".format(id)
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


    def listar_categorias_db():
        
        try:
            conn = sqlite3.connect(path)
        except:
            print("Error al conectar con la DB")

        c = conn.cursor()

        #c.execute("select * from productos;")
        c.execute("select * from CATEGORIAS;")
        record = c.fetchall()        
        
        conn.close()

        return record



    def buscar_coincidencias_db(nombre):
        
        try:
            conn = sqlite3.connect(path)
        except:
            print("Error al conectar con la DB")

        c = conn.cursor()

        c.execute("select * from PRODUCTOS where NOMBRE='nombre';")
        record = c.fetchall()        
        
        conn.close()

        return record



    def buscar_categoria_db(nombre):
        
        try:
            conn = sqlite3.connect(path)
        except:
            print("Error al conectar con la DB")

        c = conn.cursor()
        sql = "select * from CATEGORIAS where NOMBRE='{}'".format(nombre)
        c.execute(sql)
        record = c.fetchall()        
        
        conn.close()

        return record
