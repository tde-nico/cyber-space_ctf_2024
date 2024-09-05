import subprocess
import string

cmd = "valgrind --trace-children=yes --tool=callgrind ./vmvm vmvm.vm < flag.txt 2>&1 | grep refs | cut -d ' ' -f11"

flag = 'CSCTF{'

for i in range(64):
	if flag[-1] == '}':
		break
	for char in string.printable:
		with open('./flag.txt', 'w') as f:
			f.write(flag + char)
		p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
		res = p.communicate()[0].strip().decode()
		res = int(res.replace(',', ''))
	
		print(flag, char, res)
		if char == string.printable[0]:
			last = res
		else:
			if res > last:
				flag += char
				break
			elif last > res:
				flag += string.printable[0]
				break
	else:
		print('BRUH')
else:
	print('BRUH pt.2')

print(flag)

# CSCTF{i_would_make_gross_hidden_crypto_but_idk_crypto_f5f04dd12}