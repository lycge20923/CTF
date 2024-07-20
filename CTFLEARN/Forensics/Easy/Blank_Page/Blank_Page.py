from Crypto.Util.number import long_to_bytes

with open('Blank_Page/TheMessage.txt','r') as f:
    data = f.read()
'''    
for i in data:
    print(repr(i))
'''
res = ''
for c in data:
    res = res + '0' if ord(c) == 32 else res + '1'
Flag = long_to_bytes(int(res,2)).decode()

print(Flag)