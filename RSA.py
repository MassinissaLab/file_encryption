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


