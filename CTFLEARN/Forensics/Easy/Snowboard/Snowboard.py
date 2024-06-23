import os
import base64
os.system('strings Snowboard/Snowboard.jpg > Snowboard/Snowboard.txt')

with open('Snowboard/Snowboard.txt', 'r') as f:
    txt = f.readlines()

encoded = txt[2][:-1]
FLAG = base64.b64decode(encoded).decode()[:-1]
print(FLAG)
os.system('rm Snowboard/Snowboard.txt')