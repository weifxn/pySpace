import os
import random

def char(array,ship,x,y):

    array[y][x] = ship # hero
    array[0][x] = 'x'

    return array

def npc(array,l1,l2,npc):

    for i in range(npc):
        for x in range(npc):
            array[l1[x]][l2[x]] = '*'

    return array


def createArray(h,l):
        array = [[' ' for k in range(h)]for j in range(l)]

        #print(array)
        return array

def showGrid(a,h,l):
    s = ['' for k in range(h)]

    for i in range(l):
        s[i] = ''.join(a[i])
        print(s[i])

def moveUD(x,v,a,move,height,ship,g):
    if move == 'w' or move == 'q' or move == 'e':
        if v - 1 < 0:
            k = v
        else:

            a[v][x] = g
            a[v-1][x] = ship
            k = v-1
    elif move == 's':
        if v + 2 > height:
            k = v
        else:
            a[v][x] = g
            a[v + 1][x] = ship
            k = v + 1
    return k

def moveLR(x,v,a,move,length,ship,g):
    if move == 'a' or move == 'q':
        if x - 2 < 0:
            k = x
        else:
            a[v][x] = g
            a[v][x-2] = ship
            k = x-2
    elif move == 'd' or move == 'e':
        if x + 2 > length:
            k = x
        else:
            a[v][x] = g
            a[v][x+2] = ship
            k = x+2

    return k

def checkGrid(l1,l2,v,z,score,npc,len,fuel):
    for i in range(npc):
        if l1[i] == v and l2[i] == z:
            score+= 10
            randHelp = random.sample(range(1, 101), 1)
            os.system('cls' if os.name == 'nt' else 'clear')
            if randHelp[0] > 95: #2%
                help = input('\n\n\n\n\n You found a broken ship with survivors.\n Help the survivors? (y/n) : ')
                if help == 'y':
                    if randHelp[0] > 98: #2%
                        nth = input('\n\n\n\n\n The survivors gifted you 100 fuel and 50 gold!')
                        fuel+= 100
                        score += 50

                    elif randHelp[0] > 94: #2%
                        nth = input('\n\n\n\n\n It\'s a trap! You have lost 50 fuel and 25 gold!')
                        fuel -= 50
                        score -= 25


            elif randHelp[0] > 93:
                nth = input('\n\n\n\n\n You found a chest with 100 gold!')
                score += 100
    return score

def checkFuel(fuel,xaxis,yaxis,move,halfLength,stage,tut):
    if xaxis == halfLength and yaxis == 0:
        move = 'x'

    elif move == 'z':
        return move
    elif fuel > 1:
        if tut == 0:
            jump = ''
        else:
            jump = tut
        print(' Move', end='')
        move = input(': ')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

        print('\n\n\n\n\n\n Out of fuel\n\n You wander in deep space of stage',stage,
                       '\n\n\n\n\n\n c - try again\n z - quit ')
        choice = input(' Select: ')
        move = choice
    return move

def buyFuel(fuel,score,x):
    if x == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(' Fuel:', fuel, '\n Gold:', int(score), )
        print('\n\n 2 fuel per gold.\n\n Max fuel:', int(score*2))
        addFuel = int(input('\n\n Fuel amount\n (0 to return): '))
        if addFuel == '':
            fuel = fuel
        else:
            max = score-(addFuel/2)
            if max < 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(' Not enough gold')
            else:
                fuel += addFuel


    return fuel


def tutorial(tut,stage,l):
    if stage == 0 and tut == 0:
        print()
        print(' You can use WASD to control the ship.')
        print(' Type \'ww\' to move forward twice.')

    elif stage == 0 and tut == 1:
        print()
        print(' Each STEP costs 1 fuel, each MOVE costs 5 fuel.')
        print(' You have moved',len(l),'steps. Thus it costs', len(l) + 5, 'fuel.')
        print(' Now, try to get to the nearest * using only 1 move.')

    elif stage == 0 and tut == 2:
        print()
        print(' Gold are used to buy fuel and upgrades.')
        print(' Now, try your best to reach the exit X')
        print(' without using too many moves.')

    elif stage == 0 and tut == 3:
        print()
        print(' You can ignore * to reserve some fuel.')
        print(' The galaxy will expand after every stage.')
        print(' Always make sure you have enough fuel!')

    elif stage == 0 and tut == 3:
        print(' Good luck!')
