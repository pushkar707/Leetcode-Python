print('\nEnter any Number from 1 to 9 to take make your move as shown below\n')
print('''1|2|3\n4|5|6\n7|8|9\n''')
a = '_'   
b = '_'   
c = '_'   
d = '_'   
e = '_'   
f = '_'   
g = ' '   
h = ' '   
i = ' '

count = 1

def gameboard():       
    print(f'\n{a}|{b}|{c}\n{d}|{e}|{f}\n{g}|{h}|{i}')
    
def playerInput():

    def playerTurn():
        if(count %2 == 0):
            return 'X'
        else:
            return 'Y'

    num = input('\nEnter a number to make your move: ')

    global a   
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    global count

    if(num == '1' and a == "_"):        
        a = playerTurn()
        gameboard()
        count += 1
    elif(num == '2' and b == "_"):        
        b = playerTurn()
        gameboard()
        count += 1
    elif(num == '3' and c == "_"):        
        c = playerTurn()
        gameboard()
        count += 1
    elif(num == '4' and d == "_"):        
        d = playerTurn()
        gameboard()
        count += 1
    elif(num == '5' and e == "_"):        
        e = playerTurn()
        gameboard()
        count += 1
    elif(num == '6' and f == "_"):        
        f = playerTurn()
        gameboard()
        count += 1
    elif(num == '7' and g == " "):        
        g = playerTurn()
        gameboard()
        count += 1
    elif(num == '8' and h == " "):        
        h = playerTurn()
        gameboard()
        count += 1
    elif(num == '9' and i == " "):        
        i = playerTurn()
        gameboard()
        count += 1
    else:
        print('Please Enter a valid input.')

def gameWin():
    if(a == 'X' and b == 'X' and c == 'X' ):
        print('Game Over. X wins')
        exit()
    elif(a == 'X' and e == 'X' and i == 'X' ):
        print('Game Over. X wins')
        exit()
    elif(a == 'X' and d == 'X' and g == 'X' ):
        print('Game Over. X wins')
        exit()
    elif(b == 'X' and e == 'X' and h == 'X' ):
        print('Game Over. X wins')
        exit()
    elif(c == 'X' and f == 'X' and i == 'X' ):
        print('Game Over. X wins')
        exit()
    elif(d == 'X' and e == 'X' and f == 'X' ):
        print('Game Over. X wins')
        exit()
    elif(g == 'X' and h == 'X' and i == 'X' ):
        print('Game Over. X wins')
        exit()
    elif(a == 'Y' and e == 'Y' and i == 'Y' ):
        print('Game Over. Y wins')
        exit()
    elif(a == 'Y' and d == 'Y' and g == 'Y' ):
        print('Game Over. Y wins')
        exit()
    elif(b == 'Y' and e == 'Y' and h == 'Y' ):
        print('Game Over. Y wins')
        exit()
    elif(c == 'Y' and f == 'Y' and i == 'Y' ):
        print('Game Over. Y wins')
        exit()
    elif(d == 'Y' and e == 'Y' and f == 'Y' ):
        print('Game Over. Y wins')
        exit()
    elif(g == 'Y' and h == 'Y' and i == 'Y' ):
        print('Game Over. Y wins')
        exit()
    elif(a == 'Y' and b == 'Y' and c == 'Y' ):
        print('Game Over. Y wins')
        exit()
    else:
        pass
    
gameboard()
while(True):
    playerInput()
    gameWin()