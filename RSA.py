
def est_premier(a):
    if(a==2):
        return True
    elif((a<2) or ((a%2)==0)):
        return False
    elif(a>2):
        for i in range(2,a):
            if not(a%i):
                return false
    return True
 





 
#GCD
'''CALCULATION OF GCD FOR 'e' CALCULATION.'''
def egcd(e,r):
    while(r!=0):
        e,r=r,e%r
    return e
 
#Euclid's Algorithm
def eugcd(e,r):
    for i in range(1,r):
        while(e!=0):
            a,b=r//e,r%e
            if(b!=0):
                print("%d = %d*(%d) + %d"%(r,a,e,b))
            r=e
            e=b
 
#Extended Euclidean Algorithm
def eea(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
        print("%d = %d*(%d) + (%d)*(%d)"%(gcd,a,t,s,b))
        return(gcd,t,s)
 
#Multiplicative Inverse
def mult_inv(e,r):
    gcd,s,_=eea(e,r)
    if(gcd!=1):
        return False
    else:
        if(s<0):
            print("s=%d. Since %d is less than 0, s = s(modr), i.e., s=%d."%(s,s,s%r))
        elif(s>0):
            print("s=%d."%(s))
        return s%r
 


def generer_cles(p,q):
    
    if not (est_premier(p) and est_premier(q)):
        return False,False
    elif p == q:
        return False,False

    n = p * q


    r = (p-1) * (q-1)

    e=None
    for i in range(1,1000):
        if(egcd(i,r)==1):
            e=i

    eugcd(e,r)
    d = mult_inv(e,r)
    # cle public is (e, n) and cle privé is (d, n)
    

    return ((e, n), (d, n))
def encrypt(pub_key,n_text):
    e,n=pub_key
    x=[]
    m=0
    for i in n_text:
        if(i.isupper()):
            m = ord(i)-65
            c=(m**e)%n
            x.append(c)
        elif(i.islower()):               
            m= ord(i)-97
            c=(m**e)%n
            x.append(c)
        elif(i.isspace()):
            spc=400
            x.append(400)
    return x
     
 
#Decryption
'''DECRYPTION ALGORITHM'''
def decrypt(priv_key,c_text):
    d,n=priv_key
    txt=c_text
    x=''
    m=0
    for i in txt:
        if(i=='400'):
            x+=' '
        else:
            m=(int(i)**d)%n
            m+=65
            c=chr(m)
            x+=c
    return x
 
print ("RSA Encrypter/ Decrypter")
p = 3
q = 7
print ("Generating your public/private keypairs now . . .")

    
public, private = generer_cles(p, q)
print ("Your public key is ", public ," and your private key is ", private)



encrypted_msg = encrypt(public,"message")
print ("Your encrypted message is: ")
print(encrypted_msg)

print ("Decrypting message with public key ", private ," . . .")
print ("Your message is:")
print (decrypt(private, encrypted_msg))