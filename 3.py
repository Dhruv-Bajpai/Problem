var = input('FILE : ')
if var.endswith(('jpg' or 'jpeg')):
	print('image/jpeg')
elif var.endswith(('gif')):
	print('image/gif')
else:
	print('application/occet-stream')
