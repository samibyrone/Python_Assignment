def only_floats(numb, num):
	counter = 0
	if numb is float(numb):
		counter += 1
	
	if num is float(num):
		counter += 1

	if numb is not float(numb) and num is not float(num):
		counter == 0
	return print(counter)
	
only_floats(12.1, 23)
only_floats(25.2, 75)