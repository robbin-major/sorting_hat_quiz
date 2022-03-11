import random
house = ["Gryffindor!", "Hufflepuff!", "Ravenclaw!", "Slytherin!"]
pets = ["owl,", "cat,", "toad,", "mini dragon,", "lizard,"]
score = 0
playGame = False

q1 = "Would you play Quidditch at Hogwarts?"
q2 = "Would you excel in Defense Against the Dark Arts?"
q3 = "Are you Any good at playing Wizards Chess?"
q4 = "You catch a classmate cheating. Do you tell on them?"
q5 = "Would you want to have the Elder Wand?"
q6 = "Would you ever participate in a duel?"
q7 = "Do you prefer the books over the movies?"
q8 = "Would you ever work at the Ministry of Magic?"

questions = {q1: "yes", q2: "yes", q3: "yes",
             q4: "yes", q5: "yes", q6: "yes", q7: "yes", q8: "yes"}

sorting_hat = "HMMMMM, difficult... very difficult.."

user = input("""Welcome to the Wonderful Wizarding World of Harry Potter Sorting Hat!
 Would You like to be Sorted into your house? (yes/no): """).lower()

if user == "yes":
    playGame = True
else:
    print("OH! You are indeed, in fact, a muggle! Even if you agreed, you're not qualified to play! Good day!")
    playGame = False

if playGame:
    for i in questions:
        print(i)
        choice = input("Enter yes or no: ").lower()
        if choice == questions[i]:
            score = score + 3
        else:
            score = score - 1

    while True:
        if score >= 11 and score <= 13:
            print(sorting_hat, "I know what to do with you...",
                  house[0], "You and your", random.choice(pets), "report to your common room immediatly!")
            break
        elif score <= 10:
            print(sorting_hat, "You'll fit right in with...", house[1], "You and your", random.choice(
                pets), "report to your common room immediatly!")
            break
        elif score >= 14 and score <= 17:
            print(sorting_hat, "Books and cleverness...", house[2], "You and your", random.choice(
                pets), "report to your common room immediatly!")
            break
        elif score >= 17:
            print(sorting_hat, house[3], "You and your", random.choice(
                pets),  "report to your common room immediatly!")
            break
    print("Your score is: ", score)
