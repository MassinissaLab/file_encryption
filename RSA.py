import random


'''
Euclid's algorithm for determining the greatest common divisor
Use iteration to make it faster for larger integers
'''
def pgcd(a, b):
    
    while b != 0:
        a, b = b, a % b
    return a

'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''
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

'''
Tests to see if a number is prime.
'''
def est_premier(num):
    
    print(str(int(num/2)))
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
        return False
    elif p == q:
        return False
    #n = pq
    n = p * q

    #Phi is the totient of n
    phi = (p-1) * (q-1)

    #Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(2, phi)
    #Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = pgcd(e, phi)
    while g != 1:
        e = random.randrange(2, phi)
        g = pgcd(e, phi)

    #Use Extended Euclid's Algorithm to generate the private key
    d = inverse_modulaire(e, phi)
    
    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    

    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    #Unpack the key into it's components
    key, n = pk
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    #Return the array of bytes
    return cipher

def decrypt(pk, ciphertext):
  
    #Unpack the key into its components
    key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)
    

if __name__ == '__main__':
    
    #Detect if the script is being run directly by the user
    
    print ("RSA Encrypter/ Decrypter")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    print ("Generating your public/private keypairs now . . .")
    while True:
        
        public, private = generer_cles(p, q)
        print ("Your public key is ", public ," and your private key is ", private)
        if private[0]!=None:
            break

    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(public, message)
    print ("Your encrypted message is: ")
    print ('µ'.join(map(lambda x: str(x), encrypted_msg)))
    print(encrypted_msg)
    print ("Decrypting message with public key ", private ," . . .")
    print ("Your message is:")
    print (decrypt(private, encrypted_msg))