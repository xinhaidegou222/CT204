#Nguyen Thanh Nghia
#B1709551
#STT=03



# -*- coding: utf8 -*-
from tkinter import *
import tkinter as tk
from Crypto.Cipher import DES
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5
import base64
from Crypto import Random
from tkinter import filedialog
from Crypto.Hash import SHA256, MD5, SHA1, SHA224, SHA384, SHA512



#RSA Class
def save_file(content, _mode, _title, _filetypes, _defaultextension):
    f = filedialog.asksaveasfile(mode = _mode, initialdir = "D:/CTU University/CT203-ATBMTT", title = _title, filetypes = _filetypes, defaultextension = _defaultextension)
    if f is None: return
    f.write(content)
    f.close()



def get_key(key_style):
    filename = filedialog.askopenfilename(initialdir = "D:/D:/CTU University/CT203-ATBMTT", title = "Open " + key_style, filetypes = (("PEM files", "*.pem"),("All files", "*.*")))
    if filename is None: return
    file = open(filename,"rb")
    key = file.read()
    file.close()
    return RSA.importKey(key)

class MAHOA_RSA(tk.Toplevel):
	def __init__(self, parent):
		self.parent = parent
		Toplevel.__init__(self)
		self.title("CHƯƠNG TRÌNH MÃ HÓA RSA")
		self.geometry("800x600")

		#RSA UI
		self.lb1 = Label(self, text="CHƯƠNG TRÌNH DEMO", font=("Arial Bold", 20))
		self.lb1.grid(column=1, row=1)
		self.lb2 = Label(self, text="MẬT MÃ ĐỐI XỨNG DES", font=("Arial Bold", 15))
		self.lb2.grid(column=1, row=2)

		self.plain1 = Label(self, text="Văn bản gốc", font=("Arial Bold", 14))
		self.plain1.grid(column=0, row=3)
		self.plaintxt = Entry(self, width=90)
		self.plaintxt.grid(column=1, row=3)

		self.plain3 = Label(self, text="Văn bản được mã hóa", font=("Arial Bold", 14))
		self.plain3.grid(column=0, row=4)
		self.ciphertxt = Entry(self, width=90)
		self.ciphertxt.grid(column=1, row=4)

		self.plain4 = Label(self, text="Văn bản được giải mã", font=("Arial Bold", 14))
		self.plain4.grid(column=0, row=5)
		self.dectxt = Entry(self, width=90)
		self.dectxt.grid(column=1, row=5)

		self.plain5 = Label(self, text="Khóa cá nhân", font=("Arial Bold", 14))
		self.plain5.grid(column=0, row=6)
		self.pri_key = Text(self, height=10, width=65)
		self.pri_key.grid(column=1, row=6)

		self.plain6 = Label(self, text="Khóa công khai", font=("Arial Bold", 14))
		self.plain6.grid(column=0, row=7)
		self.pub_key = Text(self, height=10, width=65)
		self.pub_key.grid(column=1, row=7)

		self.button = Button(self, text="TẠO KHÓA", command=self.generate_key)
		self.button.grid(column=1, row=8)

		self.button1 = Button(self, text="MÃ HÓA", command=self.mahoa_rsa)
		self.button1.grid(column=1, row=9)

		self.button2 = Button(self, text="GIẢI MÃ", command=self.giaima_rsa)
		self.button2.grid(column=1, row=10)

		self.thoat = Button(self,text="BACK TO TITLE", command=self.destroy)
		self.thoat.grid(column=1, row=11)

	#RSA Button Command
	def mahoa_rsa(self):
		txt = self.plaintxt.get().encode()
		pub_key = get_key("Public Key")
		cipher = PKCS1_v1_5.new(pub_key)
		entxt = cipher.encrypt(txt)
		entxt = base64.b64encode(entxt)
		self.ciphertxt.delete(0,END)
		self.ciphertxt.insert(INSERT,entxt)

	def giaima_rsa(self):
		entxt = self.ciphertxt.get().encode()
		entxt = base64.b64decode(entxt)
		pri_key = get_key("Private Key")
		sentinel = Random.get_random_bytes(128)
		pri_key_object = PKCS1_v1_5.new(pri_key)
		detxt = pri_key_object.decrypt(entxt, sentinel)
		self.dectxt.delete(0,END)
		self.dectxt.insert(INSERT, detxt)

	def generate_key(self):
		key = RSA.generate(1024)
		pri = save_file(key.exportKey('PEM'), 'wb', 'Lưu khóa cá nhân', (("All files", "*.*"), ("PEM files", "*.pem")), ".pem")
		pub = save_file(key.publickey().exportKey('PEM'), 'wb', 'Lưu khóa công khai', (("All files", "*.*"),("PEM files", "*.pem")), ".pem")
		self.pri_key.delete('1.0',END)
		self.pri_key.insert(END,key.exportKey('PEM'))
		self.pub_key.delete('1.0',END)
		self.pub_key.insert(END,key.publickey().exportKey('PEM'))


