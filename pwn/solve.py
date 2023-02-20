from pwn import *
p = process('/bin/ls')

print(p.readall().decode())