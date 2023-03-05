from tkinter import * # thư viện giao diện tkinter
import math # thư viện toán 

# hàm chuyển chuỗi sang nhị phân
def Char2Num(c):
    return ord(c)-65

# chuyển nhị phân về chuỗi
def Num2Char(n):
    return chr(n+65)

# hàm mã hóa chuỗi: đầu vào là chuỗi ký tự, khóa a,b (là 2 số nguyên tố) và m (m=26 theo mật mã affine)
def encryptAF(txt,a,b,m):
    r = ""
    for c in txt:
        e = (a*Char2Num(c)+b) % m
        r = r+Num2Char(e)
    return r

# hàm tính số nguyên tố cùng nhau (học thuộc vì đây là câu 1 BÀI THI)
def xgcd(a, m):
    temp = m
    x0, x1, y0, y1 = 1, 0, 0, 1
    while m!=0:
        q, a, m = a // m, m, a % m
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    if x0 < 0: x0 = temp+x0
    return x0

# hàm mã hóa thành mật mã affine: đầu vào là từ khóa (chuỗi ký tự thôi), khóa a và b
def mahoa_affine(key,a,b):
    m = 26
    entxt = encryptAF(key,a,b,m) # gọi lại hàm mã hóa phía trên để xử lý
    return entxt # trả về chuỗi đã được mã hóa

# hàm giải mã: đầu vào là từ khóa (chuỗi ký từ đã được mã hóa), khóa a và b
def giaima_affine(key,a,b):
    m = 26
    a1 = xgcd(a,m) # tính số nguyên tố cùng nhau của a với m 
    def chuoigiaima(): #hàm tính toán để giải mã chuỗi
        r = ""
        for c in key:
            e = (a1*(Char2Num(c)-b )) % m
            r = r+Num2Char(e)
        return r # trả về chuỗi đã giải mã
    kq=chuoigiaima()
    return kq # trả về chuỗi giải mã cuối cùng

# bài thi
# thì nó cho cái chuỗi dưới đã bị mã hóa bằng mật mã affine 
# # kêu tìm chuỗi ban đầu là gì, và 2 khóa a, b là bao nhiêu, gợi ý là chuỗi ban đầu có chứa ký tự 'LAMUOI'
# Giải:
# chạy for i từ 0 đến 26 (vì m=26 theo mật mã affine) và tính ước chung của i và m để tìm khóa a (số nguyên tố => gcd(i,26)==1)
# nếu tìm được khóa a thì chạy tiếp for j cũng từ 0 đến 26 để tìm khóa b
# tính tất cả các kết quả của khóa a và b bằng hàm giải mã, ông chạy trên cmd, nó sẽ ra 1 đống luôn
# số thứ nhất là a, số thứ 2 là b, chuỗi phía sau là kết quả giải mã được dựa trên 2 khóa a và b
# ông dò trong đống đó, chuỗi nào có chứa ký tự theo gợi ý và chuỗi đó phải có nghĩa, đó là kết quả duy nhất
key = 'LOLYLTQOLTHDZTDC'
for i in range(0,26):
    if math.gcd(26,i)==1:
        for j in range(0,26):
            ketqua=giaima_affine(key,i,j)
            print(i,j,ketqua)
# dưới là kết quả bài tập này: chuỗi ban đầu là 'A LÀ NĂM B LÀ MƯỜI MỘT' ghi liền không dấu như dưới, 5 là khóa a, 11 là khóa b
# có chứa 'LAMUOI' như gợi ý và có nghĩa, chỉ có 1 kq chứa thôi nên kiếm được là dừng không cần tìm phía sau
# 5 11 ALANAMBLAMUOIMOT

