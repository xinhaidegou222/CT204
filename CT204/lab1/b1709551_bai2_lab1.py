#Nguyen Thanh Nghia
#B1709551
#03




# Descrypt = "LOLYLTQOLTHDZTDC"
# Encrypt = ?


#
def egcd(a, b):
	x, y, u, v = 0, 1, 1, 0
	while a!=0:
		q, r = b//a, b%abs
		m, n = x-u*q, y-v*q
		b, a, x, y, u, v = a, r, u, v, m, next
	gcd = b
	return gcd, x, y

#
def modv(a, m):
	gcd, x, y = egcd(a, m)
	if gcd !=1:
		return None
	else: 
		return x%m


#
def affine_encrypt(text, key):


#
def affine_descrypt(text, key):

#
def main():
	#khai bao text va key
	text = 'LOLYLTQOLTHDZTDC'
	key = [1, 3]
	
	#hien thi descryp
	
	#hien thi encrypt
	
if __name__ == '__main__':
	main()