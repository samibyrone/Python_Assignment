deposit = 0
withdraw = 0
balance = 0
newbalance = 0

print(' Welcome to En-Hakkore Mobile Banking App. ')
print(' How can we be of service to you? ')
print()

while True:
		account = int(input(''' 1, Deposit
 2, Withdraw
 3, Balance \n '''))
		print()
	
		match account :
			case 1:
				print(' Deposit ')
				deposit = int(input(" Enter amount to deposit: "))
				print(" your Deposit is: ", deposit)
				balance += deposit
				print(" Your available Balance is: ", balance)	
			
			case 2:
				print(' Withdraw ')
				withdraw = int(input(" Enter amount to withdraw: "))
				newbalance = balance - withdraw
				if withdraw <= 0:
					print(" Insuffucient Funds, Kindly make some Deposit!!! ")
				if withdraw > balance:
					print(" Insuffucient Funds, Kindly make some Deposit!!! ")
					print(" your withdraw is: ", withdraw)

			case 3:
				print(' Balance ')
				if newbalance < 0:
					newbalance = newbalance * (-1)
				print(" Your Current Available Balance is: ", newbalance)
				break

			case _:
				print(" Invalid input, please try again!!! ")
				

		