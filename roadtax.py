cost_of_car = int(input(" Enter the price for the car: "))


if (cost_of_car < 1000000):
	road_tax = cost_of_car * 10 / 100
	print("Total cost of car is", cost_of_car, "and with tax is:", road_tax)

if (cost_of_car >= 1000000 and cost_of_car <= 300000):
	road_tax = cost_0f_car * 15 / 100
	print("Total cost of car is", cost_of_car, "and with tax is:", road_tax)

if(cost_of_car >= 3000000 and cost_of_car <= 5000000):
	road_tax = cost_of_car *20 / 100
	print("Total cost of car is", cost_of_car, "and with tax is:", road_tax)

if(cost_of_car >= 5000000):
	road_tax = cost_of_car * 25 / 100
	print("Total cost of car is", cost_of_car, "and with tax is:", road_tax)
