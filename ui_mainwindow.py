# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(318, 364)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.nombre_lineEdit = QLineEdit(self.groupBox)
        self.nombre_lineEdit.setObjectName(u"nombre_lineEdit")
        self.nombre_lineEdit.setMaxLength(100)

        self.gridLayout.addWidget(self.nombre_lineEdit, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.telefono_lineEdit = QLineEdit(self.groupBox)
        self.telefono_lineEdit.setObjectName(u"telefono_lineEdit")
        self.telefono_lineEdit.setMaxLength(16)
        self.telefono_lineEdit.setFrame(True)

        self.gridLayout.addWidget(self.telefono_lineEdit, 1, 1, 1, 1)

        self.agregar_pushButton = QPushButton(self.groupBox)
        self.agregar_pushButton.setObjectName(u"agregar_pushButton")

        self.gridLayout.addWidget(self.agregar_pushButton, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.contactos_tableWidget = QTableWidget(self.groupBox_2)
        self.contactos_tableWidget.setObjectName(u"contactos_tableWidget")

        self.gridLayout_3.addWidget(self.contactos_tableWidget, 0, 0, 1, 1)

        self.eliminar_pushButton = QPushButton(self.groupBox_2)
        self.eliminar_pushButton.setObjectName(u"eliminar_pushButton")

        self.gridLayout_3.addWidget(self.eliminar_pushButton, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Agenda", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Agenda de contactos", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono", None))
        self.agregar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.groupBox_2.setTitle("")
        self.eliminar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Eliminar contactos", None))
    # retranslateUi

