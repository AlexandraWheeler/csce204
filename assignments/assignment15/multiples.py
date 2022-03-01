# Author: Alexandra Wheeler
# Listing Multiples


def multiple(num):
    list = []
    for i in range(101):
        remainder = i % num
        if remainder == 0:
            list.append(i)
        elif i > 100:
            return
    print(list)

while True:
    user_choice = input("(L)ist Multiples, or (Q)uit: ").strip().lower()
    if user_choice == "l":
        user_num = int(input("Enter a number: "))
        multiple(user_num)
    elif user_choice == "q":
        break

print("Goodbye")
    




