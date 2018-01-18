import os
import platform
import json
import PyQt5
import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QApplication, QGridLayout, QLineEdit


class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # for making the window draggable
        self.oPos = self.pos()
        self.setFixedSize(1000, 650)



        lblMath = QLabel('Math')
        lblSS = QLabel('Social Studies')
        lblLang = QLabel('Language Arts')
        lblSci = QLabel('Science')
        # Todo research which method is best
        self.mathBox = QLineEdit()
        # Todo or
        ssBox = QLineEdit()

        testlw = QVBoxLayout()
        testlw.addWidget(lblMath)
        testlw.addWidget(QLineEdit(self.mathBox))
        testlw.addWidget(lblSS)
        testlw.addWidget(QLineEdit(ssBox))
        testlw.addWidget(lblLang)
        testlw.addWidget(lblSci)

        testlo = QGridLayout()
        testlo.addLayout(testlw, 0, 1)

        self.setLayout(testlo)
        self.setWindowTitle('GooeyGPA')

    def mousePressEvent(self, event):
        self.oPos = event.globalPos()

    def mouseMoveEvent(self, QMouseEvent):
        delta = QPoint(QMouseEvent.globalPos() - self.oPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oPos = QMouseEvent.globalPos()




app = QApplication(sys.argv)
screen = Form()
screen.show()
sys.exit(app.exec_())