#importing choice function from random module for computer moves
from random import choice

#function for getting the position with the help of input
def position(row, col, symbl, D): 
    if row.upper() == 'A':
        if col == '1' and D['TL'] == ' ':
            D['TL'] = symbl
        elif col == '2' and D['TM'] == ' ':
            D['TM'] = symbl
        elif col == '3' and D['TR'] == ' ':
            D['TR'] = symbl     
        else:
            if symbl == P_symbl:
                user = 'player'
            elif symbl == comp_symbl:
                user = 'comp'            
            wrong_input(user)           #calling function for wrong input defined below
    
    elif row.upper() == 'B':
        if col == '1' and D['ML'] == ' ':
            D['ML'] = symbl
        elif col == '2' and D['centre'] == ' ':
            D['centre'] = symbl
        elif col == '3' and D['MR'] == ' ':
            D['MR'] = symbl
        else:
            if symbl == P_symbl:
                user = 'player'
            elif symbl == comp_symbl:
                user = 'comp'
            wrong_input(user)           #calling function for wrong input defined below

    
    elif row.upper() == 'C':
    
        if col == '1' and D['BL'] == ' ':
            D['BL'] = symbl
        elif col == '2' and D['BM'] == ' ':
            D['BM'] = symbl
        elif col == '3' and D['BR'] == ' ':
            D['BR'] = symbl
            
        else:
            if symbl == P_symbl:
                user = 'player'
            elif symbl == comp_symbl:
                user = 'comp'
            wrong_input(user)           #calling function for wrong input defined below
    else:
        wrong_input('player')           #calling function for wrong input defined below

    return D

#function for taking the inputs from the user and using position function defined above
def player():
    print()    
    col = input('Enter the column number [1/2/3] : ')
    print()
    row = input('Enter the row name [A/B/C] : ')
    position(row, col, P_symbl, D)

#function for taking random choices and using it as computer's moves
def comp():
    comp_col = choice(['1','2','3'])
    comp_row = choice(['A','B','C'])
    position(comp_row, comp_col, comp_symbl, D)

#function for handling wrong values by the user or computer
def wrong_input(user):
    if user == 'comp':
        comp()
    elif user == 'player':
        print('\nYou entered a location which is already filled or does not \
exist. Please re-enter your values.')
        player()

#-----------------------------------------------------------------------

#message at the beginning of the game explaining rules and procedure
print('\nHello there! This is a Tic-Tac-Toe game. \
\n\nIn this game, you have to arrange your symbol (x / o) in a straight line. \
\n\nIt can be horizontal, vertical or diagonal. \
\n\nYou will get four chances to do so. \
\n\nThis is a single player game, that is, you are competing against the computer.\n')

#while loop for continuing the game till the user wants
run = True
while run == True:

    #Dictionary for all the nine positions on the game board
    D = {'TL':' ', 'TM':' ', 'TR': ' ', 'ML':' ', 'centre':' ', 'MR':' ',\
         'BL':' ', 'BM':' ', 'BR':' '}

    #print statements for organising the dictionary values is square format
    print('\n      1   2   3 ')
    print('A    %2s |%2s |%2s' % (D['TL'],D['TM'],D['TR']))
    print('      -   -   - ')
    print('B    %2s |%2s |%2s' % (D['ML'],D['centre'],D['MR']))
    print('      -   -   - ')
    print('C    %2s |%2s |%2s\n' % (D['BL'],D['BM'],D['BR']))

    #message for the user
    print('You can choose your location by entering your column (1/2/3) and row\
 (A/B/C). \nLet\'s Begin!!!!\n\n\n')

    #asking user for choosing the symbol
    accept = True
    while accept == True:
        P_symbl = input('Enter your symbol [x / o] : ')
        P_symbl = P_symbl.lower()
        if P_symbl in ['x', 'o']:
            accept= False
        else:
            print('\nYou entered wrong symbol. Please enter "x" or "o"\n')

    #declaring the computer symbol as opposite of user
    comp_symbl = 'x' if P_symbl == 'o' else 'o'

    #loop for running the game 4 times so that the player gets 4 chances
    for i in range(4):
        player()        #calling the player's function
        comp()          #calling the computer's function
        
        #print statements for organising the dictionary values is square format
        print('\n      1   2   3 ')
        print('A    %2s |%2s |%2s' % (D['TL'],D['TM'],D['TR']))
        print('      -   -   - ')
        print('B    %2s |%2s |%2s' % (D['ML'],D['centre'],D['MR']))
        print('      -   -   - ')
        print('C    %2s |%2s |%2s\n' % (D['BL'],D['BM'],D['BR']))

        #if-else statements for deciding the winner
        if D['TL'] == D['TM'] == D['TR'] == P_symbl or \
           D['ML'] == D['centre'] == D['MR'] == P_symbl or \
           D['BL'] == D['BM'] == D['BR'] == P_symbl or \
           D['TL'] == D['ML'] == D['BL'] == P_symbl or \
           D['TM'] == D['centre'] == D['BM'] == P_symbl or \
           D['TR'] == D['MR'] == D['BR'] == P_symbl or \
           D['TL'] == D['centre'] == D['BR'] == P_symbl or \
           D['TR'] == D['centre'] == D['BL'] == P_symbl :
            print('Congratulations! You won!\n\n')
            
            #input and if statement to ask to replay the game
            ask = input('Do you want to play again?? [Y/N] : ')
            if ask.upper() == 'N':
                print('Thank you for playing this game!')
                run = False
            break

        elif D['TL'] == D['TM'] == D['TR'] == comp_symbl or \
           D['ML'] == D['centre'] == D['MR'] == comp_symbl or \
           D['BL'] == D['BM'] == D['BR'] == comp_symbl or \
           D['TL'] == D['ML'] == D['BL'] == comp_symbl or \
           D['TM'] == D['centre'] == D['BM'] == comp_symbl or \
           D['TR'] == D['MR'] == D['BR'] == comp_symbl or \
           D['TL'] == D['centre'] == D['BR'] == comp_symbl or \
           D['TR'] == D['centre'] == D['BL'] == comp_symbl:
            print('Sorry! The computer won the game!\n\n')

            #input and if statement to ask to replay the game
            ask = input('Do you want to retry?? [Y/N] : ')
            if ask.upper() == 'N':
                print('Thank you for playing this game!')
                run = False
            break
               
    #for - else statement in case no one wins the game and no break is encountered
    else:
        print('OH! no one won the game!')
        ask = input('Do you want to retry?? [Y/N] : ')
        if ask.upper() == 'N':
            print('Thank you for playing this game!')
            run = False

















