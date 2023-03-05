#Nguyen Thanh Nghia
#B1709551
#03





#import
from tkinter import*

#fsdfsfd
window = Tk()
window.title("Demo ATBMTT")

#event clicked AFbtn
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
def mahoa():
	a = int(KEYA1.get())
	b = int(KEYB1.get())
	m = 26
	entxt = encryptAF(plaintxt.get(),a,b,m)
	plaintext1.delete(0,END)
	plaintext2.delete(0,END)
	plaintext1.insert(INSERT,entxt)


#event cliked DEAFbtn
def xgcd(a, m):
	temp = m
	x0, x1, y0, y1 = 1, 0, 0, 1
	while m!=0:
		q, a, m = a // m, m, a % m
		x0, x1 = x1, x0 - q * x1
		y0, y1 = y1, y0 - q * y1
	if x0 < 0: x0 = temp+x0
	return x0
def decryptAF(txt,a,b,m):
	r = ""
	a1 = xgcd(a,m)
	for c in txt:
		e = (a1*(Char2Num(c)-b )) % m
		r = r+Num2Char(e)
	return r
def giaima():
	a = int(KEYA1.get())
	b = int(KEYB1.get())
	m = 26
	entxt2 = decryptAF(plaintext1.get(),a,b,m)
	plaintext1.delete(0,END)
	plaintext2.insert(INSERT,entxt2)


#Create control
lb0 = Label(window, text=" ",font=("Arial Bold", 10))
lb0.grid(column=0, row=0)
lbl = Label(window, text="CHƯƠNG TRÌNH DEMO",font=("Arial Bold", 20))
lbl.grid(column=1, row=1)
lb2 = Label(window, text="MẬT MÃ AFFINE",font=("Arial Bold", 15))
lb2.grid(column=0, row=2)
plainlb3 = Label(window, text="PLAIN TEXT",font=("Arial", 14))
plainlb3.grid(column=0, row=3)
plaintxt = Entry(window,width=20)
plaintxt.grid(column=1, row=3)
KEYlb4 = Label(window, text="KEY PAIR",font=("Arial", 14))
KEYlb4.grid(column=2, row=3)
KEYA1 = Entry(window,width=3)
KEYA1.grid(column=3, row=3)
KEYB1 = Entry(window,width=5)
KEYB1.grid(column=4, row=3)


#Clipertext field
plainlb4 = Label(window, text="CLIPHER TEXT", font=("Arial Bold", 14))
plainlb4.grid(column=0, row=4)
plaintext1 = Entry(window, width=20)
plaintext1.grid(column=1, row=4)

#Giai ma field
plaintext2 = Entry(window, width=20)
plaintext2.grid(column=3, row=4)


#AFbtn
AFbtn = Button(window, text="Mã Hóa", command = mahoa)
AFbtn.grid(column=5, row=3)

#DEAFbtn
DEAFbtn = Button(window, text="Giai Ma", command=giaima)
DEAFbtn.grid(column=2, row=4)

#Display Window
window.geometry('800x600')

window.mainloop()

