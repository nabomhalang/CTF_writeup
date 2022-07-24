from pwn import *

p = process("./online_library")
e = ELF("./Online Library")

p.interactive()