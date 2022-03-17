def haircutCost(gender, length, density):
    baseCost = 0
    if gender == "f":
        baseCost += 40
    else:
        baseCost += 20
    if length == "l":
        baseCost += 10
    if density == "t":
        baseCost += 15
    return baseCost
        
def colorCost(length, density, change):
    baseCost = 50
    if length == "l":
        baseCost += 20
    if density == "t":
        baseCost += 20
    if change == "l":
        baseCost += 50
    return baseCost

print("***Salon Calculator***")
gender = input("(M)ale or (F)emale: ").strip().lower()
length = input("Hair Length: (L)ong or (S)hort? ").strip().lower()
density = input("Hair Density: (T)hick or (Th)in? ").strip().lower()
haircut = input("Haircut? (Y)es or (N)o: ").strip().lower()
cost = 0
if haircut == "y":
    cost += haircutCost(gender,length,density)


coloring = input("Hair color? (Y)es or (N)o: ").strip().lower()
if coloring == "y":
    color = input("What color? (L)ighter or (D)arker: ").strip().lower()
    cost += colorCost(length, density, coloring)
totalCost = totalCost * 1.07
print(f"Your total will be ${round(totalCost,2)}.")
