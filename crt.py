import random
weapon = ["compost", "recycle", "trash"]

print("Welcome to Compost, Recycle, Trash")
print()
name = input("What is your name? ")

you = 0
computer = 0
play_again = True

while play_again == True:
    choice = input("Your choice: ")
    
    while choice != "compost" and choice != "recycle" and choice != "trash":
        choice = input("Your choice: ")
        
    pc_move = random.randint(0, 2)
    
    if choice == "compost":
        if pc_move == 0:
            print(f"Opponent's move: compost   Tie")
        elif pc_move == 1:
            print(f"Opponent's move: recycle   You win!")
            you += 1
        else:
            print(f"Opponent's move: trash   You lose..")
            computer += 1
    if choice == "recycle":
        if pc_move == 0:
            print(f"Opponent's move: compost   You lose..")
            computer += 1
        elif pc_move == 1:
            print(f"Opponent's move: recycle   Tie")
        else:
            print(f"Opponent's move: trash   You win!")
            you += 1
    if choice == "trash":
        if pc_move == 0:
            print(f"Opponent's move: compost   You win!")
            you += 1
        elif pc_move == 1:
            print(f"Opponent's move: recycle   You lose..")
            computer += 1
        else:
            print(f"Opponent's move: trash   Tie")
        
    print()
    print(f"{name}: {you}   Computer: {computer}")
    print()
    response = input("Would you like to play again? ")
    if response == "no":
        print()
        total_games = you + computer
        you_win_percent = (you / total_games) * 100
        pc_win_percent = (computer / total_games) * 100
        print(f"{name}'s winning percentage: {round(you_win_percent, 2)}%")
        print(f"Computer's winning percentage: {round(pc_win_percent, 2)}%")
        
        
        play_again = False