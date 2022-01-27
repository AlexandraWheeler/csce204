# author: Alexandra WHeeler

temp =  int(input("Enter temperature: "))
precip = input("Enter (R)ain, (S)now, or (N)one").lower().strip()

if (temp <= 40 and precip == "s"):
    print("You need a snowsuit.")
elif (temp <=40 and precip == "r"):
    print("You need a rain jacket and warm clothes.")
elif temp <=40:
    print("You need warm clothes")
elif (temp >=40 and precip == "r"):
    print("You need a rain jacket")
