from PyQt5 import QtCore, QtGui, QtWidgets
from inventario_ui import Ui_Dialog
import Controller
import Producto


def procesar_actualizacion_ext(main):

    lista = Controller.Controller.listar_productos()

    row = 0

    main.tblProductos.setRowCount( len(lista) )

    for al in lista:

        main.tblProductos.setItem(row, 0, QtWidgets.QTableWidgetItem(str(al[0])))
        main.tblProductos.setItem(row, 1, QtWidgets.QTableWidgetItem(al[1]))
        main.tblProductos.setItem(row, 2, QtWidgets.QTableWidgetItem(al[2]))
        main.tblProductos.setItem(row, 3, QtWidgets.QTableWidgetItem(str(al[3])))
        main.tblProductos.setItem(row, 4, QtWidgets.QTableWidgetItem(str(al[4])))

        row = row + 1

    # Estableciendo ancho de columnas
    main.tblProductos.setColumnWidth(0, 30)
    main.tblProductos.setColumnWidth(1, 150)
    main.tblProductos.setColumnWidth(2, 80)
    main.tblProductos.setColumnWidth(3, 80)
    main.tblProductos.setColumnWidth(4, 50)


    msgBox = QtWidgets.QMessageBox()
    msgBox.setWindowTitle(" ")
    msgBox.setText("Mostrando " + str(row) + " columnas.")
    msgBox.exec()

def procesar_agregar_ext(main):
     
    # Abre nueva ventana
        
    main.Dialog = QtWidgets.QDialog()
    main.ui = Ui_Dialog()
    main.ui.setupUi(main.Dialog)
    main.Dialog.show()

    rsp = main.Dialog.exec_()

    # Si el boton es aceptar, entonces se recupera los datos ingresados
    if rsp == QtWidgets.QDialog.Accepted:
        print("Aceptado")
        nombre = main.ui.lineEdit.text() # nombre
        categoria = main.ui.comboBox.currentText() # catogoria
        #categoria = main.ui.comboBox.currentIndex()
        costo = main.ui.lineEdit_3.text() # costo
        stock = main.ui.lineEdit_4.text() # stock

        # Buscar categoria con el nombre y recuperar el indice
        cat = Controller.Controller.buscar_categoria(categoria)

        # Limpiando datos para almacenarlos en la BD (doble caracteres y car inicio y fin)
        nombre = " ".join(nombre.split())

        # Agregar dato en la BD
        nuevo_prod = Producto.Producto()
        nuevo_prod.setnombre(nombre)
        nuevo_prod.setcategoria(cat[0][0])
        nuevo_prod.setprecio(costo)
        nuevo_prod.setstock(stock)
        res = Controller.Controller.ingresar_producto(nuevo_prod)

        # Creacion del mensaje de exito o fracaso
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle(" ")

        if res == -1:
            msgBox.setText("Error al ingresar producto")
            msgBox.exec()
        else:
            msgBox.setText("Producto ingresado con exito")
            msgBox.exec()
            main.procesar_actualizacion()

    else:
        print("Cancelado")





def procesar_borrado_ext(main):
    # Borrar entreda
    widget_selected = main.tblProductos.selectedItems() # Lista de elementos seleccioandos
    row = widget_selected[0].row()
    # Elimina row de la tabla
    # main.tblProductos.removeRow(row)

    # Se busca el id del producto (columna 0)
    id = main.tblProductos.item(row, 0).text()
    # Elimina row de la base de datos
    Controller.Controller.borrar_producto(id)
    main.procesar_actualizacion()

def procesar_edicion_ext(main):

    widget_selected = main.tblProductos.selectedItems() # Lista de elementos seleccioandos
    row = widget_selected[0].row()

    # Obteniendo los datos del producto a editar
    id_producto = main.tblProductos.item(row, 0).text()        
    nombre = main.tblProductos.item(row, 1).text()
    categoria = main.tblProductos.item(row, 2).text()
    precio = main.tblProductos.item(row, 3).text()
    stock = main.tblProductos.item(row, 4).text()

    # Buscar categoria con el nombre y recuperar el indice
    cat = Controller.Controller.buscar_categoria(categoria)
    id_cat = cat[0][0]

    # Abre nueva ventana
    main.Dialog = QtWidgets.QDialog()
    main.ui = Ui_Dialog()
    main.ui.setupUi(main.Dialog)
    main.Dialog.show()

    # Rellena datos a editar
    main.ui.lineEdit.setText(nombre)
    main.ui.comboBox.setCurrentText(categoria)
    main.ui.lineEdit_3.setText(precio)
    main.ui.lineEdit_4.setText(stock)

    rsp = main.Dialog.exec_()


    # Si el boton es aceptar, entonces se recupera los datos ingresados
    if rsp == QtWidgets.QDialog.Accepted:
        print("Aceptado")
        nombre = main.ui.lineEdit.text() # nombre
        categoria = main.ui.comboBox.currentText() # catogoria
        #categoria = main.ui.comboBox.currentIndex()
        costo = main.ui.lineEdit_3.text() # costo
        stock = main.ui.lineEdit_4.text() # stock

        # Buscar categoria con el nombre y recuperar el indice
        cat = Controller.Controller.buscar_categoria(categoria)
        id_cat = cat[0][0]
        # Limpiando datos para almacenarlos en la BD
        nombre = " ".join(nombre.split())

        # Agregar dato en la BD
        nuevo_prod = Producto.Producto()
        nuevo_prod.setnombre(nombre)
        nuevo_prod.setcategoria(id_cat)
        nuevo_prod.setprecio(costo)
        nuevo_prod.setstock(stock)
        res = Controller.Controller.actualizar_producto(id_producto, nuevo_prod)

        # Creacion del mensaje de exito o fracaso
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle(" ")

        if res == -1:
            msgBox.setText("Error al actualizar producto")
            msgBox.exec()
        else:
            msgBox.setText("Producto actualizado con exito")
            msgBox.exec()
            main.procesar_actualizacion()

    else:
        print("Cancelado")

def guardar_ext(main):
    #Guardar en .cvs
    f = open("exp.cvs", 'w')

    lista = Controller.Controller.listar_productos()

    row = 0

    for pr in lista:
        f.write(str(pr[0]) + ',' + str(pr[1]) + ',' + str(pr[2]) + ',' + str(pr[3]) + ',' + str(pr[4]) + '\n')

    f.close()
















