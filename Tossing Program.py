import random, sys
def coinflip():
    x = random.randint(0,1)
    if x == 0:
        print("\n.\n.\n.\n.Heads!\n.\n.\n.\n.")
    elif x == 1:
        print("\n.\n.\n.\n.Tails!\n.\n.\n.\n.")

while True:
    print('Welcome to Tossing Query.')
    y = input("Do you want to toss? y/n>")
    if y == 'n':
        sys.exit()
    elif y == 'y':
        coinflip()
    else:
        print("Please Enter 'y' for yes and 'n' for no!")

