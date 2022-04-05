class Question:
    def __init__(self, prompt, answer1, answer2, answer3, answer4, correctAnswer):
        self.prompt = prompt
        self.answers = (answer1,answer2,answer3,answer4)
        self.correctAnswer = correctAnswer

        def displayAnswers(self):
            for i in range(len(self.answers)):
                print(f"{i+1}. {self.answers[i]}")

        def isCorrect(self,answer):
            if answer == self.correctAnswer + 1:
                return True
            else: 
                return False 