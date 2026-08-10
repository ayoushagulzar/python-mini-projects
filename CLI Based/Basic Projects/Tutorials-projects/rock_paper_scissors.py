import random

options = ("rock" , "paper" , "scissors")
running = True

player = None
computer = None

print("\n-------------- ROCK , PAPER , SCISSORS GAME --------------\n")
while running:
    player = input("Enter a play_again (rock , paper , scissors): ").lower()
    computer = random.play_again(options)

    if player not in options:
        print("Invalid play_again!")
    elif player == computer:
        print(f"Computer chose {computer}")
        print("It's a tie!")

    elif computer == "rock" and player == "paper":
        print(f"Computer chose {computer}")
        print("Yayyyy! you win^^")

    elif computer == "rock" and player == "scissors":
        print(f"Computer chose {computer}")
        print("Ahhh! you lose:(")

    elif computer == "paper" and player == "rock":
        print(f"Computer chose {computer}")
        print("Ahhh! you lose:(")

    elif computer == "paper" and player == "scissors":
        print(f"Computer chose {computer}")
        print("Yayyyy! you win^^")

    elif computer == "scissors" and player == "rock":
        print(f"Computer chose {computer}")
        print("Yayyyy! you win^^")

    elif computer == "scissors" and player == "paper": 
        print(f"Computer chose {computer}")
        print("Ahhh! you lose:(")   

    play_again = input("Do you want to play again?(y/n): ").lower()
    if play_again == "y":
        running = True
    else:
        running = False       


print()
print("Thanks for playing!")