import Modell

class Controller:
    @staticmethod
    def ingresar_producto(al):
        #print("Ingresar No implementado")
        Modell.Modell.ingresar_producto_db(al)

    @staticmethod
    def actualizar_producto(al):
        #print("Actualizar No implementado")
        Modell.Modell.actualizar_producto_db(al)

    @staticmethod
    def borrar_producto(al):
        #print("Borrar No implementado")
        Modell.Modell.borrar_producto_db(al)

    @staticmethod
    def listar_productos():
        #print("Borrar No implementado")
        return Modell.Modell.listar_producto_db()
