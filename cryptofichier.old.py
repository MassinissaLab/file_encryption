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
    global   rsapc,rsapr,FilePath,L
    def __init__(self):
        super(Ui_cryptofichier, self).__init__()
        loadUi("cryptofichier.ui", self)
        self.L=[]
        self.FilePath=""
        self.msg_0.hide()
        self.msg_1.hide()
        self.msg_2.hide()
        self.msg_3.hide()
        self.msg_4.hide()
        
        self.exit.clicked.connect(self.close)
        self.reduit.clicked.connect(self.showMinimized)
       
    
        self.confirmer_btn.clicked.connect(self.generercles)
        self.parcourire_btn.clicked.connect(self.choisirchemin)
        
        self.crypter_btn.clicked.connect(self.crypterf)
        self.decrypter_btn.clicked.connect(self.decrypterf)
        
        
        self.setWindowFlags(Qt.FramelessWindowHint)

    

        
    def generercles(self):
        self.msg_0.hide()
        
        
        
        try:
            public, private = generer_cles(self.rsap.value(), self.rsaq.value())
            self.rsapc=(public[0], public[1])
            self.rsapr=(private[0], private[1])
            self.clepub.setText(str(self.rsapc))
            self.cleprv.setText(str(self.rsapr))


        except :
              self.msg_0.show() 
              

    def crypterf(self):
        self.FilePath=self.chemin.text()
        self.msg_1.hide()
        self.msg_2.hide()
        self.msg_3.hide()
        self.msg_4.hide()
        print(self.FilePath)
        print(self.rsapc)
        if self.FilePath=="":
            self.msg_1.show()
        else:
            #extension=os.path.splitext(self.FilePath)
            #if ".txt" in extension[1]:
            """try:
                


            except :
                self.msg_2.show()"""

            with open(self.FilePath,'r') as myfile:
                    
                    
                    
                    Lines = myfile.readlines()
                    count = 0
                    for line in Lines:
                        count += 1
                        #print("Line{}: {}".format(count, line.strip()))
                        encrypted_msg=encrypt(self.rsapc, line.strip())
                        #D:/WorkSpaces/Python workspace/tests/test.txt
                        print("encrypted")
                        print(encrypted_msg)
                        print("joined")
                        print(''.join(map(lambda x: str(x), encrypted_msg)))
                        x=''
                        for i in encrypted_msg:
                            if(i=='400'):
                                x+=' '
                            else:

                                c=chr(i)
                                x+=c
                        
                        print("x")
                        print(x)
                        #self.L.append(''.join(map(lambda x: chr(x), encrypted_msg))+'\n')

                        
                    print(self.L)      
                    if self.L==[]:
                        self.msg_2.show()
                    else:    
                        fcript = open('fcypt.txt', 'w')
                        fcript.writelines(self.L)
                        fcript .close()
                        self.msg_3.show()
            
        

    def decrypterf(self):
        self.FilePath=self.chemin.text()
        self.msg_0.hide()
        self.msg_1.hide()
        self.msg_2.hide()
        self.msg_3.hide()
        self.msg_4.hide()
        if self.FilePath=="":
            self.msg_1.show()
        else:
            extension=os.path.splitext(self.FilePath)
            if ".txt" in extension[1]:
                try:
                    with open(self.FilePath, 'r') as myfile:
                        data = myfile.read()
                   
                    encrypted_msg=decrypt(self.rsapr, data)
                    
                    
                    
                    os.remove(self.FilePath)
                    with open(self.FilePath, 'w') as outputfile:
                        outputfile.write(str(txt))
                    self.msg_4.show()


                except :
                    self.msg_2.show()
   
        
    

    def ouvrir(self):
        self.FilePath=self.chemin.text()
        self.msg_0.hide()
        self.msg_1.hide()
        self.msg_2.hide()
        self.msg_3.hide()
        self.msg_4.hide()
        if self.FilePath=="":
            self.msg_1.show()
        else:
            extension=os.path.splitext(self.FilePath)
            if ".txt" in extension[1]:
                try:
                    if sys.platform == "win32":
                        
                        os.startfile(self.FilePath)
                        
                except :
                    self.msg_2.show()
    
        
        
    def choisirchemin(self):
        self.msg_1.hide()
        self.msg_2.hide()
        self.msg_3.hide()
        self.msg_4.hide()
        self.FilePath,Filetype = QFileDialog.getOpenFileName(self)
        self.chemin.setText(self.FilePath)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = Ui_cryptofichier()
    myapp.show()
    sys.exit(app.exec_())
