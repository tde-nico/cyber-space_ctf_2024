from pwn import xor

with open('encrypted.txt', 'r') as f:
	encrypted = f.read().strip()
encrypted = bytes.fromhex(encrypted)
plaintext = len(encrypted) * b'a' + b'\n'
chiphertext = "675e2b771cba0a52d20d3878edd63fc30c89169e2969a9f28720af6af700fa98380cdb7aff583773465a"
chiphertext = bytes.fromhex(chiphertext)

key = [a ^ b for a, b in zip(plaintext, chiphertext)]

flag = xor(encrypted, key)
print(flag)

# CSCTF{y0u_br0k3_my_3ng1ne_h3re_th3_g1ft}
