import os
from cryptography.fernet import Fernet
os.system("pip install cryptography")

files = []
for file in os.listdir():
    if file == "encrypt.py" or file == "thekey.txt" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

key = open("thekey.txt", "rb")
secret = key.read()
key.close()

for file in files:
    thefile = open(file, "rb")
    contents = thefile.read()
    thefile.close()
    decrypted_data = Fernet(secret).decrypt(contents)
    thefile = open(file, "wb")
    thefile.write(decrypted_data)
    thefile.close()




