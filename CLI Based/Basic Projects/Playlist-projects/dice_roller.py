import random

dice_art = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),

    2: (
        "┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘",
    ),

    3: (
        "┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘",
    ),

    4: (
        "┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘",
    ),

    5: (
        "┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘",
    ),

    6: (
        "┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘", 
    )
}

dice = []
total = 0
num_of_dice = int(input("How many dice? "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))


#Prints dice vertically 
# for die in range(num_of_dice):
#     dice.append(random.randint(1,6))
#     for line in dice_art.get(dice[die]):
#         print(line)         

#Prints dice horizontally
for line in range(5):
    for die in dice:
        print(dice_art[die][line] , end = " ")    
    print()

# ========================= Problem & Solution =========================
# Problem:
# Printing all dice horizontally caused the output to become too wide
# when rolling many dice (e.g., more than 7).

# Solution:
# Print the dice in fixed-size rows by slicing the dice list into
# chunks of 7. Each chunk is printed horizontally before moving to
# the next row.
# ======================================================================

# max_per_row = 7

# for start in range(0, len(dice), max_per_row):
#     current_row = dice[start:start + max_per_row]

#     for line in range(5):
#         for die in current_row:
#             print(dice_art[die][line], end=" ")
#         print()

#     print()     
 
for die in dice:
    total += die  

print(f"Total: {total}")