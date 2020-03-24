import random
import sys
print('Welcome to Stone Paper Scissors')
wins = 0
losses = 0
ties = 0
while True:
    print(str(wins)+ 'wins, ' +str(losses)+ 'losses, ' +str(ties)+ 'ties ')
    print('Enter your Move: (r)ock, (p)apers, (s)cissors, (q)quit ')
    #computer's move 
    comp_number = random.randint(1,3)
    if comp_number == 1:
        comp_choice = 'ROCK'
    elif comp_number == 2:
        comp_choice = 'PAPER'
    elif comp_number == 3:
        comp_choice = 'SCISSORS'
    #player's move
    player_choice = input()
    if player_choice == 'q':
            print('Ha! you a quitter')
            sys.exit() 
    elif player_choice == 'r':
        print ('ROCK versus')
        print (comp_choice)
    elif player_choice == 'p':
        print ('PAPERS versus')
        print (comp_choice)
    elif player_choice == 's':
        print ('SCISSORS versus')
        print (comp_choice)
    #deciding who wins/won
    if player_choice == 'r' and comp_number == 1:
        print('It is a tie')
        ties = ties + 1
    if player_choice == 'r' and comp_number == 2:
        print('You loose!')
        losses = losses + 1
    if player_choice == 'r' and comp_number == 3:
        print('You won')
        wins = wins + 1
    if player_choice == 'p' and comp_number == 1:
        print('You won')
        wins = wins + 1
    if player_choice == 'p' and comp_number == 2:
        print('It is a tie')
        ties = ties + 1
    if player_choice == 'p' and comp_number == 3:
        print('You loose!')
        losses = losses + 1
    if player_choice == 's' and comp_number == 1:
        print('You loose!')
        losses = losses + 1
    if player_choice == 's' and comp_number == 2:
        print('You won')
        wins = wins + 1
    if player_choice == 's' and comp_number == 3:
        print('It is a tie')
        ties = ties + 1