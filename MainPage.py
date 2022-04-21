# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\titou\PycharmProjects\info_jetpack\MainPage.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1080, 720)
        Main.setMinimumSize(QtCore.QSize(1080, 720))
        Main.setMaximumSize(QtCore.QSize(1080, 720))
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, -10, 1081, 681))
        font = QtGui.QFont()
        font.setFamily("Sansation")
        font.setPointSize(28)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-image: url(:/newPrefix/fond.png);\n"
"border-color: rgb(177, 200, 181);\n"
"color: rgb(250,250,250);")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 26))
        self.menubar.setObjectName("menubar")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "MainWindow"))
        self.pushButton.setText(_translate("Main", "STORY OF QUENTOUAN BELAUMAY"))

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())
