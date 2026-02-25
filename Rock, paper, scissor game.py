#A short program: Rock, Paper and Scissor
#Book's version. I didn't know about this program very much. That,s why, my own version is lacking here.
import random, sys
print('ROCK, PAPER, SCISSOR')

#These variables keep track of the number of wins, losses and ties.
wins = 0
losses = 0
ties = 0
while True:
    print('%s Wins, %s Losses, %s Ties' % (wins,losses,ties))
    while True:
        print("Enter your move: (r)ock (p)aper (s)cissor or (q)uit")
        player_move = input('>')
        if player_move == 'q':
            sys.exit()
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break
        print("Type one of r, p, s, or q.")
    if player_move == 'r':
        print("Rock versus...")
    elif player_move == 'p':
        print("Paper versus...")
    elif player_move == 's':
        print("Scissors versus...")

    move_number = random.randint(1,3)
    if move_number == 1:
        computer_move = 'r'
        print('Rock')
    elif move_number == 2:
        computer_move = 'p'
        print("Paper")
    elif move_number == 3:
        computer_move = 's'
        print("Scissors")
    if player_move == computer_move:
        print("It's a tie!")
        ties = ties + 1
    elif player_move == 'r' and computer_move == 's':
        print('You Win!')
        wins = wins + 1
    elif player_move == 'r' and computer_move == 'p':
        print("Computer Wins!")
        losses = losses + 1
    elif player_move == 'p' and computer_move == 'r':
        print("You win!")
        wins = wins + 1
    elif player_move == 'p' and computer_move == 's':
        print("Computer Wins!")
        losses = losses + 1
    elif player_move == 's' and computer_move == 'r':
        print("Computer Wins!")
        losses = losses + 1
    elif player_move == 's' and computer_move == 'p':
        print("You Win!")
        wins = wins + 1


