def factorial(num):
    ans = 1

    for i in range(1,num+1):
        ans *= i

    print(f"{num}! = {ans}")

def sum(num):
    ans = 1
    for i in range(2, num+1):
        ans += i
    print(f"sum {num} = {ans}")

def power(base,exponent):
    ans = 1
    for i in range(exponent):
        ans *= base
    print(f"{base}^{exponent} = {ans}")

def prime(num):
    ans = 1
    for i in range(2,num):
        if num % i == 0:
            print(f"{num} is not prime")
            return
    print(f"{num} is prime")

while True:
    command = input("(S)um, (P)ower, (F)actorial, P(R)ime, or (Q)uit: ").strip().lower()
    if command == "q":
        break
    elif command == "s":
        num = int(input("Enter number: "))
        sum(num)
    elif command == "p":
        base = int(input("Enter number: "))
        exponent = int(input("Enter number: "))
        power(base, exponent)
    elif command == "f":
        num = int(input("Enter number: "))
        factorial(num)
    elif command == "r":
        num = int(input("Enter number: "))
        prime(num)
    else: 
        print("Invalid command")
print("Goodbye")

