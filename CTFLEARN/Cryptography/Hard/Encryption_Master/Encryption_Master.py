from base64 import b64decode

path = 'Encryption_Master/Here ya go!.txt'
with open(path, 'r') as f:
    data = f.read()
encrypt1 = data.split(' ')[-1]
encrypt2 = b64decode(encrypt1).decode().split(' ')[-1]
encrypt3 = bytes.fromhex(encrypt2).decode().split('.')[-1][1:]
encrypt4 = "".join([chr(int(ele, 2)) for ele in encrypt3.split(" ")])
Flag = b64decode(encrypt4.split(' ')[-1]).decode()
print(Flag)
