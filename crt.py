import random
weapon = ["compost", "recycling", "trash"]
you = 0
computer = 0
play_again = True
while play_again == True:
    choice = input("Your choice: ")
    
    while choice != "compost" and choice != "recycling" and choice != "trash":
        choice = input("Your choice: ")
        
    pc_move = random.randint(0, 2)
    
    if choice == "compost":
        if pc_move == 0:
            print(f"Opponent's move: compost   Tie")
        elif pc_move == 1:
            print(f"Opponent's move: recycling   You win!")
            you += 1
        else:
            print(f"Opponent's move: trash   You lose..")
            computer += 1
    if choice == "recycling":
        if pc_move == 0:
            print(f"Opponent's move: compost   You lose..")
            computer += 1
        elif pc_move == 1:
            print(f"Opponent's move: recycling   Tie")
        else:
            print(f"Opponent's move: trash   You win!")
            you += 1
    if choice == "trash":
        if pc_move == 0:
            print(f"Opponent's move: compost   You win!")
            you += 1
        elif pc_move == 1:
            print(f"Opponent's move: recycling   You lose..")
            computer += 1
        else:
            print(f"Opponent's move: trash   Tie")
            
    print(f"You: {you}   Computer: {computer}")
    print()
    response = input("Would you like to play again? ")
    if response == "no":
        play_again = False