import random

choices = [
    "rock", "paper", "scizors"    
]

player_choice = int(input("Choose Your Destiny (0, 1, 2): \n"))
comptr_choice = random.randint(0, 2)

if (player_choice > 2 or player_choice < 0):
    print("Wrong number input, you lose.")
else:

    print(f"your choice: {choices[player_choice]} - \"{player_choice}\"")
    print(f"computer choice: {choices[comptr_choice]} - \"{comptr_choice}\"")

    if (player_choice == comptr_choice):
        print("draw")
    elif(player_choice == 0 and comptr_choice == 2):
        print("you win!")
    elif(comptr_choice == 0 and player_choice == 2):
        print("you lose!")
    elif(player_choice > comptr_choice):
        print("you win!")
    elif(comptr_choice > player_choice):
        print("you lose!")