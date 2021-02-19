from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto import Random
from base64 import b64encode, b64decode
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

filename="D:/WorkSpaces/Python workspace/tests/test.docx"

doc =docx.Document(filename)
ClearText =[]
cc=[]
for p in doc.paragraphs :
	ClearText.append(p.text)

for el in ClearText:
	
	cc.append(el.split(" "))

public, private =newkeys(1024)

print(public,private)
pk=importKey('public.pem')




result=[]
print ("********************************  ENCRYPT  ************************************")
for p in cc:
	for e in p :
		print(e)
		result.append(encrypt(e.encode('utf-8'),pk))

print(result)


print("*********************************  DECRYPT  ************************************")
d=""
for e in result:
	d+=decrypt(e,private).decode('utf-8')+" "


print(d)