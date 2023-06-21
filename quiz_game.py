print("Welcome to my Kings Island quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play!")
score = 0

class Question:
    score = 0

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        
    def ask(self, question, answer):
        user_answer = input(question)
        if user_answer.lower() == answer:
            print("Correct")
            Question.score += 1
        else:
            print("Incorrect")
        return Question.score

question_1 = "What year did Kings Island open? "
answer_1 = "1972"

question_2 = "What is the name of the spinning barrel ride? "
answer_2 = "cargo loco"

question_3 = "Which coaster holds a World Record? "
answer_3 = "the beast"

question_4 = "Is Adventure Express a Steel or Wood coaster? "
answer_4 = "steel"

question_5 = "Who currently owns Kings Island? "
answer_5 = "cedar fair"

question_6 = "True or False? The Beast is manufactured by Great Coasters International "
answer_6 = "false"

question_7 = "As of 2023, how many coasters does the park have? "
answer_7 = "14"

question_8 = "Which movie company owned Kings Island previously? "
answer_8 = "paramount"

question_9 = "What TV show filmed an episode in the park in 1973? "
answer_9 = "the brady bunch"

question_10 = "How many buses did Evel Knievel jump over at Kings Island? "
answer_10 = "14"

complete1 = Question(question_1, answer_1)
complete2 = Question(question_2, answer_2)
complete3 = Question(question_3, answer_3)
complete4 = Question(question_4, answer_4)
complete5 = Question(question_5, answer_5)
complete6 = Question(question_6, answer_6)
complete7 = Question(question_7, answer_7)
complete8 = Question(question_8, answer_8)
complete9 = Question(question_9, answer_9)
complete10 = Question(question_10, answer_10)

complete1.ask(question_1, answer_1)
complete2.ask(question_2, answer_2)
complete3.ask(question_3, answer_3)
complete4.ask(question_4, answer_4)
complete5.ask(question_5, answer_5)
complete6.ask(question_6, answer_6)
complete7.ask(question_7, answer_7)
complete8.ask(question_8, answer_8)
complete9.ask(question_9, answer_9)
complete10.ask(question_10, answer_10)

print("You got " + str(Question.score) + " questions correct!")
print("You got " + str(Question.score/10 * 100) + "%.")

# TODO: Iterate through questions to avoid copying code