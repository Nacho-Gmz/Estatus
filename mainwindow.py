import os, pickle
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QWidget, QMessageBox, QPushButton, QTableWidgetItem
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.contactos = list()
        if os.path.exists('contactos.pickle'):
            archivo = open('contactos.pickle', 'rb')
            while True:
                try:
                    contacto = pickle.load(archivo)
                    self.contactos.append(contacto)
                except:
                    break
            archivo.close()

        self.setupUi(self)
        self.agregar_pushButton.clicked.connect(self.agregar)
        self.eliminar_pushButton.clicked.connect(self.eliminar)
        self.print_table()

    @Slot()
    def agregar(self):
        contacto = list()
        #Estructura de contacto: Nombre(0), Telefono (1)
        contacto.append(self.nombre_lineEdit.text())
        contacto.append(self.telefono_lineEdit.text())
        archivo = open ('contactos.pickle', 'ab')
        pickle.dump(contacto,archivo)
        archivo.close()
        self.contactos.append(contacto)
        self.nombre_lineEdit.clear()
        self.telefono_lineEdit.clear()
        self.print_table()
    
    @Slot()
    def eliminar(self):
        self.contactos.clear()
        if os.path.exists('contactos.pickle'):
            os.remove('contactos.pickle')
        self.print_table()

    def print_table(self):
        self.contactos_tableWidget.setColumnCount(2)
        self.contactos_tableWidget.setRowCount(len(self.contactos))
        self.contactos_tableWidget.setHorizontalHeaderLabels(['Nombre','Telefono'])
        for row in range (len(self.contactos)):
            for column in range (0,2):
                self.contactos_tableWidget.setItem(
                    row,
                    column,
                    QTableWidgetItem(str(self.contactos[row][column]))
                )