import os
import base64
os.system('strings Tux/Tux.jpg > Tux/term.txt')
with open('Tux/term.txt', 'r') as f:
    encrypt = f.readlines()[1][:-1]

password = base64.b64decode(encrypt).decode().strip()

os.system('binwalk -e Tux/Tux.jpg')
print("Input the password:{}".format(password))
os.system('unzip Tux/_Tux.jpg.extracted/1570.zip -d Tux/')

with open('Tux/flag', 'r') as f:
    print(f.read().strip())


os.system('rm -r Tux/_Tux.jpg.extracted')
os.system('rm Tux/flag')
