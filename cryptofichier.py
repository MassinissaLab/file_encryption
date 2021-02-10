from PyQt5.QtGui import *
import os
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import time
import os,subprocess,sys
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from RSA import *
import pickle

class Ui_cryptofichier(QMainWindow):
    global   rsapc,rsapr,FilePath
    def __init__(self):
        super(Ui_cryptofichier, self).__init__()
        loadUi("cryptofichier.ui", self)
      
        self.FilePath=""
        self.msg_erreur.hide()
       
        self.msg_11.hide()
        self.msg_13.hide()
        self.msg_14.hide()
        self.msg_15.hide()
        
        self.exit.clicked.connect(self.close)
        self.reduit.clicked.connect(self.showMinimized)
       
    
        #self.confirmer_btn.clicked.connect()
        self.parcourire_btn.clicked.connect(self.choisirchemin)
        
        self.crypter_btn.clicked.connect(self.crypterf)
        self.decrypter_btn.clicked.connect(self.decrypterf)
        
        
        self.setWindowFlags(Qt.FramelessWindowHint)

    

        
    
    def crypterf(self):
        self.FilePath=self.chemin.text()
        self.msg_11.hide()
        self.msg_13.hide()
        self.msg_14.hide()
        self.msg_15.hide()
        if self.FilePath=="":
            self.msg_11.show()
        else:
            extension=os.path.splitext(self.FilePath)
            if ".txt" in extension[1]:
                try:
                    with open(self.FilePath, 'r') as myfile:
                        data = myfile.read()

                        encrypted_msg=encrypt(self.rsapc, data)
                        txt='µ'.join(map(lambda x: str(x), encrypted_msg))
                
                    
                    os.remove(self.FilePath)
                    with open(self.FilePath, 'w') as outputfile:
                        outputfile.write(str(txt))
                    self.msg_14.show()


                except :
                    self.msg_13.show()
            else :
                self.msg_12.show()      
        

    def decrypterf(self):
        self.FilePath=self.chemin.text()
        self.msg_11.hide()
        self.msg_13.hide()
        self.msg_14.hide()
        self.msg_15.hide()
        if self.FilePath=="":
            self.msg_11.show()
        else:
            extension=os.path.splitext(self.FilePath)
            if ".txt" in extension[1]:
                try:
                    with open(self.FilePath, 'r') as myfile:
                        data = myfile.read()
                   
                    encrypted_msg=decrypt(self.rsapc, data)
                    txt='µ'.join(map(lambda x: str(x), encrypted_msg))
                    
                    
                    os.remove(self.FilePath)
                    with open(self.FilePath, 'w') as outputfile:
                        outputfile.write(str(txt))
                    self.msg_15.show()


                except :
                    self.msg_13.show()
            else :
                self.msg_12.show()      
        
    

    def ouvrir(self):
        self.FilePath=self.chemin.text()
        self.msg_11.hide()
        self.msg_13.hide()
        self.msg_14.hide()
        self.msg_15.hide()
        if self.FilePath=="":
            self.msg_11.show()
        else:
            extension=os.path.splitext(self.FilePath)
            if ".txt" in extension[1]:
                try:
                    if sys.platform == "win32":
                        
                        os.startfile(self.FilePath)
                        
                except :
                    self.msg_13.show()
            else :
                self.msg_12.show()      
        
        
    def choisirchemin(self):
        self.msg_11.hide()
        self.msg_13.hide()
        self.msg_14.hide()
        self.msg_15.hide()
        self.FilePath,type = QFileDialog.getOpenFileName(self)
        self.chemin.setText(self.FilePath)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = Ui_cryptofichier()
    myapp.show()
    sys.exit(app.exec_())
