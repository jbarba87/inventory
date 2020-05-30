# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_inventario.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import Controller
import Producto

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(634, 573)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 591, 491))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btnEliminar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnEliminar.setObjectName("btnEliminar")
        self.gridLayout.addWidget(self.btnEliminar, 3, 3, 1, 1)
        self.btnEditar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnEditar.setObjectName("btnEditar")
        self.gridLayout.addWidget(self.btnEditar, 3, 2, 1, 1)
        self.btnAgregar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnAgregar.setObjectName("btnAgregar")
        self.gridLayout.addWidget(self.btnAgregar, 3, 1, 1, 1)
        self.btnActualizar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnActualizar.setObjectName("btnActualizar")
        self.gridLayout.addWidget(self.btnActualizar, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 4)
        self.tblProductos = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tblProductos.setObjectName("tblProductos")
        self.tblProductos.setColumnCount(5)
        self.tblProductos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblProductos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblProductos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblProductos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblProductos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblProductos.setHorizontalHeaderItem(4, item)
        self.gridLayout.addWidget(self.tblProductos, 1, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 634, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        # Conexiones ingresadas
        #self.btnAgregar.clicked.connect(self.procesar_agregar)
        self.btnActualizar.clicked.connect(self.procesar_actualizacion)
        #self.btnBorrar.clicked.connect(self.procesar_borrado)
        #self.btnEditar.clicked.connect(self.procesar_edicion)
        #self.tableWidget.cellClicked.connect(self.table_clicked)

    def procesar_ingreso(self):
        self.procesar(0)


    def procesar_actualizacion(self):
        lista = Controller.Controller.listar_productos()

        row = 0

        self.tblProductos.setRowCount( len(lista) )

        print(lista)

        for al in lista:

            self.tblProductos.setItem(row, 0, QtWidgets.QTableWidgetItem(str(al[0])))
            self.tblProductos.setItem(row, 1, QtWidgets.QTableWidgetItem(al[1]))
            self.tblProductos.setItem(row, 2, QtWidgets.QTableWidgetItem(al[2]))
            self.tblProductos.setItem(row, 3, QtWidgets.QTableWidgetItem(str(al[3])))
            self.tblProductos.setItem(row, 4, QtWidgets.QTableWidgetItem(str(al[4])))

            row = row + 1

        # Estableciendo ancho de columnas
        self.tblProductos.setColumnWidth(0, 30)
        self.tblProductos.setColumnWidth(1, 100)
        self.tblProductos.setColumnWidth(2, 80)
        self.tblProductos.setColumnWidth(3, 50)
        self.tblProductos.setColumnWidth(4, 50)

        
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle(" ")
        msgBox.setText("Mostrando " + str(row) + " columnas.")
        msgBox.exec()





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnEliminar.setText(_translate("MainWindow", "Eliminar"))
        self.btnEditar.setText(_translate("MainWindow", "Editar"))
        self.btnAgregar.setText(_translate("MainWindow", "Agregar"))
        self.btnActualizar.setText(_translate("MainWindow", "Actualizar"))
        item = self.tblProductos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tblProductos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tblProductos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Producto"))
        item = self.tblProductos.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Categoria"))
        item = self.tblProductos.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Stock"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

