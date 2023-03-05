#B1709551
#Nguyen Thanh Nghia
#03

from tkinter import *
import tkinter as tk
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA256, MD5, SHA1, SHA224, SHA384, SHA512
from Crypto.Cipher import PKCS1_v1_5
import base64

window = Tk()
window.title("Demo ATBMTT")

def hashing():
	content = plaintext.get().encode()
	func = hashmode.get()
	if func == 0:
		result = MD5.new(content)
	if func == 1:
		result = SHA1.new(content)
	if func == 2:
		result = SHA256.new(content)
	if func == 3:
		result = SHA512.new(content)

	rs = result.hexdigest().upper()
	hashvalue.delete(0,END)
	hashvalue.insert(INSERT,rs)


lb1 = Label(window, text="CHƯƠNG TRÌNH DEMO", font=("Arial Bold", 20))
lb1.grid(column=1, row=0)

lb_txt_view_1 = Label(window, text="Van ban: ", font=("Arial", 14))
lb_txt_view_1.grid(column=0, row=1)

plaintext = Entry(window, width=120)
plaintext.grid(column=1, row=1)

radioGroup = tk.LabelFrame(window, text = "Hàm băm")
radioGroup.grid(row=3, column=1)
hashmode = IntVar()
hashmode.set(-1)
md5_func = tk.Radiobutton(radioGroup, text="Hash MD5", font=("Times New Roman", 11), variable=hashmode, value=0, command=hashing)
md5_func.grid(row=4, column=0)
sha1_func = tk.Radiobutton(radioGroup, text="Hash SHA1", font=("Times New Roman", 11), variable=hashmode, value=1, command=hashing)
sha1_func.grid(row=5, column=0)
sha256_func = tk.Radiobutton(radioGroup, text="Hash SHA256", font=("Times New Roman", 11), variable=hashmode, value=2, command=hashing)
sha256_func.grid(row=6, column=0)
sha256_func = tk.Radiobutton(radioGroup, text="Hash SHA512", font=("Times New Roman", 11), variable=hashmode, value=3, command=hashing)
sha256_func.grid(row=7, column=0)

lb_txt_view_2 = Label(window, text="Gia tri bam: ", font=("Arial", 14))
lb_txt_view_2.grid(column=0, row=8)

hashvalue = Entry(window, width=120)
hashvalue.grid(column=1, row=8)

#Display Window
window.geometry('900x300')

window.mainloop()