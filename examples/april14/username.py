import email
import random

# email: acw34@email.sc.edu, username: acw34
def getUsername(email):
    return email.split("@")[0]



def getPassword(phrase):
    password=""

    charConvert = {
        "a" : "@",
        "b" : "8",
        "c" : "4",
        "d" : "b",
        "e" : "*",
        "h" : "7",
        "i" : "!",
        "w" : "3",
        "o" : "0",
        "l" : "(",
        "j" : ")",
        "s" : "5"
    }

    for letter in phrase:
        if letter.lower() in charConvert:
            password += charConvert[letter.lower()]
        else:
            password += capatilize(letter)
    return password

def capatilize(letter):
    if random.randint(1,2) ==  1:
        return letter.upper()
    else:
        return letter.lower()


eMail = input("What is your email? ")
phrase = input("What is your password? ")
username = getUsername(eMail)
password = getPassword(phrase)
print(f"""
Username: {username}
Secure Password: {password}
""")