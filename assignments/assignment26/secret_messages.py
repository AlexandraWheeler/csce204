#Author: Alexandra WHeeler
# Secret Messages


def toSymbols(message):
    answer = ""
    for letter in message:
            answer += str(ord(letter)) + "."
    return answer

def toLetters(message):
    message = message.split(".")

    answer = ""
    for symbol in message:
        answer += chr(int(symbol.strip()))
    return answer

#print(toSymbols("Hello friend"))
#print(toLetters("72.101.108.108.111.32.102.114.105.101.110.100"))

print("Secret Messages!")
while True:
    command = input("(E)ncode, (D)ecode, or(Q)uit: ").strip().lower()
    if command == "e":
        message = input("What is your message? ")
        encodedMessage = toSymbols(message)
        print(f"Your encoded message is {encodedMessage}")
    elif command == "d":
        message = input("What is your encoded message? ")
        decodedMessage = toLetters(message)
        print(f'Your secret message is "{decodedMessage}"')
    elif command == "q":
        break
    else:
        print("Invalid Command")

print("Goodbye!")



    

        
