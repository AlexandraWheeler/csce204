#Author: Alexandra Wheeler

import math

# Incrementing age
age = float(input("Enter age: "))
decade = 10

future_age = age + decade
print(f"Your future age is {future_age}.")


# Pizza party
print("We're having a pizza party!")
numGuests = int(input("How many guests? "))
avgSlices = float(input("Enter average number of slices per guest: "))
totalSlices = numGuests * avgSlices
pizzas = math.ceil(totalSlices // 8)
print(f"We will need {pizzas} pizzas")

# Chickens and eggs
numEggs = int(input("How many eggs did you collect today? "))
numCartons = numEggs // 12
# extraEggs = numEggs - numCartons * numEggs
extraEggs = numEggs % 12 # remainder after division
print(f"""You need {numCartons} cartons.
You have {extraEggs} eggs left over""")


# Wage
hourlyWage = float(input("How much do you get paid per hour? "))
#overtime = hourlyWage * 1.5
hourlyWage *= 1.5
#print(f"You should make ${hourlyWage} in overtime. ")
print(f"You should make ${round(hourlyWage, 2)} in overtime. ")
