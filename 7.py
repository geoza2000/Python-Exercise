letters = ['A', 'B', 'C']
numbers = ['1', '2', '3']
User = True
counter = 0

n = 4
magicTable = [[0] * n for i in range(n)]
magicTable[0][0] = ' '
magicTable[0][1] = 1
magicTable[0][2] = 2
magicTable[0][3] = 3
magicTable[1][0] = 'A'
magicTable[2][0] = 'B'
magicTable[3][0] = 'C'

for x in range(1,4):
    for y in range(1,4):
        magicTable[x][y] = ' '

def printTable():
    for posx in range(4):
        for posy in range(4):
            print(magicTable[posx][posy]),
        print('\n')

def getCoords():
    global User
    global counter
    if User == True:
        coords = raw_input('Give the cordinates of the box u want to play (eg. A 3)')
    else:
        for posx in range(1,4):
            for posy in range(1,4):
                if magicTable[posx][posy] == ' ':
                    coords = letters[posx-1] + str(posy)


    for char in coords:
        for letter in letters:
            if char == letter:
                for num in coords:
                    for number in numbers:
                        if num == number:
                            if letter == 'A':
                                letter = 1
                            elif letter == 'B':
                                letter = 2
                            elif letter == 'C':
                                letter = 3
                            if magicTable[letter][int(number)] == ' ': 
                                if User:
                                    magicTable[letter][int(number)] = 'X'
                                else:
                                    magicTable[letter][int(number)] = 'O'
                                User = not User
                                counter = counter + 1
                            break

def checkGameStatus():
    global magicTable
    horx = 0
    verx = 0
    horo = 0
    vero = 0
    for posx in range(1,4):
        for posy in range(1,4):
            if magicTable[posx][posy] == 'X':
                horx = horx + 1
            elif magicTable[posx][posy] == 'O':
                horo = horo + 1
            if magicTable[posy][posx] == 'X':
                verx = verx + 1
            elif magicTable[posy][posx] == 'O':
                vero = vero + 1
        if horx == 3 or verx == 3:
            return 1
        elif horo == 3 or vero == 3:
            return 2
        horx = 0
        verx = 0
        horo = 0
        vero = 0
    
    posx = 0
    poso = 0
    for pos in range(1,4):
        if magicTable[pos][pos] == 'X':
            posx = posx + 1
        elif magicTable[pos][pos] == 'O':
            poso = poso + 1
    if posx == 3:
        return 1
    elif poso == 3:
        return 2

    posx = 0
    poso = 0
    for pos in range(1,4):
        if magicTable[pos][4-pos] == 'X':
            posx = posx + 1
        elif magicTable[pos][4-pos] == 'O':
            poso = poso + 1
    if posx == 3:
        return 1
    elif poso == 3:
        return 2
    
    

playerWon = False
while (not playerWon) and counter < 9 :
    printTable()
    getCoords()
    if checkGameStatus() == 1:
        print 'User won'
        counter = 10
    elif checkGameStatus() == 2:
        print 'AI won'
        counter = 10
printTable()
