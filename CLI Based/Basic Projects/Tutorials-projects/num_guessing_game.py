import random

low = 1
high = 100
answer = random.randint(low,high)

guesses = 0

print("\n-------------- NUMBER GUESSING GAME --------------\n")
while(True):
    number = int(input(f"Enter a number between {low} and {high}: "))
    guesses+=1
    if number == answer:
        print(f"Correct! the answer was {answer}")
        print(f"You guessed the number in {guesses} guesses.")
        break
    else:
        if number >= 1 and number <= 100:
            if number > answer:
                print("Lower number please!")
                guesses+=1
            elif number < answer:
                print("Higher number please!")
                guesses+=1
        else:
            print(f"Out of range! Please select between {low} and {high}.")
            guesses+=1

print("Thanks for playing!")                    