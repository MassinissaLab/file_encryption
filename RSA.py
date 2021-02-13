import random 
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
 




def egcd(e,r):
	while(r!=0):
		e,r=r,e%r
	return e
 
#Euclid's Algorithm
def eugcd(e,r):
	for i in range(1,r):
		while(e!=0):
			a,b=r//e,r%e
			
			r=e
			e=b
 
#Extended Euclidean Algorithm
def eea(a,b):
	if(a%b==0):
		return(b,0,1)
	else:
		gcd,s,t = eea(b,a%b)
		s = s-((a//b) * t)
		
		return(gcd,t,s)
 
#Multiplicative Inverse
def mult_inv(e,r):
	
	for n in range(r):
		if (e * n) % r == 1:
			return n
			break

		elif n == r - 1:
			return False
		else:
			continue
   
 


def generer_cles(p,q):
	
	if not (est_premier(p) and est_premier(q)):
		return False,False
	elif p == q:
		return False,False

	n = p * q


	r = (p-1) * (q-1)
	print(r)

	e = random.randrange(2, r)
	g = egcd(e, r)
	while g != 1:
		e = random.randrange(2, r)
		g = egcd(e, r)

	#eugcd(e,r)
	d = mult_inv(e,r)

	print(d)
	# cle public is (e, n) and cle privé is (d, n)
	

	return ((e, n), (d, n))

def encrypt(pub_key,n_text):
	e,n=pub_key
	x=[]
	m=0
	for i in n_text:
		if(i.isspace()):
			spc=400
			x.append(400)
		else:

			m = ord(i)
			
			c=(m**e)%n
			print(str(i)+' '+str(ord(i))+' '+str(m)+' '+str(c))

			x.append(c)
		
		
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
			
			c=chr(m)
			x+=c
	return x
 
print ("RSA Encrypter/ Decrypter")
p = 11
q = 17
print ("Generating your public/private keypairs now . . .")

	
public, private = generer_cles(p, q)
print ("Your public key is ", public ," and your private key is ", private)



encrypted_msg = encrypt(public,"Message")

print ("Your encrypted message is: ")
print(encrypted_msg)

print ("Decrypting message with public key ", private ," . . .")
print ("Your message is:")
print (decrypt(private, encrypted_msg))