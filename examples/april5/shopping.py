from functools import total_ordering
from product import Product

shoppingList = {
    Product("Shoes","Black and White Tennis Shoes", 59.99),
    Product("Doll", "Walking and Talking Fun Doll", 29.99),
    Product("Scrabble", "Fun Word Game to Play with Friends and Family", 15.99)
}
print("Your shopping list:")
totalCost = 0
for product in shoppingList:
    product.display()
    totalCost += product.getTotal()

print(f"Total Cost: ${round(totalCost,2)}")


