import random
from termcolor import colored
print(colored(' Hello, Welcome to the Game ', 'blue', attrs=['reverse', 'blink']))
print()
print(colored(' You can choose one of the following options : ', 'green', attrs=['reverse', 'blink']))
print()
items = ["rock", "paper", "scissor"]
print(items)
items[0]="r"
items[1]="p"
items[2]="s"
print()
print('r=rock , p=paper , s=scissor')
print()
round=int(input("How many rounds do you want to play ? "))
user_score = 0
computer_score = 0

# شرایط شکست ، پیروزی و تساوی
for i in range(round):
    user = input("Please write your choice : ")
    computer = random.choice(items)

    if computer == "r" and user == "p":
        print(f"Compute_Choice: {computer}")
        print(colored(' User Wins ', 'green', attrs=['reverse', 'blink']))
        user_score += 1
        print(colored(f"UserScore: {user_score} and ComputerScore: {computer_score}", color="yellow"))

    elif computer == "r" and user == "s":
        print(f"Compute_Choice: {computer}")
        print(colored(' Computer Wins ', 'red', attrs=['reverse', 'blink']))
        computer_score += 1
        print(colored(f"UserScore: {user_score} and ComputerScore: {computer_score}", color="yellow"))

    elif computer == "p" and user == "r":
        print(f"Compute_Choice: {computer}")
        print(colored(' Computer Wins ', 'red', attrs=['reverse', 'blink']))
        computer_score += 1
        print(colored(f"UserScore: {user_score} and ComputerScore: {computer_score}", color="yellow"))

    elif computer == "p" and user == "s":
        print(f"Compute_Choice: {computer}")
        print(colored(' User Wins ', 'green', attrs=['reverse', 'blink']))
        user_score += 1
        print(colored(f"UserScore: {user_score} and ComputerScore: {computer_score}", color="yellow"))

    elif computer == "s" and user == "r":
        print(f"Compute_Choice: {computer}")
        print(colored(' User Wins ', 'green', attrs=['reverse', 'blink']))
        user_score += 1
        print(colored(f"UserScore: {user_score} and ComputerScore: {computer_score}", color="yellow"))

    elif computer == "s" and user == "p":
        print(f"Compute_Choice: {computer}")
        print(colored(' Computer Wins ', 'red', attrs=['reverse', 'blink']))
        computer_score += 1
        print(colored(f"UserScore: {user_score} and ComputerScore: {computer_score}", color="yellow"))

    elif computer == user:
        print(f"Compute_Choice: {computer}")
        print(colored(' Equal ', 'blue', attrs=['reverse', 'blink']))
        print(colored(f"UserScore: {user_score} and ComputerScore: {computer_score}", color="yellow"))