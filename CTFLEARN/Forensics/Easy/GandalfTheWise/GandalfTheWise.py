import os
from base64 import b64decode
from Crypto.Util.number import long_to_bytes
os.system('strings GandalfTheWise/Gandalf.jpg > GandalfTheWise/res.txt')
with open('GandalfTheWise/res.txt', 'r') as f:
    data = f.readlines()
hint = data[1][1:]
print(b64decode(hint).decode('utf-8')[:-1])
text1, text2 = data[2][1:-1], data[3][1:-1]
hex_t1, hex_t2 = b64decode(text1).hex(), b64decode(text2).hex()
Flag = long_to_bytes(int(hex_t1, 16) ^ int(hex_t2, 16)).decode()
print(Flag)
os.system('rm GandalfTheWise/res.txt')

#print(bytes.fromhex(text1.encode().hex()))
#print(long_to_bytes(int(text1.encode().hex(), 16) ^ int(text2.encode().hex(), 16)))