#DES Class
def pad(s):
	return s + (8 - len(s) % 8) * chr(8 - len(s) % 8)

def unpad(s):
	return s[:-ord(s[len(s)-1:])]

class MAHOA_DES(tk.Toplevel):
	def __init__(self, parent):
		self.parent = parent
		Toplevel.__init__(self)
		self.title("CHƯƠNG TRÌNH MÃ HÓA BẤT ĐỐI XỨNG DES ^^ !")
		self.geometry("950x300")

		self.lb1 = Label(self, text="CHƯƠNG TRÌNH MÃ HÓA BẮT ĐỐI XỨNG ĐƠN GIẢN", font=("Arial Bold", 20))
		self.lb1.grid(column=1, row = 1)

		self.lb2 = Label(self, text="MẬT MÃ BẤT ĐỐI XỨNG DES", font=("Arial Bold", 14))
		self.lb2.grid(column=1, row =2)

		self.plainlb3 = Label(self, text="Văn bản gốc", font=("Arial", 14))
		self.plainlb3.grid(column=0, row=4)
		self.plaintxt = Entry(self,width=100)
		self.plaintxt.grid(column=1, row=4)

		self.lb4 = Label(self, text="Khóa",font=("Arial", 14))
		self.lb4.grid(column=0, row=5)
		self.keytxt = Entry(self,width=100)
		self.keytxt.grid(column=1, row=5)
		self.lb5 = Label(self, text="Văn bản được mã hóa", font=("Arial", 14))
		self.lb5.grid(column=0, row=6)
		self.ciphertxt = Entry(self, width=100)
		self.ciphertxt.grid(column=1, row=6)
		self.lb6 = Label(self, text="Văn bản được giải mã", font=("Arial", 14))
		self.lb6.grid(column=0, row=7)
		self.denctxt = Entry(self,width=100)
		self.denctxt.grid(column=1, row=7)
		self.btn_enc = Button(self, text="MÃ HÓA", command=self.mahoa_DES)
		self.btn_enc.grid(column=1, row=9)
		self.btn_dec = Button(self, text="GIẢI MÃ ", command=self.giaima_DES)
		self.btn_dec.grid(column=1, row=10)
		self.thoat = Button(self,text="BACK TO TITLE", command=self.destroy)
		self.thoat.grid(column=1, row=11)

	
	#XL
	def mahoa_DES(self):
 		txt = pad(self.plaintxt.get()).encode()
 		key = pad(self.keytxt.get()).encode()
 		cipher = DES.new(key, DES.MODE_ECB)
 		entxt = cipher.encrypt(txt)
 		entxt = base64.b64encode(entxt)
 		self.ciphertxt.delete(0,END)
 		self.ciphertxt.insert(INSERT,entxt)

	def giaima_DES(self):
 		txt = self.ciphertxt.get()
 		txt = base64.b64decode(txt)
 		key = pad(self.keytxt.get()).encode()
 		cipher = DES.new(key, DES.MODE_ECB)
 		detxt = unpad(cipher.decrypt(txt))
 		self.denctxt.delete(0,END)
 		self.denctxt.insert(INSERT,detxt)

	
	

