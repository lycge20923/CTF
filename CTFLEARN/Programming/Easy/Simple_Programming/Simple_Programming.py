with open('Simple_Programming/data.dat', 'r') as f:
    data = f.read()
count = [0, 0]
FLAG = 0
for e in data:
    if e == '0':
        count[0] += 1
    elif e == '1':
        count[1] += 1
    elif e == '\n':
        if count[0] % 3 == 0 or count[1] % 2 == 0:
            FLAG += 1
        count = [0, 0]
print(FLAG)
    