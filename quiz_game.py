print("Welcome to my Kings Island quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play!")
score = 0

answer_1 = input("What year did Kings Island open? ")
if answer_1.lower() == "1972":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer_2 = input("What is the name of the spinning barrel ride? ")
if answer_2.lower() == "cargo loco":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer_3 = input("Which coaster holds a World Record? ")
if answer_3.lower() == "the beast":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer_4 = input("Is Adventure Express a Steel or Wood coaster? ")
if answer_4.lower() == "steel":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer_5 = input("Who owns Kings Island? ")
if answer_5.lower() == "cedar fair":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer_6 = input("True or False? The Beast is manufactured by Great Coasters International ")
if answer_6.lower() == "false":
    print("Correct! It was made in-house!")
    score += 1
else:
    print("Incorrect.")

answer_7 = input("As of 2023, how many coasters does the park have? ")
if answer_7.lower() == "14":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer_8 = input("Which movie company owned Kings Island previously? ")
if answer_8.lower() == "paramount":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer_9 = input("What TV show filmed an episode in the park in 1973? ")
if answer_9.lower() == "the brady bunch":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer_10 = input("How many buses did Evel Knievel jump over at Kings Island? ")
if answer_10.lower() == "14":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")    

print("You got " + str(score) + " questions correct!")
print("You got " + str(score/10 * 100) + "%.")

# TODO: Change questions to class