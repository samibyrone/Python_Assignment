total = 0
for number in range(1, 101):
	print(number)
	if number % 2 == 1:
		total += number 
print(total)

total = 0
for number in range(1, 101, 2):
	print(number)
	total += number n
print(total)

total = 0
for number in range(101, 1, -2):
	print(number)
	total += number 
print(total)



evenNumber = 0
oddNumber = 0

for index in range(0, 11):
	index = int(input( " Enter your number: "))
	if index % 2 == 0:
		evenNumber += index
	elif index % 3 == 1:
		oddNumber += index

print(" This is an Even number ", evenNumber )
print(" This is an Odd number ", oddNumber )



# ternary operator

score = int(input(" Enter your input: "))
result = 'passed' if score > 45 else 'failed'
print(result)