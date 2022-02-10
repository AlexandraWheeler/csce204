toys = ["car", "truck", "doll", "train", "legos"]
#print(toys[3])
toys.append("jump rope")
toys.pop()

#toys=[]
#toys.append("cars")
#toys.append("truck")

for i in range(len(toys)):
    print(toys[i])

for toy in toys:
    print(toy)