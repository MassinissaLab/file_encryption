from PyQt5.QtGui import *
import os
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import time
import os,subprocess,sys
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from RSA import *
import codecs
import docx 
class Ui_cryptofichier(QMainWindow):
    global   rsapc,rsapr,FilePath,ResultPath
    def __init__(self):
        super(Ui_cryptofichier, self).__init__()
        loadUi("cryptofichier.ui", self)
        self.FilePath=""
        self.ResultPath=""
        
        self.msg_1.hide()
        self.msg_2.hide()
        self.msg_3.hide()
        self.msg_4.hide()
        self.msg_5.hide()
        self.msg_6.hide()
       
    
        self.confirmer_btn.clicked.connect(self.generercles)

        self.pubkey.clicked.connect(self.choisirchemin)
        self.prvkey.clicked.connect(self.choisirchemin)
        self.parcourire_btn.clicked.connect(self.choisirchemin)
        self.parcourire_btn_2.clicked.connect(self.choisirchemin)

        self.crypter_btn.clicked.connect(self.crypterf)
        self.decrypter_btn.clicked.connect(self.decrypterf)
          
    def generercles(self):
        
        public, private =newkeys(1024)


              

    def crypterf(self):
        self.msg_1.hide()
        self.msg_2.hide()
        self.msg_3.hide()
        self.msg_4.hide()
        self.msg_5.hide()
        self.msg_6.hide()

        self.FilePath=self.chemin.text()
        self.ResultPath=self.rchemin.text()


        ext1=os.path.splitext(self.FilePath)
        ext2=os.path.splitext(self.ResultPath)
        ext3=os.path.splitext(self.rsapc)
        ext4=os.path.splitext(self.rsapr)

        if self.FilePath=="":
            self.msg_1.show()
        elif self.ResultPath=="":
            self.msg_5.show()
        else:
            if(".docx" not in ext1[1] or ".docx" not in ext2[1]) :
                self.msg_2.show()
            elif ".pem" not in ext3[1]:
                self.msg_6.show()
            else :
                print("encrypt")
                doc =docx.Document(FilePath)
                ClearText =[]
                cc=[]

                for p in doc.paragraphs :
                    ClearText.append(p.text)

                for el in ClearText:
                    
                    cc.append(el.split(" "))

                public, private =newkeys(1024)

                
                pk=importKey(self.rsapc)


                docc = docx.Document() 
                        


                result=[]
                
                for p in cc:
                    pf=[]
                    for e in p :
                        
                        pf.extend(str(base64.b64encode(encrypt(e.encode('utf-8'),public)), encoding='utf-8')+" ")

                    result.append(pf)

                print(result)
                for pp in result :
                    para = docc.add_paragraph().add_run(pp)
                docc.save(self.ResultPath)

                self.msg_3.show()



    def decrypterf(self):
        self.msg_1.hide()
        self.msg_2.hide()
        self.msg_3.hide()
        self.msg_4.hide()
        self.msg_5.hide()
        self.msg_6.hide()

        self.FilePath=self.chemin.text()
        self.ResultPath=self.rchemin.text()
        

        extension=os.path.splitext(self.FilePath)
        extr=os.path.splitext(self.ResultPath)

        if(".docx" not in extension[1] or ".docx" not in extr[1]):
            self.msg_2.show()
        else :
            print("decrypt")
                
        
    def choisirchemin(self):
        self.msg_1.hide()
        self.msg_2.hide()
        self.msg_3.hide()
        self.msg_4.hide()
        self.msg_5.hide()
        self.msg_6.hide()
        FPath,Ftype = QFileDialog.getOpenFileName(self)
        

        if self.parcourire_btn.isChecked():
            
            self.chemin.setText(FPath)


        if self.parcourire_btn_2.isChecked():
            self.rchemin.setText(FPath)
           


        if self.pubkey.isChecked():
           self.chemin_pubkey.setText(FPath)
           self.rsapc=importKey(self.chemin_pubkey.text())


        if self.prvkey.isChecked():
            self.chemin_prvkey.setText(FPath)
            self.rsapr=importKey(self.chemin_prvkey.text())



        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = Ui_cryptofichier()
    myapp.show()
    sys.exit(app.exec_())
