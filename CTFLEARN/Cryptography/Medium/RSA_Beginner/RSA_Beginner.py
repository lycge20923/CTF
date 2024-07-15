import requests
from Crypto.Util.number import * 

with open('RSA_Beginner/rsa.txt', 'r') as file:
    data = file.readlines()
e, c, n = int(data[0].split(':')[1][:-1]), \
            int(data[1].split(':')[1][:-1]), \
                int(data[2].split(':')[1])
result = requests.get("http://factordb.com/api?query={}".format(str(n))).json()['factors']
p, q = int(result[0][0]), int(result[1][0])
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
plaintext = pow(c, d, n)
Flag = long_to_bytes(plaintext).decode()
print(Flag)