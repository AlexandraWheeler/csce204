from question import Question
import random
def getQuestions():
    questions = []
    with open("examples/april7/questions.txt") as file:
        for line in file:
            data = line.split(',')
            prompt = data[0].strip()
            answer1 = data[1].strip()
            answer2 = data[2].strip()
            answer3 = data[3].strip()
            answer4 = data[4].strip()
            correctAnswer = int(data[5].strip())
            questions.append(Question(prompt,answer1,answer2,answer3,answer4,correctAnswer))

    return questions

print("Welcome to our Trivia Game!")

while True:
    command =  input("(P)lay or (Q)uit? ").strip().lower()
    if command == "q":
        break
    elif command != "p":
        print("Invalid Command")
        continue

    question = random.choice(getQuestions())
    print("\n" + question.prompt)
    question.displayAnswers()

    userAns = int(input("Enter numerical answer: "))
    if question.isCorrect(userAns):
        print("Nicely done")
    else:
        print("Wrong Answer")

print("Goodbye")