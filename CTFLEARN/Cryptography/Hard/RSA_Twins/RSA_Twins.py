import requests
import gmpy2
from Crypto.Util.number import *

with open('RSA_Twins/rsa.txt', 'r') as f:
    data = f.readlines()
n = int(data[0].split('= ')[-1][:-1])
e = int(data[2].split('= ')[-1][:-1])
c = int(data[4].split('= ')[-1])
result = requests.get("http://factordb.com/api?query={}".format(str(n))).json()['factors']
p, q = int(result[0][0]), int(result[1][0])
#print(p, q)
d = inverse(e, (p - 1) * (q - 1))
Flag = long_to_bytes(pow(c, d, n)).decode()
print(Flag)

