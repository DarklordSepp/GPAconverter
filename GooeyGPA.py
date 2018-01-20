import sys
import os
import platform
import json
import PyQt5
import GooeyPrompt
import test

from PyQt5.QtWidgets import QVBoxLayout, QLabel, QDesktopWidget, QWidget, QApplication, QInputDialog, QLineEdit, \
    QPushButton, QFormLayout, QHBoxLayout
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
            border: 5px solid rgba(0,0,0,0%);
            border-radius: 428px;
            padding: 0px;
            text-align: center;
            '''
        )

# class PopupRapper()


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
        #self.setWindowFlags(
            #Qt.FramelessWindowHint
            # | Qt.WA_TranslucentBackground
            # | Qt.WindowStaysOnTopHint
            # | Qt.SplashScreen
            # | Qt.AA_DisableHighDpiScaling  # for testing
            # | Qt.AbsoluteSize  # may be needed for lower res devices than surface
            # | Qt.ActionsContextMenu  # don't know what this does todo figure that out
       # )
        # alt way to make base window transparent. todo figure out which works best
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setGeometry(100, 100, winwidth, winheight)
        self.setWindowTitle('Gooey GPA')

        self.btn = QPushButton('test')
        self.btn.clicked.connect(self.testr)
        VBox.addWidget(self.btn)
        Cbox = QHBoxLayout()
        VBox.addChildLayout(Cbox)

        self.show()

# class Chrome(QWidget):
#     def __init__(self, parent = windowFrame):
#         super(Chrome, self).__init__(self)
#
#         lo = QFormLayout()
#         self.btn = QPushButton('test')
#         self.btn.clicked.connect(self.getint())
#         self.setLayout(lo)

# class ipDia(QInputDialog):
#     def __init__(self):
#         super(ipDia, self)
#         lo = Q


    def testr(self):
        class StartSub2(QLabel, GooeyPrompt.BubbleFrame):
            def __init__(self, parent=None):
                QLabel.__init__(self, parent)
                self.setupUi(self)
        StartSub2(self)

    # This makes the window movable
    # todo Implement proper button handling
    def mousePressEvent(self, event):
        self.oPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oPos = event.globalPos()




#def openDialog():






def main():


    app = QApplication(sys.argv)
    alldone = windowFrame()  # Unused but I'm sure it will be usefull later
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()



