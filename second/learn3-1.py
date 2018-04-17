#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Py40.com PyQt5 tutorial

In this example, we create a simple
window in PyQt5.

author: alex
"""

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication,QLabel)

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUi()

    def initUi(self):
        '''
        lbl1 = QLabel('Zetcode',self)
        lbl1.move(15,10)

        lbl2 = QLabel('tutorials',self)
        lbl2.move(15,40)     #从哪一点开始显示标签

        lbl3 = QLabel('for programmers',self)
        lbl3.move(55,70)
        '''
        okButton = QPushButton("ok")
        cancelBuntton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelBuntton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.setGeometry(300,300,300,200)  #前面两个参数是设置在界面的位置左上角为坐标0点。后面两个参数是设置窗口的大小。
        self.setWindowTitle('learning3-1')
        self.show()

if __name__ == '__main__':
    #创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())