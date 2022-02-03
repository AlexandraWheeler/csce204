# Author: Alexandra Wheeler
# Looping factors

print("Lets Count Factors")
num = int(input("Enter a number: "))
print("Factors of your number are: ")

x = 1
while x <=num:
    if num%x==0:
        print(f"-{x}")
    x = x + 1

