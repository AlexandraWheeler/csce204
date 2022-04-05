from question import Question
import random
questions = (
    Question("What type of animal is a seahorse?", "Crustacean", "Arachnid", "Fish", "Shell", 2),
    Question("Which of the following dog breeds is the smallest?", "Dachshund", "Poodle", "pomeranian", "Chicuahua", 3),
    Question("What color are zebras?", "White with black stripes?", "Black with white stripes", "Both of the above", "None of the above", 1),
    Question("What existing bird has the largest wingspan?", "Stork", "Swan", "Condor", "Albatross", 3)
)

print("Welcome to our Trivia Game!")

while True:
    command =  input("(P)lay or (Q)uit? ").strip().lower()
    if command == "q":
        break
    elif command != "p":
        print("Invalid Command")
        continue

    question = random.choice(questions)
    print("\n" + question.prompt)
    question.displayAnswers()

    userAns = int(input("Enter numerical answer: "))
    if question.isCorrect(userAns):
        print("Nicely done")
    else:
        print("Wrong Answer")

print("Goodbye")