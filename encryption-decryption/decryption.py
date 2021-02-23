from cryptography.fernet import Fernet
from encryption import key
from encryption import encrypted
import csv

f = Fernet(key) 

with open('encryption-decryption/enc_testData.csv', "rb") as file:
    # read all file data
    encrypted = file.read()

decrypted = f.decrypt(encrypted)

with open('encryption-decryption/dec_testData.csv', 'wb') as file: 
    file.write(decrypted)

