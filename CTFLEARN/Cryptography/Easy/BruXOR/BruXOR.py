text = "q{vpln'bH_varHuebcrqxetrHOXEj"
index = 0
while True:
    FLAG = ""
    for c in text:
        if 33 <= (ord(c) ^ index) <= 126:
            FLAG += chr(ord(c) ^ index)
        else:
            break
    else:
        if 'flag' in FLAG.lower():
            break
    index += 1
print(FLAG)