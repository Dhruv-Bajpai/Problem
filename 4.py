try:
	var1=int(input('enter x '))
	var2 =int(input('enter y '))
	if var1/var2 == 1/2 :
		print('50%')
	elif var1/var2 == 1/4 :
		print('25%')
	elif var1/var2 == 3/4 :
		print('75%')
	elif var1/var2 == 1 or 99/100:
		print('F')
	elif var1/var2 == 0 or 1/100:
		print('E')
except ZeroDivisionError:
	pass
