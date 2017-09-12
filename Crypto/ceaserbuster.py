string = input('Give meh a string: \n > ')
inplaintext = input('If you know any plaintext give it here (else type "no"):  \n')

string = string.lower()
inplaintext = inplaintext.lower()

for i in range(1, 27): 
	shift = i
	plaintext = '' 
	for char in string: 
		if ord(char) < 97 or ord(char) > 122: 
			plaintext += char
		elif ord(char) + i <= 122: 
			plaintext += chr(ord(char)+i)
		else: 
			plaintext += chr(96 +(ord(char)+i - 122))  
	#print(plaintext)
	if inplaintext != 'no': 
		if inplaintext in plaintext: 
			print(plaintext) 
			break
		else: 
			continue
	else: 	
		print(plaintext)
		response = input("Does this look right? (Y/N) \n")
		response = response.lower()
		if response == 'y': 
			print(plaintext)
			break
		else: 
			continue
