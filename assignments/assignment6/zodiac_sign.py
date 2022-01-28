# Author: Alexandra Wheeler
# If statement fortune telling

print("***Monthly Fortune Telling***")

userChoice = input("What would you like to do? (V)iew signs or see your (F)ortune? ").lower().strip()
zodiacSign = ""

if userChoice == "v":
    print(f"""Astrological Signs and Dates:
    - Aries: March 21 - April 19
    - Taurus: April 20 - May 20
    - Gemini: May 21 - June 21
    - Cancer: June 22 - July 22
    - Leo: July 23 - August 22
    - Virgo: August 23 - September 22
    - Libra: September 23 - October 23
    - Scorpio: October 24 - November 21
    - Sagittarius: November 22 - December 21
    - Capricorn: December 22 - January 19
    - Aquarius: January 20 - February 18
    - Pisces: February 19 - March 20""")
elif userChoice == "f":
    zodiacSign = input("Enter your sign: ").lower().strip()
    if zodiacSign == "aries":
        print("You will be asked to tap into your power on a professional level.")
    elif zodiacSign == "taurus":
        print("You will find a new hobby.")
    elif zodiacSign == "gemini":
        print("You will start a new book this month.")
    elif zodiacSign == "cancer":
        print("You will lose money trying to start something new.")
    elif zodiacSign == "leo":
        print("You will lose a friend this month.")
    elif zodiacSign == "virgo":
        print("You will find happiness with an additional person who comes into your life.")
    elif zodiacSign == "libra":
        print("You will start a new creative project this month.")
    elif zodiacSign == "scorpio":
        print("You will meet a new animal friend.")
    elif zodiacSign == "sagitarrius":
        print("You will encounter sadness with the loss of something or someone.")
    elif zodiacSign == "capricorn":
        print("You will have a new idea that changes your life.")
    elif zodiacSign == "aquarius":
        print("You will encounter a new health and wellness journey.")
    elif zodiacSign == "pisces":
        print("You will finally ask for and get the help you need in your life.")

print("Have a nice day!")

