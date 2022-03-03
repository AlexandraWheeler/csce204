def factorial(num):
    ans = 1

    for i in range(1,num+1):
        ans *= i

    print(f"{num}! = {ans}")

factorial(7)

def sum(num):
    ans = 1
    for i in range(2, num+1):
        ans += i
    print(f"sum {num} = {ans}")

sum(5)

def power(base,exponent):
    ans = 1
    for i in range(exponent):
        ans *= base
    print(f"{base}^{exponent} = {ans}")

power(2,3)

def prime(num):
    ans = 1
    for i in range(2,num):
        if num % i == 0:
            print(f"{num} is not prime")
            return
    print(f"{num} is prime")

prime(37)