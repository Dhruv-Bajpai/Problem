import random

print('number guess game')
number=random.randint(1,10)

Input=int(input('plz enter a number '))
while Input != number:
	print('no')
	inpu =input('do u want answer '  )
	if inpu== 'yes':
		print(number)
	Input=int(input('plz enter a number ')) 

if Input == number :
	print('yes' )