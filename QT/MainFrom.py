# coding = utf-8

import sys
from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2 import QtCore

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("勞資是標題")
        self.resize(300,300)
        self.move(500,200)
        self.show()