def f_to_c(fahrenheit):
    celcius = (fahrenheit-32)*5/9
    return celcius

def c_to_f(celcius):
    fahr = celcius * 9/5 + 32
    return fahr

def m_to_km(miles):
    kilometers = miles * 1.60934
    return kilometers

def km_to_m(kilo):
    miles = kilo * .621371
    return miles

# conversion program

command = int(input(f"""
Enter type of conversion:
1: Fahrenheit to Celcius
2: Celcius to Fahrenheit
3: Miles or Kilometers
4: Kilometers to Miles 
"""))
value = float(input("Enter value: "))

if command == 1:
    result = f_to_c(value)
    print(f"{value}F={round(result,1)}C")
elif command == 2: 
    result = c_to_f(value)
    print(f"{value}C={round(result,1)}F")
elif command == 3:
    result = m_to_km(value)
    print(f"{value} miles={round(result,1)}km")
elif command == 4:
    result = km_to_m(value)
    print(f"{value}km={round(result,1)} miles")
else:
    print("Invalid Command")


    
