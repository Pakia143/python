import random
while True:
    my_answer = input("choose: rock, paper, scissor \n")
    my_answer = my_answer.lower()

    if my_answer != "rock" and my_answer != "paper" and my_answer != "scissor":
        print("Please choose a correct answer")
        continue

    computer_answer = random.choice(["rock", "paper", "scissor"])
    print(f"computer chose: {computer_answer}")

    if my_answer == computer_answer:
        print("You tied")
        continue
    elif my_answer == "rock" and computer_answer == "paper":
        print("You Lose") 
        continue
    elif my_answer == "paper" and computer_answer == "scissor":
        print("You Lose")
        continue
    elif my_answer == "scissor" and computer_answer == "rock":
        print("You Lose")
        continue
    else:
        print("You Won")
        break                   