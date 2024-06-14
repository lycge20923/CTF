text = 'gwox{RgqssihYspOntqpxs}'
index, key = 0, 'blorpy' 
FLAG = ''
for c in text:
    if c in ('{', '}'):
        FLAG += c
    else:
        if c.islower():
            ch = chr((ord(c) - ord(key[index])) % 26 + ord('a'))
        else:
            ch = chr((ord(c) - ord(key[index].upper())) % 26 + ord('A'))
        FLAG += ch
        index = (index + 1) % len(key)
print(FLAG)