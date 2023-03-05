import math

def xgcd(a, m):
    temp = m
    x0, x1, y0, y1 = 1, 0, 0, 1
    while m!=0:
        q, a, m = a // m, m, a % m
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    if x0 < 0: x0 = temp+x0
    return x0

print(xgcd(15,24))

def Char2Num(c):
    return ord(c)-65

def Num2Char(n):
    return chr(n+65)

def encryptAF(txt,a,b,m):
    r = ""
    for c in txt:
        e = (a*Char2Num(c)+b) % m
        r = r+Num2Char(e)
    return r

def mahoa_affine(key,a,b):
    m = 26
    entxt = encryptAF(key,a,b,m)
    return entxt 

def giaima_affine(key,a,b):
    m = 26
    a1 = xgcd(a,m)
    def chuoigiaima(): 
        r = ""
        for c in key:
            e = (a1*(Char2Num(c)-b )) % m
            r = r+Num2Char(e)
        return r 
    kq=chuoigiaima()
    return kq 

key = 'LOLYLTQOLTHDZTDC'
for i in range(0,26):
    if math.gcd(26,i)==1:
        for j in range(0,26):
            ketqua=giaima_affine(key,i,j)
            print(i,j,ketqua)
