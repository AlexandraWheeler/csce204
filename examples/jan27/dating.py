#Author: Alexandra Wheeler

status = input("Enter relationship status: ").lower().strip()

if(not(status == "married" or status == "dating")):
    print("You can come! ")
elif status == "married" or status == "dating":
    print("You cannot come!")
