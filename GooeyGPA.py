import sys
import os
import platform
import json
import PyQt5

from PyQt5.QtWidgets import QVBoxLayout, QLabel, QDesktopWidget, QWidget, QApplication
from PyQt5.QtCore import Qt, QPoint


class Rapper(QLabel):
    def __init__(self, parent):
        QLabel.__init__(self, parent)
        # thanks im_dead_sirius!
        self.setStyleSheet(
            '''
            color: rgba(0,0,0,100%);
            background-color: rgba(0,0,0,0%);
            background-image: url("res/path52.png");
            border: 5px solid rgba(0,0,0,100%);
            border-radius: 428px;
            padding: 0px;
            text-align: center;
            '''
        )


class windowFrame(QWidget):
    def __init__(self):
        super(windowFrame, self).__init__()
        self.initUI()
        self.oPos = self.pos()

    def initUI(self):
        winwidth = 915
        winheight = 1024
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
        self.setGeometry(0, 0, winwidth, winheight)
        self.setWindowTitle('Gooey GPA')
        self.show()

    # This makes the window movable
    # todo Implement proper button handling
    def mousePressEvent(self, event):
        self.oPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oPos = event.globalPos()


def main():
    app = QApplication(sys.argv)
    alldone = windowFrame()  # Unused but I'm sure it will be usefull later
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
