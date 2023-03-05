#Cao Minh Nhut
#B1709556
#04

#import
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5
import base64


window = Tk()
window.title("Thực hành buổi 3 - Application")

#ui
lb_empty_0 = Label(window, text='', font=("Arial Bold", 10))
lb_empty_0.grid(column=0, row=0)

lb_txt_view_1 = Label(window, text='CHƯƠNG TRÌNH DEMO', font=("Arial Bold", 18))
lb_txt_view_1.grid(column=1, row=1)

lb_txt_view_2 = Label(window, text='MẬT MÃ ĐỐI XỨNG RSA', font=("Arial Bold", 14))
lb_txt_view_2.grid(column=1, row=2)

lb_txt_view_3 = Label(window, text='Văn bản gốc: ', font=("Arial Bold", 12))
lb_txt_view_3.grid(column=0, row=3)

ln_edit_1= Entry(window, width=120)
ln_edit_1.grid(column=1, row=3)

lb_txt_view_4 = Label(window, text='Văn bản được mã hóa: ', font=("Arial Bold", 12))
lb_txt_view_4.grid(column=0, row=4)

ln_edit_2= Entry(window, width=120)
ln_edit_2.grid(column=1, row=4)

lb_txt_view_5 = Label(window, text='Văn bản được giải mã: ', font=("Arial Bold", 12))
lb_txt_view_5.grid(column=0, row=5)

ln_edit_3= Entry(window, width=120)
ln_edit_3.grid(column=1, row=5)

lb_txt_view_6 = Label(window, text='Khóa cá nhân: ', font=("Arial Bold", 12))
lb_txt_view_6.grid(column=0, row=6)

ln_edit_4= Entry(window, width=100, height=60)
ln_edit_4.grid(column=1, row=6)

lb_txt_view_7 = Label(window, text='Khóa công khai: ', font=("Arial Bold", 12))
lb_txt_view_7.grid(column=0, row=7)

ln_edit_5= Entry(window, width=100, height=60)
ln_edit_5.grid(column=1, row=7)

btn_taokhoa = Button(window, text= "Tạo khóa!")
btn_taokhoa.grid(column=2, row=8)

btn_mahoa = Button(window, text='Mã hóa!')
btn_mahoa.grid(column=0, row=9)

btn_giaima = Button(window, text='Giải mã!')
btn_giaima.grid(column=1, row=10)

#xuly
from tkinter import *
from tkinter import filedialog

def generate_key():
    key = RSA.generate(1024)
    pri = save_file(key.exportKey('PEM'),
                    'wb',
                    'Lưu khóa cá nhân',
                    ("All files", "*.*"), ("PEM files", "*.pem")),
                    ".pem")
    pub = save_file(key.publickey().exportKey('PEM'),
                    'wb',
                    'Lưu khóa công khai',
                    (("All files", "*.*"),("PEM files", "*.pem")),
                    ".pem")
 pri_key.delete('1.0',END)
 pri_key.insert(END,key.exportKey('PEM'))
 pub_key.delete('1.0',END)
 pub_key.insert(END,key.publickey().exportKey('PEM'))

def save_file(content, _mode, _title, _filetypes,_defaultextension):
    f = filedialog.asksaveasfile(mode = _mode,
                            initialdir = "C:/",
                            title = _title,
                            filetypes = _filetypes,
                            defaultextension = _defaultextension)
    if f is None: return
    f.write(content)
    f.close()

def get_key(key_style):
    filename = filedialog.askopenfilename(initialdir = "C:/",
                                    title = "Open " + key_style,
                                    filetypes = (("PEM files", "*.pem"),("All
                                    files", "*.*")))
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