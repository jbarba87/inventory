import Modell

class Controller:
    @staticmethod
    def ingresar_producto(prod):
        #print("Ingresar No implementado")
        return Modell.Modell.ingresar_producto_db(prod)

    @staticmethod
    def actualizar_producto(id_producto, prod):
        #print("Actualizar No implementado")
        return Modell.Modell.actualizar_producto_db(id_producto, prod)

    @staticmethod
    def borrar_producto(id):
        #print("Borrar No implementado")
        Modell.Modell.borrar_producto_db(id)

    @staticmethod
    def listar_productos():
        #print("Borrar No implementado")
        return Modell.Modell.listar_producto_db()

    @staticmethod
    def listar_categorias():
        #print("Borrar No implementado")
        return Modell.Modell.listar_categorias_db()

    @staticmethod
    def buscar_coincidencias(nombre):
        #print("Borrar No implementado")
        return Modell.Modell.buscar_coincidencias_db(nombre)

    @staticmethod
    def buscar_categoria(nombre):
        #print("Borrar No implementado")
        return Modell.Modell.buscar_categoria_db(nombre)

