# Author: Alexandra Wheeler
# List of shoes

shoes = []
command = "y"
print("Shoe Inventory")
while command== "y":
    shoe = input("Enter shoe name: ")
    shoes.append(shoe)
    command = input("Do you have more shoes to add? (Y or N) ").lower().strip()
    if command == "n":
        print("Heres your shoe inventory: ")
        for shoe in shoes:
            print(f"- {shoe}")


