#Mad Libs Assignment
#Author: Alexandra Wheeler

print("Complete the Mad Lib:")
first_number = input("Pick a number between 0 and 1000: ")
second_number = input("Pick a number between 0 and 10: " )
animal = input("Choose an animal: ")
liquid = input("Choose any liquid: ")
third_number = input("Pick a number between 0 and 10: ")
first_adj = input("Choose an adjective: ")
sweet_food = input("Choose a dessert: ")
fourth_number = input("Choose a number between 1 and 60: ")
second_adj = input("Choose an adjective: ")
print("***Cake Recipe***")
print(f"""First preheat the oven to {first_number} degrees. Then beat {second_number} {animal} egg(s) with a cup of {liquid}.  
Next add {third_number} teaspoon(s) of baking soda and mix with eggs and {liquid} until it reaches a {first_adj} texture.  
Don't forget the {sweet_food}! Pour into a 9 by 9 pan and bake for {fourth_number} minute(s) or until the cake is {second_adj}.""")