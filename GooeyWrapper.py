from PyQt5.QtWidgets import QVBoxLayout, QLabel, QDesktopWidget, QWidget, QApplication
from PyQt5.QtCore import Qt, QPoint


class Rapper(QLabel):
    def __init__(self, parent):
        QLabel.__init__(self, parent)
