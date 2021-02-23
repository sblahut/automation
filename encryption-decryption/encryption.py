from cryptography.fernet import Fernet

# Create key
key = Fernet.generate_key() 
with open('token.key', 'wb') as key_file: 
    # This will write a random string as the file
    key_file.write(key)

# Load key   
with open('token.key', 'rb') as key_file:
    key = key_file.read()

# Encrypting the file 
f = Fernet(key)

with open('encryption-decryption/testData.csv', "rb") as file:
    # read all file data
    original = file.read()

encrypted = f.encrypt(original)

# writing the encrypted data 
with open('encryption-decryption/enc_testData.csv', 'wb') as file: 
    file.write(encrypted)







