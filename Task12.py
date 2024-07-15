
print("\n Application that reads in Five-digit Integer and Determine Whether it's a Palindrome. ")

number = input("\n Enter your number: "))

temp = number
sum = 0

while(number > 0 ):

    digit = number % 10

    sum = sum * 10 + digit

    number = number // 10

if(temp == sum):
	print("\n The number is a palindrome! ")
else:
	print("\n The number isn't a palindrome! ")