# Author: Alexandra Wheeler 01/20/2022
# Calculating Trip Price

gallonPrice = 3.159
gallonMiles = 24.9
breakfast = 10.0
lunch = 12.50
dinner = 20.0
hotel = 103.25

print("How much will your trip cost! ")
numMiles = float(input("How many miles did you travel? "))
numDays = int(input("How many days did you travel? "))

# calculations
totalGas = numMiles / gallonMiles * gallonPrice
totalStay = numDays * breakfast + numDays * lunch + numDays * dinner + numDays * hotel
totalCost = totalGas + totalStay

print(f"Total travel cost: ${round(totalCost , 2)}")