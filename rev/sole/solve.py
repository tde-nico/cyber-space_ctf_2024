from z3 import *

c = [BitVec(f"c{i}", 32) for i in range(26)]

s = Solver()

for i in range(26):
	if i == 5 or i == 25:
		continue
	else:
		# s.add(Or(
		# 	And(c[i] >= 0x30, c[i] <= 0x39),
		# 	And(c[i] >= 0x41, c[i] <= 0x41+25),
		# 	And(c[i] >= 0x61+26, c[i] <= 0x61+25),
		# 	c[i] == ord('_'),
		# 	c[i] == ord('-'),
		# ))
		s.add(And(c[i] >= 0x20, c[i] <= 0x7E))

s.add(c[0] == ord('C'))
s.add(c[1] == ord('S'))
s.add(c[2] == ord('C'))
s.add(c[3] == ord('T'))
s.add(c[4] == ord('F'))
s.add(c[5] == ord('{'))
s.add(c[25] == ord('}'))

v332 = c[19] * c[11]
s.add( c[4] * v332 == 0x5F76C )
v330 = c[13] * c[8]
s.add( c[22] * v330 == 0x8A9A8 )
v329 = c[22] * c[0]
s.add( c[15] + v329 == 4872 )
v328 = c[0] + c[8]
s.add( c[11] + v328 == 0xC7 )
v327 = c[22] * c[12]
s.add( c[13] - v327 == 0xFFFFF177 )
v326 = c[9] * c[4]
s.add( v326 - c[1] == 0x1F65 )
v325 = c[9] * c[16]
s.add( c[11] * v325 == 0x429C0 )
v324 = c[23] * c[3]
s.add( c[15] + v324 == 0x2640 )
v323 = c[9] - c[23]
s.add( v323 - c[4] == 0xFFFFFFBA )
v322 = c[5] - c[21]
s.add( v322 - c[8] == 0xFFFFFFC1 )
v321 = c[24] * c[3]
s.add( c[0] + v321 == 5359 )
v320 = c[25] * c[1]
s.add( c[17] + v320 == 10483 )
v319 = c[7] * c[19]
s.add( c[2] * v319 == 893646 )
v318 = c[11] - c[4]
s.add( c[19] + v318 == 93 )
v317 = c[7] + c[6]
s.add( v317 - c[10] == 136 )
v316 = c[0] + c[25]
s.add( c[10] + v316 == 287 )
v315 = c[12] + c[5]
s.add( v315 - c[22] == 104 )
v314 = c[4] * c[7]
s.add( v314 + c[12] == 8243 )
v313 = c[1] - c[22]
s.add( c[4] + v313 == 81 )
v312 = c[19] * c[11]
s.add( c[8] - v312 == -5503 )
v311 = c[8] - c[10]
s.add( v311 - c[7] == -129 )
v310 = c[20] + c[22]
s.add( c[21] + v310 == 224 )
v309 = c[24] + c[23]
s.add( c[12] + v309 == 232 )
v282 = c[15] - c[9]
s.add( c[4] + v282 == 2 )
v255 = c[9] * c[15]
s.add( c[2] + v255 == 5635 )
v228 = c[24] + c[14]
s.add( c[16] + v228 == 210 )
v201 = c[1] + c[10]
s.add( v201 - c[12] == 125 )
v174 = c[18] - c[1]
s.add( v174 - c[5] == -111 )
v147 = c[12] - c[14]
v146 = v147 - c[7]
s.add( v146 == 0xFFFFFF5D )
# v119 = c[1] + c[5]
# s.add( v119 == 158 )


if s.check() == sat:
	m = s.model()
	print(''.join([chr(m[c[i]].as_long()) for i in range(26)]))


# CSCTF{ruSt_15_c00l_r1gHt?}
