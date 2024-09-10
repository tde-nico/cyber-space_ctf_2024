from z3 import *

length = 32
f = [BitVec('flag_%d' % i, 32) for i in range(length)]
s = Solver()

s.add( f[21] + f[0] == 114 )
s.add( f[16] * f[1] == 11413 )
s.add( f[11] + f[2] == 174 )
s.add( f[9] + f[3] == 157 )
s.add( f[2] ^ f[4] == 78 )
s.add( f[19] + f[5] == 155 )
s.add( f[24] + f[6] == 142 )
s.add( f[21] * f[7] == 3080 )
s.add( f[8] - f[28] == 72 )
s.add( f[9] - f[31] == -47 )
s.add( f[10] + f[9] == 165 )
s.add( f[11] * f[6] == 3920 )
s.add( f[6] ^ f[12] == 15 )
s.add( f[13] - f[14] == -48 )
s.add( f[21] ^ f[14] == 26 )
s.add( f[16] * f[15] == 12726 )
s.add( f[16] * f[13] == 3939 )
s.add( f[17] - f[31] == 31 )
s.add( f[29] + f[18] == 82 )
s.add( f[2] * f[19] == 5928 )
s.add( f[20] + f[6] == 109 )
s.add( f[30] * f[21] == 3696 )
s.add( f[22] - f[24] == -32 )
s.add( f[27] + f[23] == 201 )
s.add( f[24] - f[4] == 48 )
s.add( f[25] - f[6] == 51 )
s.add( f[26] - f[10] == -18 )
s.add( f[27] + f[12] == 159 )
s.add( f[3] ^ f[28] == 95 )
s.add( f[29] - f[9] == 29 )
s.add( f[30] ^ f[26] == 87 )
s.add( f[31] + f[4] == 129 )
s.add( f[20] + f[10] == 174 )
s.add( f[16] ^ f[11] == 35 )
s.add( f[4] * f[23] == 3686 )
s.add( f[26] * f[3] == 11639 )
s.add( f[12] ^ f[31] == 108 )
s.add( f[12] * f[30] == 2640 )
s.add( f[20] * f[14] == 4611 )
s.add( f[19] ^ f[10] == 64 )
s.add( f[23] + f[0] == 134 )
s.add( f[9] - f[12] == -11 )
s.add( f[19] * f[4] == 2166 )
s.add( f[8] ^ f[15] == 8 )
s.add( f[15] ^ f[11] == 56 )
s.add( f[2] * f[22] == 5616 )
s.add( f[19] ^ f[24] == 111 )
s.add( f[16] + f[0] == 138 )
s.add( f[16] * f[18] == 909 )
s.add( f[15] * f[29] == 9198 )
s.add( f[27] + f[9] == 148 )
s.add( f[0] * f[20] == 1961 )
s.add( f[15] + f[8] == 244 )
s.add( f[23] + f[30] == 145 )
s.add( f[19] * f[12] == 3135 )
s.add( f[8] * f[26] == 12154 )
s.add( f[0] ^ f[2] == 77 )
s.add( f[12] - f[19] == -2 )
s.add( f[22] - f[28] == 8 )

if s.check() == sat:
	m = s.model()
	flag = ''.join([chr(m[f[i]].as_long()) for i in range(length)])
	import base64
	b64 = base64.b64encode(flag.encode()).decode()
	print(flag)
	print(b64)


import requests

URL = 'http://rev-trendzzzz.bugg.cc/saass'
r = requests.request('CONNECT', URL, headers={'X-Super-Secret': b64})

print(r)
print(r.text)

# CSCTF{47db65c7-7fec-429d-a065-d8b6e91bba21}