#Affine Class

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
##Affine Main
class MAHOA_AFFINE(tk.Toplevel):
	def __init__(self, parent):
		self.parent = parent
		Toplevel.__init__(self)
		self.title("CHƯƠNG TRÌNH MÃ HÓA AFFINE ^^ !")
		self.geometry("1200x200")
		#Create control
		self.lb0 = Label(self, text=" ",font=("Arial Bold", 10))
		self.lb0.grid(column=0, row=0)
		self.lbl = Label(self, text="CHƯƠNG TRÌNH MÃ HÓA AFFINE ĐƠN GIẢN",font=("Arial Bold", 20))
		self.lbl.grid(column=1, row=1)
		self.lb2 = Label(self, text="MẬT MÃ AFFINE",font=("Arial Bold", 15))
		self.lb2.grid(column=0, row=2)
		self.plainlb3 = Label(self, text="PLAIN TEXT",font=("Arial", 14))
		self.plainlb3.grid(column=0, row=3)
		self.plaintxt = Entry(self,width=20)
		self.plaintxt.grid(column=1, row=3)
		self.KEYlb4 = Label(self, text="KEY PAIR",font=("Arial", 14))
		self.KEYlb4.grid(column=2, row=3)
		self.KEYA1 = Entry(self,width=3)
		self.KEYA1.grid(column=3, row=3)
		self.KEYB1 = Entry(self,width=5)
		self.KEYB1.grid(column=4, row=3)


		#Clipertext field
		self.plainlb4 = Label(self, text="CLIPHER TEXT", font=("Arial Bold", 14))
		self.plainlb4.grid(column=0, row=4)
		self.plaintext1 = Entry(self, width=20)
		self.plaintext1.grid(column=1, row=4)

		#Giai ma field
		self.plaintext2 = Entry(self, width=20)
		self.plaintext2.grid(column=3, row=4)


		#AFbtn
		self.AFbtn = Button(self, text="MÃ HÓA", command =self.mahoa)
		self.AFbtn.grid(column=5, row=3)

		#DEAFbtn
		self.DEAFbtn = Button(self, text="GIẢI MÃ", command=self.giaima)
		self.DEAFbtn.grid(column=2, row=4)

		self.thoat = Button(self,text="BACK TO TITLE", font=("SDK_JP_WEB 85W", 11), command=self.destroy)
		self.thoat.grid(column=1, row=11)

	def mahoa(self):
		a = int(self.KEYA1.get())
		b = int(self.KEYB1.get())
		m = 26
		entxt = encryptAF(self.plaintxt.get(),a,b,m)
		self.plaintext1.delete(0,END)
		self.plaintext2.delete(0,END)
		self.plaintext1.insert(INSERT,entxt)

	def giaima(self):
		a = int(self.KEYA1.get())
		b = int(self.KEYB1.get())
		m = 26
		entxt2 = decryptAF(self.plaintext1.get(),a,b,m)
		self.plaintext1.delete(0,END)
		self.plaintext2.insert(INSERT,entxt2)

#HASHING CLASS

