import os 
from base64 import b64decode
os.system('binwalk -e Minions/Hey_You.png')
os.system('unrar e Minions/_Hey_You.png.extracted/D3EDB.rar Minions/ -Y')
os.system('rm -r Minions/_Hey_You.png.extracted')

with open('Minions/..txt', 'r') as f:
    path = f.read()
os.system('rm Minions/..txt')
os.system('megadl {} Minions/'.format(path))
os.system('mv Only_Few_Steps.jpg Minions/')

os.system('binwalk -e Minions/Only_Few_Steps.jpg')
os.system('mv Minions/_Only_Few_Steps.jpg.extracted/YouWon\(Almost\).jpg Minions/YouWon\(Almost\).jpg')
os.system('rm -r Minions/_Only_Few_Steps.jpg.extracted')

os.system('strings Minions/YouWon\(Almost\).jpg > Minions/res.txt')
os.system("rm Minions/Only_Few_Steps.jpg & rm Minions/YouWon\(Almost\).jpg")

with open('Minions/res.txt', 'r') as f:
    data = f.readlines()
    encoded = [ele[:-1] for ele in data if "CTF{" in ele][0][4:]

os.system('rm Minions/res.txt')

while 'C00L' not in encoded:
    encoded = b64decode(encoded).decode()

Flag = 'CTF{' + encoded + '}'
print(Flag)
