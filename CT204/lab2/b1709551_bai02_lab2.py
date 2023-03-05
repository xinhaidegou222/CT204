#Nguyen Thanh Nghia
#B1709551
#STT: 03
#Nhom sang 4
#Lab2
#Bai2

#import
from cryptography.fernet import Fernet
#tao ra khoa ngau nhien
key = Fernet.generate_key()

#tao chuoi luu khoa
with open('file_key.key', 'wb') as filekey:
	filekey.write(key)

#mo file doc khoa
with open('file_key.key', 'rb') as filekey:
	key = filekey.read()

#lay khoa ra
fernet = Fernet(key)

#lay noi dung file muon ma hoa
with open('b1709551.txt', 'rb') as file:
	original = file.read()
	
#ma hoa noi dung file
encrypted = fernet.encrypt(original)

#luu noi dung da ma hoa vao file moi
with open('b1709551_encrypted.txt', 'wb') as encrypted_file:
	encrypted_file.write(encrypted)

#

#mo va doc noi dung file da duoc ma hoa
with open('b1709551_encrypted.txt', 'rb') as enc_file:
	encrypted = enc_file.read()

#giai ma file
decrypted = fernet.decrypt(encrypted)

#viet lai du lieu da duoc giai ma vao file moi
with open('b1709551_decrypted.txt', 'wb') as dec_file:
	dec_file.write(decrypted)