class MAHOA_HASHING(tk.Toplevel):
	def __init__(self, parent):
		self.parent = parent
		Toplevel.__init__(self)
		self.title("CHƯƠNG TRÌNH BĂM ^^ !")
		self.geometry("900x400")

		self.lb1 = Label(self, text="CHƯƠNG TRÌNH BĂM", font=("SDK_JP_WEB 85W", 20))
		self.lb1.grid(column=1, row=0)

		self.lb_txt_view_1 = Label(self, text="Văn bản: ", font=("SDK_JP_WEB 85W", 14))
		self.lb_txt_view_1.grid(column=0, row=1)

		self.plaintext = Entry(self, width=120)
		self.plaintext.grid(column=1, row=1)

		self.radioGroup = tk.LabelFrame(self, text = "HÀM BĂM", font=("SDK_JP_WEB 85W", 10))
		self.radioGroup.grid(row=3, column=1)
		self.hashmode = IntVar()
		self.hashmode.set(-1)
		self.md5_func = tk.Radiobutton(self.radioGroup, text="HASH MD5", font=("SDK_JP_WEB 85W", 14), variable=self.hashmode, value=0, command=self.hashing)
		self.md5_func.grid(row=4, column=0)
		self.sha1_func = tk.Radiobutton(self.radioGroup, text="HASH SHA1", font=("SDK_JP_WEB 85W", 14), variable=self.hashmode, value=1, command=self.hashing)
		self.sha1_func.grid(row=5, column=0)
		self.sha256_func = tk.Radiobutton(self.radioGroup, text="HASH SHA256", font=("SDK_JP_WEB 85W", 14), variable=self.hashmode, value=2, command=self.hashing)
		self.sha256_func.grid(row=6, column=0)
		self.sha256_func = tk.Radiobutton(self.radioGroup, text="HASH SHA512", font=("SDK_JP_WEB 85W", 14), variable=self.hashmode, value=3, command=self.hashing)
		self.sha256_func.grid(row=7, column=0)

		self.lb_txt_view_2 = Label(self, text="Kết quả băm: ", font=("SDK_JP_WEB 85W", 14))
		self.lb_txt_view_2.grid(column=0, row=8)

		self.hashvalue = Entry(self, width=120)
		self.hashvalue.grid(column=1, row=8)

		self.thoat = Button(self,text="BACK TO TITLE", font=("SDK_JP_WEB 85W", 11), command=self.destroy)
		self.thoat.grid(column=1, row=11)

	def hashing(self):
		content = self.plaintext.get().encode()
		func = self.hashmode.get()
		if func == 0:
			result = MD5.new(content)
		if func == 1:
			result = SHA1.new(content)
		if func == 2:
			result = SHA256.new(content)
		if func == 3:
			result = SHA512.new(content)

		rs = result.hexdigest().upper()
		self.hashvalue.delete(0,END)
		self.hashvalue.insert(INSERT,rs)

#Main UI
class MainWindow(tk.Frame):
	def __init__(self, parent):
		self.parent = parent
		tk.Frame.__init__(self)

		self.mahoa_AFFINE = Button(text="AFFINE", font=("SDK_JP_WEB 85W", 11), command=self.des_affine)
		self.mahoa_AFFINE.pack()

		self.mahoa_DES = Button(text="DES", font=("SDK_JP_WEB 85W", 11), command=self.des_DES)
		self.mahoa_DES.pack()

		self.mahoa_RSA = Button(text="RSA", font=("SDK_JP_WEB 85W", 11), command=self.des_RSA)
		self.mahoa_RSA.pack()

		self.mahoa_HASHING = Button(text="HASHING", font=("SDK_JP_WEB 85W", 11), command=self.des_hashing)
		self.mahoa_HASHING.pack()

		self.thoat = Button(text="EXIT", font=("SDK_JP_WEB 85W", 11), command=quit)
		self.thoat.pack()
	def des_DES(self):
		MAHOA_DES(self)
	
	def des_affine(self):
		MAHOA_AFFINE(self)

	def des_RSA(self):
		MAHOA_RSA(self)

	def des_hashing(self):
		MAHOA_HASHING(self)

def main():
	window = tk.Tk()
	window.title("CHƯƠNG TRÌNH CHÍNH ^^ !")
	window.geometry("400x200")
	MainWindow(window)
	window.mainloop()
main()