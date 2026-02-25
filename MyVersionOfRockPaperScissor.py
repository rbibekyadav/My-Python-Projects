#Rock Paper Scissor (My version)
import random, sys, time
p=0
c=0
def game():
    global c
    global p
    user_choice = input("Enter your move: Rock, Paper or Scissor>(r/p/s) or 'q' to QUIT:>").lower()
    computer_number = random.randint(1,3)
    if user_choice=='q':
        user_mood = 'n'
        print("---THANKS FOR PLAYING---")
        time.sleep(1)
        sys.exit()

    elif user_choice == 'r':
        user_move = 'Rock'
    elif user_choice == 'p':
        user_move = 'Paper'

    elif user_choice == 's':
        user_move = 'Scissors'




        if computer_number == 1:
            computer_choice = "r"
        elif computer_number == 2:
            computer_choice = "p"
        elif computer_number == 3:
            computer_choice = "s"


        if computer_choice == "r":
            computers_move = "Rock"
        elif computer_choice == "p":
            computers_move = "Paper"
        elif computer_choice == "s":
            computers_move = "Scissors"







        print("YOU CHOSE: "+ user_move)
        print("COMPUTER CHOSE: "+ computers_move)


        if computer_choice == user_choice:
            print("---GAME DRAW---")
        elif computer_choice == 'r' and user_choice == 's':
            print("---COMPUTER WINS---")
            c =c+1
        elif computer_choice == 'r' and user_choice == 'p':
            print("---YOU WIN---")
            p = p+1
        elif computer_choice == 'p' and user_choice=='s':
            print("---YOU WIN---")
            p = p + 1
        elif computer_choice == 'p' and user_choice=='r':
            print("---COMPUTERPUTER WINS---")
            c = c + 1
        elif computer_choice== 's' and user_choice == 'r':
            print("---YOU WIN---")
            p = p + 1
        elif computer_choice == 's' and user_choice =='p':
            print("---COMPUTER WINS---")
            c = c + 1
    else:
            print("Please enter 'r' for Rock, 'p' for Paper and 's' for Scissors")
print("---WELCOME TO THE GAME---")
print("Do you want to play?>(y/n)")
global user_mood
user_mood = input(":>").lower()
play = True
while play:

    if user_mood == 'y':
        game()
        print(f"Scores: \n\tCOMPUTER'S SCORE> {c} \n\tYOUR SCORE> {p}")
    elif user_mood == 'n':
        print("---THANKS FOR PLAYING---")
        time.sleep(0.5)
        sys.exit()
    else:
        print("Please enter 'y' to play or 'n' to quit the game!!!")


