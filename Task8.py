print("\n THIS NUMBER CHECK FOR SQUARE AND CUBES OF NUMBERS ")

number = int(input("\n Enter number: "))

print ("Number \tSquare \tCube")

for loops in range(0, number+1):

	print(loops, "\t", loops **2, "\t", loops **3)