from base64 import b64decode

encoded_txt = '==QTh9lMx8Fd08VZt9FdFNTb'
Flag = b64decode(encoded_txt[::-1]).decode()
print(Flag)