# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frist.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import (QApplication, QWidget,QToolTip,QPushButton,QMessageBox,QDesktopWidget, QMainWindow)
class Ui_Form(QMainWindow):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setTabletTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("show.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        QMainWindow.closeEvent = self.closeEvent  #自身的关闭窗口事件绑定到Ui界面的关闭按钮上面
        self.quit = QtWidgets.QPushButton(Form)
        self.quit.setGeometry(QtCore.QRect(130, 140, 93, 28))
        self.quit.setObjectName("quit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 50, 141, 16))
        self.label.setObjectName("label")
        self.label.raise_()
        self.quit.raise_()

        self.retranslateUi(Form)
        self.quit.clicked.connect(Form.close)    #//按钮的点击事件与Form的关闭事件绑定在一起。
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "new game"))
        self.quit.setToolTip(_translate("Form", "this is a <b>Qiut</b> button"))
        self.quit.setText(_translate("Form", "quit"))
        self.label.setText(_translate("Form", "这是我第一个QT程序"))

    def closeEvent(self,event):
        reply = QMessageBox.question(self,'Message',"Are you sure to quit?",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
