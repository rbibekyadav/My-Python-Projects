#A program to create a ludo Dice.
import sys, random, time
def dice():
    n=0
    vary = True
    while vary:
        x = random.randint(1,6)
        if x == 1:
            print("""
             _______
            |       |
            |       |
            |   *   |
            |       |
            |_______|
                     """)
            vary = False
        elif x == 2:
            print("""
             _______
            |       |
            |       |
            | *   * |
            |       |
            |_______|
            """)
            vary = False
        elif x == 3:
            print("""
             _______
            |       |
            | *   * |
            |       |
            |   *   |
            |_______|
            """)
            vary = False
        elif x == 4:
            print("""
             _______
            |       |
            | *   * |
            |       |
            | *   * |
            |_______|
            """)
            vary = False
        elif x == 5:
            print("""
             _______
            |       |
            | *   * |
            |   *   |
            | *   * |
            |_______|
            """)
            vary = False
        elif x == 6:
            print("""
             _______
            |       |
            | *   * |
            | *   * |
            | *   * |
            |_______|
            """)
            n = n+1
            if n == 3:
                print("None of the Sixes count. You lost your chance. Pass the dice to other player.")
                vary = False
            else:
                vary = True

print("---LUDO DICE---")
print("---Do you want to roll?---y/n")
while True:
    player = input(">")
    if player == "y":
        dice()
    elif player == "n":
        print("___Have a nice day!!!___")
        time.sleep(1)
        sys.exit()
    else:
        print("Please enter 'y' for yes and 'n' to Quit.")


