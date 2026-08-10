import random
import time

def spin_row():
    symbols = ['🍒' , '🌸' , '⭐' , '🍉' , '🦋' , '🕊️']

    return  [random.choice(symbols) for symbol in range(3)]

def print_row(row):
    print("-------------")
    print(" | ".join(row))
    print("-------------")

def get_payout(row , bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 8
        elif row[0] == '🌸':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 5
        elif row[0] == '🍉':
            return bet * 3
        elif row[0] == '🦋':
            return bet * 6
        elif row[0] == '🕊️':
            return bet * 7
        
    return 0 
        
def main(): 
    balance = 100 

    print("-----------------------")
    print("Welcome to Python Slots")
    print("Symbols:🍒🌸⭐🍉🦋🕊️")
    print("-----------------------")

    while balance > 0:
        print(f"\nCurrent balance: ${balance}")

        bet = input("Place you bet amount: " )

        if not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient balance!")
            continue

        if bet <= 0:
            print("Bet must be greater than zero.")
            continue

        balance -= bet
        row = spin_row()
        print("Spinning....\n")
        time.sleep(1)
        print_row(row)
        print()

        payout = get_payout(row , bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry, you lost this round.")

        balance += payout

        play_again = input("Do you want to spin again? (y/n): ").lower()

        if play_again != "y":
            break


    print("\n------------------------------------------")
    print(f"Game over! your final balance is ${balance}")
    print("--------------------------------------------")




if __name__ == "__main__":
    main() 