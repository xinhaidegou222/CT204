#Nguyen Thanh Nghia
#B1709551
#03

#import
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5
import base64
from tkinter import *
from tkinter import filedialog


window = Tk()
window.title("Thực hành buổi 3 - Application")

def save_file(content, _mode, _title, _filetypes, _defaultextension):
    f = filedialog.asksaveasfile(mode = _mode, initialdir = "D:/", title = _title, filetypes = _filetypes, defaultextension = _defaultextension)
    if f is None: return
    f.write(content)
    f.close()

def generate_key():
    key = RSA.generate(1024)
    pri = save_file(key.exportKey('PEM'), 'wb', 'Lưu khóa cá nhân', (("All files", "*.*"), ("PEM files", "*.pem")), ".pem")
    pub = save_file(key.publickey().exportKey('PEM'), 'wb', 'Lưu khóa công khai', (("All files", "*.*"),("PEM files", "*.pem")), ".pem")
    pri_key.delete('1.0',END)
    pri_key.insert(END,key.exportKey('PEM'))
    pub_key.delete('1.0',END)
    pub_key.insert(END,key.publickey().exportKey('PEM'))

def get_key(key_style):
    filename = filedialog.askopenfilename(initialdir = "C:/", title = "Open " + key_style, filetypes = (("PEM files", "*.pem"),("All files", "*.*")))
    if filename is None: return
    file = open(filename,"rb")
    key = file.read()
    file.close()
    return RSA.importKey(key)

def mahoa_rsa():
    txt = plaintxt.get().encode()
    pub_key = get_key("Public Key")
    cipher = PKCS1_v1_5.new(pub_key)
    entxt = cipher.encrypt(txt)
    entxt = base64.b64encode(entxt)
    ciphertxt.delete(0,END)
    ciphertxt.insert(INSERT,entxt)

def giaima_rsa():
    entxt = ciphertxt.get().encode()
    entxt = base64.b64decode(entxt)
    pri_key = get_key("Private Key")
    sentinel = Random.get_random_bytes(128)
    pri_key_object = PKCS1_v1_5.new(pri_key)
    detxt = pri_key_object.decrypt(entxt, sentinel)
    dectxt.delete(0,END)
    dectxt.insert(INSERT, detxt)

#ui
lb1 = Label(window, text="CHƯƠNG TRÌNH DEMO", font=("Arial Bold", 20))
lb1.grid(column=1, row=1)
lb2 = Label(window, text="MẬT MÃ ĐỐI XỨNG DES", font=("Arial Bold", 15))
lb2.grid(column=1, row=2)

plain1 = Label(window, text="Văn bản gốc", font=("Arial Bold", 14))
plain1.grid(column=0, row=3)
plaintxt = Entry(window, width=90)
plaintxt.grid(column=1, row=3)

plain3 = Label(window, text="Văn bản được mã hóa", font=("Arial Bold", 14))
plain3.grid(column=0, row=4)
ciphertxt = Entry(window, width=90)
ciphertxt.grid(column=1, row=4)

plain4 = Label(window, text="Văn bản được giải mã", font=("Arial Bold", 14))
plain4.grid(column=0, row=5)
dectxt = Entry(window, width=90)
dectxt.grid(column=1, row=5)

plain5 = Label(window, text="Khóa cá nhân", font=("Arial Bold", 14))
plain5.grid(column=0, row=6)
pri_key = Text(window, height=10, width=65)
pri_key.grid(column=1, row=6)

plain6 = Label(window, text="Khóa công khai", font=("Arial Bold", 14))
plain6.grid(column=0, row=7)
pub_key = Text(window, height=10, width=65)
pub_key.grid(column=1, row=7)

button = Button(window, text="Tạo khóa", command=generate_key)
button.grid(column=1, row=8)

button1 = Button(window, text="Mã hóa", command=mahoa_rsa)
button1.grid(column=1, row=9)

button2 = Button(window, text="Giải mã", command=giaima_rsa)
button2.grid(column=1, row=10)


window.geometry('800x600')
window.mainloop()
