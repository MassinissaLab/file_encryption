from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto import Random
import base64
import docx



def newkeys(keysize):
   random_generator = Random.new().read
   key = RSA.generate(keysize, random_generator)
   private, public = key, key.publickey()


   f = open('public.pem','wb')
   f.write(public.export_key('PEM'))
   f.close()

   f = open('private.pem','wb')
   f.write(private.export_key('PEM'))
   f.close()

   return public, private

def importKey(pathKey):
   f = open(pathKey,'r')
   key = RSA.import_key(f.read())

   return key

def getpublickey(priv_key):
   return priv_key.publickey()

def encrypt(message, pub_key):
   cipher = PKCS1_OAEP.new(pub_key)

   return cipher.encrypt(message)

def decrypt(ciphertext, priv_key):
   cipher = PKCS1_OAEP.new(priv_key)
   return cipher.decrypt(ciphertext)

fichier="D:/WorkSpaces/Python workspace/tests/test.docx"
crypter="crypter.docx"
doc =docx.Document(fichier)
ClearText =[]
cc=[]
for p in doc.paragraphs :
	ClearText.append(p.text)

for el in ClearText:
	
	cc.append(el.split(" "))

public, private =newkeys(1024)

print(cc)
pk=importKey('public.pem')


docc = docx.Document() 
        


result=[]
print ("********************************  ENCRYPT  ************************************")
for p in cc:
	pf=[]
	for e in p :
		
		pf.extend(str(base64.b64encode(encrypt(e.encode('utf-8'),public)), encoding='utf-8')+" ")

	result.append(pf)

print(result)
for pp in result :
	para = docc.add_paragraph().add_run(pp)
docc.save(crypter)

print("*********************************  DECRYPT  ************************************ \n")


crypt="crypter.docx"
docc =docx.Document(crypt)

CypherText =[]
ccc=[]
for p in docc.paragraphs :
	CypherText.append(p.text)




for el in CypherText:

	
	ccc.append(el.split(" "))




cpt=0
for elm in ccc:
	for l in elm:
	 	cpt+=1

print(cpt)	
print(ccc)

"""
d=""
for e in CypherText:
	print(decrypt(base64.b64decode(e),private).decode('utf-8')+" ")


"""