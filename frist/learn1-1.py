#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Py40.com PyQt5 tutorial

In this example, we create a simple
window in PyQt5.

author: alex
"""

import sys

#这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
from PyQt5.QtWidgets import (QApplication, QWidget,QToolTip,QPushButton,QMessageBox,QDesktopWidget)
from PyQt5.QtGui import (QIcon,QFont)
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #这种静态的方法设置一个用于显示工具提示的字体，我们使用10px滑体字体 提示文字的字体设置
        QToolTip.setFont(QFont('SansSerif',10))
        #创建一个提示，我们称之为settooltip（）方法。我们可以使用丰富的文本格式
#        self.setToolTip('This is a <b>QPushButton</b> widget')
        #创建一个qiut按键并设置一个tooltip
        btn = QPushButton('Quit',self)
        btn.setToolTip('This is a <b>Quit</b> widget') #把提示信息绑定到按钮的区域。
        btn.clicked.connect(QCoreApplication.instance().quit)
        #btn.sizeHint()显示默认尺寸
        btn.resize(btn.sizeHint())
        #移动窗口的位置
        btn.move(50,50)
#        #设置窗口的位置和大小
#        self.setGeometry(300,300,300,220)
        self.resize(300,200)
        self.center()
        #设置窗口的标题
        self.setWindowTitle('small game')
        #设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('show.jpg'))
        #显示窗口
        self.show()

    def closeEvent(self,event):
        reply = QMessageBox.question(self,'Message',"Are you sure to quit?",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def center(self):
        #获取窗口：
        qr = self.frameGeometry()
        #获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        #显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    #创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())