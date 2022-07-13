from pwn import *
context.clear(log_level='debug', os='linux', kernel='amd64')
p = remote("141.164.39.45", 5959)
# p = process("./logo")
e = ELF("./logo")



p.interactive()