try:
	print ('x * y = xy ')
	x= int(input ('what is x '))
	
	for i in range(10):
		var=i+1
		print(x, '*', i+1,'=' , x*var )
except Exception:
	print('enter a valid x ')
