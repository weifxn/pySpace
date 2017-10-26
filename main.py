'''

- Changelog -
11/10:
    - Added hop. (multiple input)
    - Increased to 8 directions

12/10:
    - added fuel
    - changed to gold

13/10:
    - added change ship
    - added exit
    - added q and e for extra direction
    - added stages
    - fixed exit from menu
    - do: add upgrades?
    - added upgrades
    - do: add tutorial, put inside txt file

26/10
    - added tutorials
    - removed skills
    - fix: horizontal length random
    - do: increase stars at higher stage



'''

import grid
import os
import random
import time
from time import strftime

rand2 = []
l = []
move = ''
exitGame = 2
ship = '^'
tmpf = 0
bonus = 0
fBonus = 0
guide = '.'
p= 0

while exitGame > 1:
    exit = 3
    score = 100
    fuel = 200
    orContinue = " 0. How to Play\n\n 1. Start "
    stage = 0

    while exit > 1:
        stage +=1
        gHeight = 14 + (stage)
        gLength = 14 + (stage)
        menu = 2
        os.system('cls' if os.name == 'nt' else 'clear')
        xaxis = 6
        if stage > 1:
            orContinue = " 1. Next Stage "
        npc = 7



        yaxis = gLength - 1
        halfLength = xaxis
        rand1 = random.sample(range(1, gHeight-1, 2), npc)
        rand2 = random.sample(range(0,14,2),7)
        repeat = 3
        array = grid.createArray(gHeight,gLength)
        array = grid.npc(array,rand1,rand2,npc)

        array = grid.char(array,ship,xaxis,yaxis)
        temp = fuel
        os.system('cls' if os.name == 'nt' else 'clear')
        while menu > 1:
            tut = 0
            print(' Fuel:', fuel, '\n Gold:', int(score), )
            x = input('\n\n\t[ Stage {Stage} ]\n\n\n{Start}\n\n 2. Buy fuel\n\n 3. Upgrades\n\n 4. Quit\n\n Select: '.format(Start = orContinue,Stage=stage))
            if x == '0':
                os.system('cls' if os.name == 'nt' else 'clear')
                stage -= 1
                menu = 1
            if x == '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('\n\n Upgrades:\n\n\n 1. Moves consume 10% less fuel [199 Gold]\n')
                bonus = int(input(' 2. Moves consume 20% less fuel\t[399 Gold] \n\n 3. Moves consume 40% less fuel\t[799 Gold]\n\n Select (0 to return): '))
                if bonus == 1:
                    if score > 198:
                        score -= 199
                        fBonus = 1
                    else:
                        bonus = 0
                elif bonus == 2:
                    if score > 398:
                        score -= 399
                        fBonus = 2
                    else:
                        bonus = 0
                elif bonus == 3:
                    if score > 798:
                        score -= 799
                        fBonus = 3
                    else:
                        bonus = 0
                else:
                    bonus = 0

                bonus = 0

            elif x=='1':
                menu = 1
            elif x == '4':
                menu = 1
                move = 'z'
            else:
                fuel = grid.buyFuel(fuel,score,x)
                value = fuel - temp
                score -= value / 2

            os.system('cls' if os.name == 'nt' else 'clear')

        while repeat > 2:

            
            print(' Fuel:',fuel)
            print(' Gold:',int(score))
            print()
            grid.showGrid(array,gHeight,gLength)
            millis = int(round(time.time()*1000))
            #print(millis)
            grid.tutorial(tut,stage,l)
            print()
            move = grid.checkFuel(fuel,xaxis,yaxis,move,halfLength,stage,tut)




            l = list(move)
            fuel -=5
            if fBonus == 1:
                tmpf = (tmpf**2) -1
                if tmpf == -1:
                    fuel+=1
            if fBonus == 2:
                fuel +=1

            if fBonus == 3:
                fuel +=2


            s = int(strftime("%S"))
            tempSec = s
            if len(l) > 0:
                tempPosition = l[len(l)-1]
                if tempPosition == 'w' or tempPosition == 'q' or tempPosition == 'e':
                    ship = '^'
                elif tempPosition == 'a':
                    ship = '<'
                elif tempPosition == 'd':
                    ship = '>'
                elif tempPosition == 's':
                    ship = 'v'
                else:
                    ship = '^'

            for i in range(len(l)):

                move = l[i]

                if move == 'w' or move =='s':
                    yaxis = grid.moveUD(xaxis,yaxis,array,move,gHeight,ship,guide)



                elif move == 'a' or move == 'd':
                    xaxis = grid.moveLR(xaxis,yaxis,array,move,gLength,ship,guide)

                elif move == 'q' or move == 'e':
                    xaxis = grid.moveLR(xaxis, yaxis, array, move, gLength, ship,guide)
                    yaxis = grid.moveUD(xaxis, yaxis, array, move, gHeight, ship,guide)

                elif move == 'z':# q
                    exitGame = 1
                    exit = 1
                    repeat = 2
                elif move == 'x':# f remember to remove this
                    repeat = 2
                elif move == 'c':# e
                    repeat = 2
                    exit = 1
                else:
                    tempList = int(l[i])
                    if tempList > 0:
                        tempStore = i
                        alpha = l[i - 1]
                        i = len(l)
                        for m in range(tempList):
                            l.insert(m + 1, alpha)
                tempScore = score
                score = grid.checkGrid(rand1, rand2, yaxis, xaxis, score, npc,len(l),fuel)
                fuel -= 1
            tut += 1

            




            os.system('cls' if os.name == 'nt' else 'clear')
        if stage == 0:
                    score = 100
                    fuel = 200




