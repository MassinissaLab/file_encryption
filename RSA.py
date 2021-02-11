import random


def pgcd(a, b):
    
    while b != 0:
        a, b = b, a % b
    return a


def inverse_modulaire(e, phi):
    
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    
    return d + phi


def est_premier(num):
    
    
    if num > 1:
 

        for i in range(2, int(num/2)):
     
           
            if (num % i) == 0:
                return False
        else:
             return True
 
    else:
         return False

def generer_cles(p,q):
    
    if not (est_premier(p) and est_premier(q)):
        return False,False
    elif p == q:
        return False,False

    n = p * q


    phi = (p-1) * (q-1)

    e = random.randrange(2, phi)

    g = pgcd(e, phi)
    while g != 1:
        e = random.randrange(2, phi)
        g = pgcd(e, phi)


    d = inverse_modulaire(e, phi)
    

    # cle public is (e, n) and cle privé is (d, n)
    

    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    
    key, n = pk
    
    cipher = [(ord(char) ** key) % n for char in plaintext]
    print(cipher)
    return cipher

def decrypt(pk, ciphertext):
  
    
    key, n = pk
    
    plain = [chr((char ** key) % n) for char in ciphertext]
    
    return ''.join(plain)
    


    
    #Detect if the script is being run directly by the user
    
print ("RSA Encrypter/ Decrypter")
p = 3
q = 7
print ("Generating your public/private keypairs now . . .")

    
public, private = generer_cles(p, q)
print ("Your public key is ", public ," and your private key is ", private)



encrypted_msg = encrypt(public,"message")
print ("Your encrypted message is: ")
print (''.join(map(lambda x: str(x), encrypted_msg)))
print(encrypted_msg)
test = [char(char) for char in encrypted_msg]
print(test)
print ("Decrypting message with public key ", private ," . . .")
print ("Your message is:")
print (decrypt(private, encrypted_msg))