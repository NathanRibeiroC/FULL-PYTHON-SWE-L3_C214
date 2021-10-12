# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lista.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

"""interface.py represents ui's Main Window class"""
from PyQt5 import QtCore, QtGui, QtWidgets
from src.service.ServiceGame import *
from src.utils.csvUtils import *

class Ui_MainWindow(object):
    """Class that represents ui's Main Window"""
    def setupUi(self, MainWindow):
        """Method that setups Main Window's elements"""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 395)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(40
                                           , 20
                                           ,QtWidgets.QSizePolicy.Expanding
                                           , QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        self.verticalLayout.addWidget(self.tableWidget)
        spacerItem1 = QtWidgets.QSpacerItem(40
                                            , 20
                                            , QtWidgets.QSizePolicy.Expanding
                                            , QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40
                                            , 20
                                            , QtWidgets.QSizePolicy.Expanding
                                            , QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_3.addWidget(self.comboBox_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        spacerItem3 = QtWidgets.QSpacerItem(40
                                            , 20
                                            , QtWidgets.QSizePolicy.Expanding
                                            , QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem3)
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # table widget configuration
        self.tableWidget.setHorizontalHeaderLabels(["rank","name","platform","year"
                                                       ,"genre","publisher","na_sales","eu_sales"
                                                       ,"jp_sales","other_sales","global_sales"])

        # combo box PUBLISHER configuration
        self.comboBox.addItem('None')
        self.comboBox.addItem('Nintendo')
        self.comboBox.addItem('Microsoft Game Studios')
        self.comboBox.addItem('Take-Two Interactive')
        self.comboBox.addItem('Activision')
        self.comboBox.addItem('Sony Computer Entertainment')
        self.comboBox.addItem('Electronic Arts')

        # combo box PLATFORM configuration
        self.comboBox_2.addItem('None')
        self.comboBox_2.addItem('PS4')
        self.comboBox_2.addItem('PC')
        self.comboBox_2.addItem('XB')
        self.comboBox_2.addItem('Wii')
        self.comboBox_2.addItem('GB')
        self.comboBox_2.addItem('GBA')
        self.comboBox_2.addItem('X360')
        self.comboBox_2.addItem('PS3')
        self.comboBox_2.addItem('PS2')

        # configuring pushButton
        self.pushButton.clicked.connect(self.get_list_by_combo_select)

        # parsed list from CSV file
        self.parsedL = CsvOperations().csv_convert()

    def get_combo_box_text(self):
        """Gets text from combo boxes"""
        comboPublisher = str(self.comboBox.currentText())
        comboPlatform = str(self.comboBox_2.currentText())
        return comboPlatform, comboPublisher

    def get_list_by_combo_select(self):
        """Searches games based on combo boxes parameters"""
        aux = []
        Platform, Publisher = self.get_combo_box_text()
        if(Platform == 'None')and(Publisher!='None'):
            aux = ServiceGame.get_list_by_publisher(self.parsedL, Publisher)
        elif(Platform != 'None')and(Publisher=='None'):
            aux = ServiceGame.get_list_by_platform(self.parsedL, Platform)
        elif(Platform != 'None')and(Publisher!='None'):
            aux = ServiceGame.get_list_by_platform_and_publisher(self.parsedL,Publisher,Platform)
        else:
            aux = []
        self.show_list_on_table(aux)

    def show_list_on_table(self,aux):
        """Shows games searched on table widget"""
        tablerow = 0
        self.tableWidget.setRowCount(len(aux))
        for row in aux:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
            self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
            self.tableWidget.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row[8])))
            self.tableWidget.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(str(row[9])))
            self.tableWidget.setItem(tablerow, 10, QtWidgets.QTableWidgetItem(str(row[10])))
            tablerow += 1


    def retranslateUi(self, MainWindow):
        """Defines Main Window element's texts"""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LISTA 3 C214"))
        self.label_2.setText(_translate("MainWindow", "Select Publisher"))
        self.label.setText(_translate("MainWindow", "Select Platform"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
