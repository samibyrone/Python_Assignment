amount = 0
interest = 0
duration = 0
total = 0

amount = input('\n Enter your principal amount: ')
amount = float(amount)

interest = input('\n Enter your annual interest rate: ')
interest = float(interest) / 100 / 12

duration = input('\n enter the duration in years: ')
duration = float(duration) * 12

mortgagePayment = amount * (interest * (1 + interest) ** duration) / ((1 + interest) ** duration - 1)

print(" Your monthly mortgage payment is: $%.2f " % mortgagePayment  )

