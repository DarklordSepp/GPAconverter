import sys
import os
import platform
import json
import PyQt5
from PyQt5.QtGui import QPainter, QPixmap

import GooeyPrompt
import test

from PyQt5.QtWidgets import QVBoxLayout, QLabel, QDesktopWidget, QWidget, QApplication, QInputDialog, QLineEdit, \
    QPushButton, QFormLayout, QHBoxLayout, QAbstractButton
from PyQt5.QtCore import Qt, QPoint


class Rapper(QLabel):
    def __init__(self, parent):
        QLabel.__init__(self, parent)
        # thanks im_dead_sirius!
        self.setStyleSheet(
            '''
            color: rgba(0,0,0,100%);
            background-color: rgba(0,0,0,0%);
            background-image: url("res/path20.png");
            background-repeat: no-repeat;
            border: 5px solid rgba(0,0,0,0%);
            border-radius: 0px;
            padding: 0px;
            text-align: center;
            '''

        )

class PicButton(QAbstractButton):
    def __init__(self, pixmap, parent=None):
        super(PicButton, self).__init__(parent)
        self.pixmap = pixmap

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)

    def sizeHint(self):
        return self.pixmap.size()
# class PopupRapper()


class windowFrame(QWidget):
    def __init__(self):
        super(windowFrame, self).__init__()
        self.initUI()
        self.oPos = self.pos()

    def initUI(self):
        winwidth = 1590
        winheight = 1100
        VBox = QVBoxLayout()
        nonConformalWindow = Rapper(self)
        VBox.addWidget(nonConformalWindow)
        self.setLayout(VBox)
        self.setWindowFlags(
            Qt.FramelessWindowHint
            # | Qt.WA_TranslucentBackground
            # | Qt.WindowStaysOnTopHint
            # | Qt.SplashScreen
            # | Qt.AA_DisableHighDpiScaling  # for testing
            # | Qt.AbsoluteSize  # may be needed for lower res devices than surface
            # | Qt.ActionsContextMenu  # don't know what this does todo figure that out
        )
        # alt way to make base window transparent. todo figure out which works best
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setGeometry(100, 100, winwidth, winheight)
        self.setWindowTitle('Gooey GPA')

        #btn = QPushButton('Close')
        btn = PicButton(QPixmap('res/x.png'), self)
        VBox.addChildWidget(btn)
        btn.clicked.connect(self.stubz)
        btn.setGeometry(32, 182, 20, 20)


        teMath = QLineEdit()
        VBox.addChildWidget(teMath)
        teMath.setGeometry(90, 300, 350, 35)
        teMath.setPlaceholderText('Enter your Math score')
        teMath.setStyleSheet(
            '''
            background-color: rgba(26,26,26,20%);
            color: rgb(245,245,245);
            border: 0px solid rgbs(0,0,0,0%)
            
            '''
        )

        teSS = QLineEdit()
        VBox.addChildWidget(teSS)
        teSS.setGeometry(90, 400, 350, 35)
        teSS.setPlaceholderText('Enter your Social Studies score')
        teSS.setStyleSheet(
            '''
            background-color: rgba(26,26,26,20%);
            color: rgb(245,245,245);
            border: 0px solid rgbs(0,0,0,0%)

            '''
        )

        teLang = QLineEdit()
        VBox.addChildWidget(teLang)
        teLang.setGeometry(90, 500, 350, 35)
        teLang.setPlaceholderText('Enter your Math score')
        teLang.setStyleSheet(
            '''
            background-color: rgba(26,26,26,20%);
            color: rgb(245,245,245);
            border: 0px solid rgbs(0,0,0,0%)

            '''
        )

        teSci = QLineEdit()
        VBox.addChildWidget(teSci)
        teSci.setGeometry(90, 600, 350, 35)
        teSci.setPlaceholderText('Enter your Math score')
        teSci.setStyleSheet(
            '''
            background-color: rgba(26,26,26,20%);
            color: rgb(245,245,245);
            border: 0px solid rgbs(0,0,0,0%)

            '''
        )

        self.show()

    def stubz(self):
        sys.exit()

    # This makes the window movable
    # todo Implement proper button handling
    def mousePressEvent(self, event):
        self.oPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oPos = event.globalPos()


def other(QWidget):
    lo = QHBoxLayout
    QWidget.setLayout(lo)
    btn = QPushButton('hi')

    lo.addWidget(btn)
    other.show()


# def openDialog():


def main():
    app = QApplication(sys.argv)
    alldone = windowFrame()  # Unused but I'm sure it will be usefull later
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
