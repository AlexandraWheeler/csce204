print("Welcome to my toy store")
toys = ["truck", "car", "doll", "jump rope", "train"]

while True:
    command = input("(V)iew, (A)dd, (R)emove, (Q)uit: ").lower().strip()

    if command == "q":
        break
    elif command == "a":
        toy =  input("Enter toy: ")
        toys.append(toy)
        print(f"{toy} was added.")
    elif command == "r":
        toy = input("Enter toy: ")
        toys.remove(toy)
        print(f"{toy} was removed. ")
    elif command == "v":
        for toy in toys:
            print(f"- {toy}")
    else:
        print("Invalid")
