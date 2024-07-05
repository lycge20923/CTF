import requests
import gmpy2
from Cryptodome.Util import number

with open('RSA_Noob/rsanoob.txt','r') as f:
    data = f.readlines()
e = int(data[0].split(':')[1][:-1])
c = int(data[1].split(':')[1][:-1])
n = int(data[2].split(':')[1])
result = requests.get("http://factordb.com/api?query={}".format(str(n))).json()
p, q = int(result['factors'][0][0]), int(result['factors'][1][0])
d = gmpy2.invert(e, (p - 1) * (q - 1))
p = pow(c, d, n)
FLAG = number.long_to_bytes(p).decode()
print(FLAG)