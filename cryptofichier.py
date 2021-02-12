# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cryptofichier.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CRYPTOFICHIER(object):
    global   rsapc,rsapr,FilePath,L
    def setupUi(self, CRYPTOFICHIER):

        
        CRYPTOFICHIER.setObjectName("CRYPTOFICHIER")
        CRYPTOFICHIER.resize(682, 362)
        CRYPTOFICHIER.setStyleSheet("background-color: rgb(6, 100, 135);")

        self.centralwidget = QtWidgets.QWidget(CRYPTOFICHIER)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 681, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("C:/Users/ML/.designer/backup/image/32CYPHER.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_35 = QtWidgets.QLabel(self.layoutWidget)
        self.label_35.setStyleSheet("color: rgb(0, 255, 0);\n"
"background:transparent;\n"
"font: 75 16pt \"Century Gothic\";\n"
"")
        self.label_35.setObjectName("label_35")
        self.horizontalLayout.addWidget(self.label_35)
        self.label_68 = QtWidgets.QLabel(self.layoutWidget)
        self.label_68.setStyleSheet("color: #ffffff;\n"
"background:transparent;\n"
"font: 75 16pt \"Century Gothic\";\n"
"")
        self.label_68.setObjectName("label_68")
        self.horizontalLayout.addWidget(self.label_68)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.reduit = QtWidgets.QPushButton(self.layoutWidget)
        self.reduit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/ML/.designer/backup/image/tire_dwit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reduit.setIcon(icon)
        self.reduit.setIconSize(QtCore.QSize(20, 20))
        self.reduit.setObjectName("reduit")
        self.horizontalLayout.addWidget(self.reduit)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.exit = QtWidgets.QPushButton(self.layoutWidget)
        self.exit.setAutoFillBackground(False)
        self.exit.setStyleSheet("")
        self.exit.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/ML/.designer/backup/image/close.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon1)
        self.exit.setIconSize(QtCore.QSize(20, 20))
        self.exit.setAutoRepeat(False)
        self.exit.setAutoExclusive(True)
        self.exit.setAutoRepeatDelay(12)
        self.exit.setAutoRepeatInterval(12)
        self.exit.setAutoDefault(False)
        self.exit.setDefault(False)
        self.exit.setFlat(False)
        self.exit.setObjectName("exit")
        self.horizontalLayout.addWidget(self.exit)
        self.decrypter_btn = QtWidgets.QPushButton(self.centralwidget)
        self.decrypter_btn.setEnabled(True)
        self.decrypter_btn.setGeometry(QtCore.QRect(530, 270, 121, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.decrypter_btn.sizePolicy().hasHeightForWidth())
        self.decrypter_btn.setSizePolicy(sizePolicy)
        self.decrypter_btn.setStyleSheet("font: 14pt \"5by7\";\n"
"color: rgb(255, 255, 255);")
        self.decrypter_btn.setCheckable(False)
        self.decrypter_btn.setDefault(True)
        self.decrypter_btn.setObjectName("decrypter_btn")
        self.crypter_btn = QtWidgets.QPushButton(self.centralwidget)
        self.crypter_btn.setEnabled(True)
        self.crypter_btn.setGeometry(QtCore.QRect(390, 270, 121, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.crypter_btn.sizePolicy().hasHeightForWidth())
        self.crypter_btn.setSizePolicy(sizePolicy)
        self.crypter_btn.setStyleSheet("font: 14pt \"5by7\";\n"
"color: rgb(255, 255, 255);font: 14pt \"5by7\";\n"
"")
        self.crypter_btn.setCheckable(False)
        self.crypter_btn.setDefault(True)
        self.crypter_btn.setObjectName("crypter_btn")
        self.msg_3 = QtWidgets.QLabel(self.centralwidget)
        self.msg_3.setEnabled(False)
        self.msg_3.setGeometry(QtCore.QRect(10, 290, 281, 31))
        self.msg_3.setStyleSheet("background: rgba(0, 170, 0,0.7);\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"font: 12pt \"Century Gothic\";")
        self.msg_3.setObjectName("msg_3")
        self.msg_1 = QtWidgets.QLabel(self.centralwidget)
        self.msg_1.setEnabled(False)
        self.msg_1.setGeometry(QtCore.QRect(10, 260, 291, 31))
        self.msg_1.setStyleSheet("background:rgba(255,0,0,0.8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"font: 12pt \"Century Gothic\";")
        self.msg_1.setObjectName("msg_1")
        self.msg_2 = QtWidgets.QLabel(self.centralwidget)
        self.msg_2.setEnabled(False)
        self.msg_2.setGeometry(QtCore.QRect(10, 260, 171, 31))
        self.msg_2.setStyleSheet("background:rgba(255,0,0,0.8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"font: 12pt \"Century Gothic\";")
        self.msg_2.setObjectName("msg_2")
        self.msg_4 = QtWidgets.QLabel(self.centralwidget)
        self.msg_4.setEnabled(False)
        self.msg_4.setGeometry(QtCore.QRect(10, 290, 301, 31))
        self.msg_4.setStyleSheet("background: rgba(0, 170, 0,0.7);\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"font: 12pt \"Century Gothic\";")
        self.msg_4.setObjectName("msg_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 150, 121, 31))
        self.label_4.setStyleSheet("background:transparent;\n"
"font: 14pt \"5by7\";\n"
"\n"
"font: 14pt \"Century Gothic\";\n"
"\n"
"color:#ffffff;")
        self.label_4.setObjectName("label_4")
        self.rsap = QtWidgets.QSpinBox(self.centralwidget)
        self.rsap.setGeometry(QtCore.QRect(290, 90, 111, 31))
        self.rsap.setWhatsThis("")
        self.rsap.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"border:1px solid #9cd3e2;\n"
"background-color: rgb(33, 65, 103);")
        self.rsap.setReadOnly(False)
        self.rsap.setProperty("showGroupSeparator", True)
        self.rsap.setMinimum(1)
        self.rsap.setMaximum(99999)
        self.rsap.setProperty("value", 11)
        self.rsap.setObjectName("rsap")
        self.clepub = QtWidgets.QLabel(self.centralwidget)
        self.clepub.setGeometry(QtCore.QRect(350, 150, 101, 31))
        self.clepub.setStyleSheet("color: rgb(0, 255, 0);\n"
"background:transparent;\n"
"font: 75 16pt \"Century Gothic\";")
        self.clepub.setObjectName("clepub")
        self.chemin = QtWidgets.QLineEdit(self.centralwidget)
        self.chemin.setEnabled(True)
        self.chemin.setGeometry(QtCore.QRect(10, 210, 491, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chemin.sizePolicy().hasHeightForWidth())
        self.chemin.setSizePolicy(sizePolicy)
        self.chemin.setSizeIncrement(QtCore.QSize(15, 15))
        self.chemin.setBaseSize(QtCore.QSize(15, 15))
        self.chemin.setMouseTracking(False)
        self.chemin.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chemin.setAutoFillBackground(False)
        self.chemin.setStyleSheet("\n"
"\n"
"color:#ffffff;\n"
"border-radius: 0px;\n"
"border:1px solid #9cd3e2;\n"
"background-color: rgb(33, 65, 103);\n"
"font: 12pt \"Century Gothic\";")
        self.chemin.setInputMask("")
        self.chemin.setText("")
        self.chemin.setMaxLength(999999999)
        self.chemin.setFrame(True)
        self.chemin.setCursorPosition(0)
        self.chemin.setPlaceholderText("chemin de fichier")
        self.chemin.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.chemin.setClearButtonEnabled(False)
        self.chemin.setObjectName("chemin")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 90, 271, 31))
        self.label.setStyleSheet("background:transparent;\n"
"font: 14pt \"5by7\";\n"
"\n"
"font: 14pt \"Century Gothic\";\n"
"\n"
"color:#ffffff;")
        self.label.setObjectName("label")
        self.parcourire_btn = QtWidgets.QPushButton(self.centralwidget)
        self.parcourire_btn.setEnabled(True)
        self.parcourire_btn.setGeometry(QtCore.QRect(510, 210, 161, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parcourire_btn.sizePolicy().hasHeightForWidth())
        self.parcourire_btn.setSizePolicy(sizePolicy)
        self.parcourire_btn.setStyleSheet("font: 14pt \"5by7\";\n"
"color: rgb(255, 255, 255);")
        self.parcourire_btn.setCheckable(False)
        self.parcourire_btn.setDefault(True)
        self.parcourire_btn.setObjectName("parcourire_btn")
        self.confirmer_btn = QtWidgets.QPushButton(self.centralwidget)
        self.confirmer_btn.setGeometry(QtCore.QRect(540, 90, 121, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirmer_btn.sizePolicy().hasHeightForWidth())
        self.confirmer_btn.setSizePolicy(sizePolicy)
        self.confirmer_btn.setStyleSheet("font: 14pt \"5by7\";\n"
"color: rgb(255, 255, 255);")
        self.confirmer_btn.setCheckable(False)
        self.confirmer_btn.setDefault(True)
        self.confirmer_btn.setObjectName("confirmer_btn")
        self.rsaq = QtWidgets.QSpinBox(self.centralwidget)
        self.rsaq.setGeometry(QtCore.QRect(420, 90, 111, 31))
        self.rsaq.setStyleSheet("\n"
"\n"
"color: rgb(255, 255, 255);border-radius: 0px;\n"
"border:1px solid #9cd3e2;\n"
"background-color: rgb(33, 65, 103);")
        self.rsaq.setReadOnly(False)
        self.rsaq.setProperty("showGroupSeparator", True)
        self.rsaq.setMinimum(1)
        self.rsaq.setMaximum(99999)
        self.rsaq.setProperty("value", 17)
        self.rsaq.setObjectName("rsaq")
        self.cleprv = QtWidgets.QLabel(self.centralwidget)
        self.cleprv.setGeometry(QtCore.QRect(110, 150, 101, 31))
        self.cleprv.setStyleSheet("color: rgb(255, 0, 0);\n"
"background:transparent;\n"
"font: 75 16pt \"Century Gothic\";")
        self.cleprv.setObjectName("cleprv")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 101, 31))
        self.label_3.setStyleSheet("background:transparent;\n"
"font: 14pt \"5by7\";\n"
"\n"
"font: 14pt \"Century Gothic\";\n"
"\n"
"color:#ffffff;")
        self.label_3.setObjectName("label_3")
        self.msg_0 = QtWidgets.QLabel(self.centralwidget)
        self.msg_0.setEnabled(False)
        self.msg_0.setGeometry(QtCore.QRect(290, 50, 231, 31))
        self.msg_0.setStyleSheet("background:rgba(255,0,0,0.8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"font: 14pt \"5by7\";\n"
"font: 12pt \"Century Gothic\";")
        self.msg_0.setObjectName("msg_0")
        CRYPTOFICHIER.setCentralWidget(self.centralwidget)

        self.retranslateUi(CRYPTOFICHIER)
        QtCore.QMetaObject.connectSlotsByName(CRYPTOFICHIER)
       
    def retranslateUi(self, CRYPTOFICHIER):
        self.L=[]
        self.FilePath=""

        _translate = QtCore.QCoreApplication.translate
        CRYPTOFICHIER.setWindowTitle(_translate("CRYPTOFICHIER", "CRYPTOFICHIER"))
        CRYPTOFICHIER.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.label_35.setText(_translate("CRYPTOFICHIER", "Cryptage "))
        self.label_68.setText(_translate("CRYPTOFICHIER", "Fichier"))
        self.reduit.setShortcut(_translate("CRYPTOFICHIER", "Ctrl+S, Ctrl+S"))
        self.decrypter_btn.setText(_translate("CRYPTOFICHIER", "Decrypter"))
        self.decrypter_btn.setShortcut(_translate("CRYPTOFICHIER", "Return"))
        self.crypter_btn.setText(_translate("CRYPTOFICHIER", "Crypter"))
        self.crypter_btn.setShortcut(_translate("CRYPTOFICHIER", "Return"))
        self.msg_3.setText(_translate("CRYPTOFICHIER", " Le fichier a été crypté avec succes"))
        self.msg_1.setText(_translate("CRYPTOFICHIER", " Entrer le chemin d\'abord "))
        self.msg_2.setText(_translate("CRYPTOFICHIER", " le fichier n\'existe pas "))
        self.msg_4.setText(_translate("CRYPTOFICHIER", " Le fichier a été decrypté avec succes"))
        self.label_4.setText(_translate("CRYPTOFICHIER", "Clé Publique"))
        self.clepub.setText(_translate("CRYPTOFICHIER", "pck"))
        self.label.setText(_translate("CRYPTOFICHIER", "Donner les valeurs P et Q :"))
        self.parcourire_btn.setText(_translate("CRYPTOFICHIER", "Parcourire"))
        self.parcourire_btn.setShortcut(_translate("CRYPTOFICHIER", "Return"))
        self.confirmer_btn.setText(_translate("CRYPTOFICHIER", "Confirme ✔"))
        self.confirmer_btn.setShortcut(_translate("CRYPTOFICHIER", "Return"))
        self.cleprv.setText(_translate("CRYPTOFICHIER", "prk"))
        self.label_3.setText(_translate("CRYPTOFICHIER", "Clé Privée"))
        self.msg_0.setText(_translate("CRYPTOFICHIER", "  p et q doive etre premier"))
        self.msg_0.hide()
        self.msg_1.hide()
        self.msg_2.hide()
        self.msg_3.hide()
        self.msg_4.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CRYPTOFICHIER = QtWidgets.QMainWindow()
    ui = Ui_CRYPTOFICHIER()
    ui.setupUi(CRYPTOFICHIER)

    CRYPTOFICHIER.show()
    sys.exit(app.exec_())
