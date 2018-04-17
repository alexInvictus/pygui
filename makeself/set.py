# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'set.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
class Ui_setWindow(QtWidgets):
    speed = 50
    def setupUi(self, QDialog):
        QDialog.setObjectName("setWindow")
        QDialog.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(QDialog)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(QDialog)
        self.pushButton.setGeometry(QtCore.QRect(490, 130, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(280, 130, 87, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(QDialog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        QtWidgets.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Dialog)
        self.statusbar.setObjectName("statusbar")
        QDialog.setStatusBar(self.statusbar)

        self.retranslateUi(QDialog)
        self.pushButton.clicked.connect(self.setvalue)
        QtCore.QMetaObject.connectSlotsByName(QDialog)

    def retranslateUi(self, QDialog):
        _translate = QtCore.QCoreApplication.translate
        QDialog.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "设置"))
        self.comboBox.setItemText(0, _translate("MainWindow", "简单"))
        self.comboBox.setItemText(1, _translate("MainWindow", "困难"))

    def setvalue(self):
        speed =100
        self.close()


