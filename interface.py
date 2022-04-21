# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\titou\PycharmProjects\info_jetpack\interface.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_principale_ihm(object):
    def setupUi(self, principale_ihm):
        principale_ihm.setObjectName("principale_ihm")
        principale_ihm.resize(1080, 720)
        font = QtGui.QFont()
        font.setFamily("Sansation")
        principale_ihm.setFont(font)
        principale_ihm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\titou\\PycharmProjects\\info_jetpack\\../../OneDrive - Ecole Nationale Supérieure de Techniques Avancées Bretagne/Bureau/Jetpack_Joyride_iOS.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        principale_ihm.setWindowIcon(icon)
        principale_ihm.setWindowOpacity(-2.0)
        self.centralwidget = QtWidgets.QWidget(principale_ihm)
        self.centralwidget.setObjectName("centralwidget")
        self.conteneur = QtWidgets.QWidget(self.centralwidget)
        self.conteneur.setEnabled(True)
        self.conteneur.setGeometry(QtCore.QRect(10, 10, 4520, 30))
        self.conteneur.setObjectName("conteneur")
        self.layoutWidget = QtWidgets.QWidget(self.conteneur)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 471, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bouton_gen_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.bouton_gen_2.setObjectName("bouton_gen_2")
        self.horizontalLayout.addWidget(self.bouton_gen_2)
        self.bouton_pas = QtWidgets.QPushButton(self.layoutWidget)
        self.bouton_pas.setObjectName("bouton_pas")
        self.horizontalLayout.addWidget(self.bouton_pas)
        self.bouton_sim = QtWidgets.QPushButton(self.layoutWidget)
        self.bouton_sim.setObjectName("bouton_sim")
        self.horizontalLayout.addWidget(self.bouton_sim)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.bouton_qui = QtWidgets.QPushButton(self.layoutWidget)
        self.bouton_qui.setObjectName("bouton_qui")
        self.horizontalLayout.addWidget(self.bouton_qui)
        principale_ihm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(principale_ihm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 23))
        self.menubar.setObjectName("menubar")
        self.menuFichiers = QtWidgets.QMenu(self.menubar)
        self.menuFichiers.setObjectName("menuFichiers")
        principale_ihm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(principale_ihm)
        self.statusbar.setObjectName("statusbar")
        principale_ihm.setStatusBar(self.statusbar)
        self.actionQuitter = QtWidgets.QAction(principale_ihm)
        self.actionQuitter.setObjectName("actionQuitter")
        self.menuFichiers.addAction(self.actionQuitter)
        self.menubar.addAction(self.menuFichiers.menuAction())

        self.retranslateUi(principale_ihm)
        self.bouton_qui.clicked.connect(principale_ihm.close)
        self.actionQuitter.triggered.connect(principale_ihm.close)
        QtCore.QMetaObject.connectSlotsByName(principale_ihm)

    def retranslateUi(self, principale_ihm):
        _translate = QtCore.QCoreApplication.translate
        principale_ihm.setWindowTitle(_translate("principale_ihm", "Ecosysteme"))
        self.bouton_gen_2.setText(_translate("principale_ihm", "Générer"))
        self.bouton_pas.setText(_translate("principale_ihm", "Un pas"))
        self.bouton_sim.setText(_translate("principale_ihm", "Simuler"))
        self.bouton_qui.setText(_translate("principale_ihm", "Quitter"))
        self.menuFichiers.setTitle(_translate("principale_ihm", "Fichiers"))
        self.actionQuitter.setText(_translate("principale_ihm", "Quitter"))
        self.actionQuitter.setShortcut(_translate("principale_ihm", "Ctrl+Q"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    principale_ihm = QtWidgets.QMainWindow()
    ui = Ui_principale_ihm()
    ui.setupUi(principale_ihm)
    principale_ihm.show()
    sys.exit(app.exec_())
