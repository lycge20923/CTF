import base64

with open('So_many_64s/flag.txt', 'r', encoding='utf-8') as f:
    data = f.read()

while True:
    data = base64.b64decode(data).decode()
    if 'abctf' in data.lower():
        break

flag = data
print(flag)