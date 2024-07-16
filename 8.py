string = input('string : ')
strings = ('')


for char in string :
	if char == char.upper():
		a = '_'+char.lower()
		print(a,end='')
		
	if char == char.lower():
		c= char.lower()
		print(c ,end='')
		