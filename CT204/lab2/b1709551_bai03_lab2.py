#Nguyen Thanh Nghia
#B1709551
#STT: 03
#Nhom sang 4
#Lab2
#Bai3

#import
from Crypto.Util.Padding import pad, unpad
from Crypto import Random
from Crypto.Cipher import DES
import base64
from tkinter import*

window = Tk()
window.title("Thực hành buổi 2 - Bài 3 Application")


#ui design
lb_empty_0 = Label(window, text='', font=("Arial Bold", 10))
lb_empty_0.grid(column=0, row=0)

lb_txt_view_1 = Label(window, text='CHƯƠNG TRÌNH DEMO', font=("Arial Bold", 18))
lb_txt_view_1.grid(column=1, row=1)

lb_txt_view_2 = Label(window, text='MẬT MÃ ĐỐI XỨNG DES', font=("Arial Bold", 14))
lb_txt_view_2.grid(column=1, row=2)

lb_txt_view_3 = Label(window, text='Văn bản gốc: ', font=("Arial Bold", 12))
lb_txt_view_3.grid(column=0, row=3)

ln_edit_1= Entry(window, width=70)
ln_edit_1.grid(column=1, row=3)

lb_txt_view_3 = Label(window, text='Khóa: ', font=("Arial Bold", 12))
lb_txt_view_3.grid(column=0, row=4)

ln_edit_2= Entry(window, width=70)
ln_edit_2.grid(column=1, row=4)

lb_txt_view_3 = Label(window, text='Văn bản được mã hóa: ', font=("Arial Bold", 12))
lb_txt_view_3.grid(column=0, row=5)

ln_edit_3= Entry(window, width=70)
ln_edit_3.grid(column=1, row=5)

lb_txt_view_3 = Label(window, text='Văn bản được giải mã: ', font=("Arial Bold", 12))
lb_txt_view_3.grid(column=0, row=6)

ln_edit_4= Entry(window, width=70)
ln_edit_4.grid(column=1, row=6)

btn_mahoa = Button(window, text='Mã hóa!' )
btn_mahoa.grid(column=0, row=7)

btn_giaima = Button(window, text='Giải mã!')
btn_giaima.grid(column=1, row=7)

#xu ly su kien
def pad(s):
	return s + (8 - len(s) % 8) * chr(8 - len(s) % 8)

def unpad(s):
	return s[:-ord(s[len(s)-1:])]

def mahoa_DES():
	txt = pad(ln_edit_1.get()).encode("utf8")
	key = pad(ln_edit_2.get()).encode("utf8")
	cipher = DES.new(key, DES.MODE_ECB)
	entxt = cipher.encrypt(txt)
	entxt = base64.b64encode(entxt)
	ciphertxt.delete(0, END)
	ciphertxt.insert(INSERT, entxt)

def giaima_DES():
	txt = ciphertxt.get()
	txt = base64.b64decode(txt)
	key = pad(keytxt.get()).encode("utf8")
	cipher = DES.new(key, DES.MODE_ECB)
	detxt = unpad(cipher.decrypt(txt))
	denctxt.delete(0, END)
	denctxt.insert(insert, detxt)
#display ui
window.geometry('650x350')
window.mainloop()
