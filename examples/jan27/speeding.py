# Author: Alexandra WHeeler

speed = float(input("Enter speed: "))
ticket_price = 0

if speed >= 100:
    print("Time to stay overnight")
    ticket_price = 20 * (speed-70)
elif speed >= 90:
    print("Time for a ticket")
    ticket_price = 10 * (speed-70)
elif speed > 80:
    print("Warning!")
elif speed > 70:
    print("Not cool.")
elif speed > 60:
    print("Good job")
elif speed > 50:
    ("Speed up")
else:
    print("Too slow.")
    

if ticket_price > 0:
    print(f"You are charged ${ticket_price}.")