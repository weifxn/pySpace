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
    - added autosave (at menu)
    - added save and load page
    - added delete save (number 4)
    - do: easygui



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
save = ['','','']
stat = ['','','']





while exitGame > 1:
    os.system('cls' if os.name == 'nt' else 'clear')
    userSel = input(' 1. New game \n 2. Load game\n 3. Quit game\n : ')
    exit = 3
    score = 100
    fuel = 200
    orContinue = " 0. How to Play\n\n 1. Start "
    stage = 0
    if userSel == '3':
        exit = 1
        exitGame = 1
        os.system('cls' if os.name == 'nt' else 'clear')
    elif userSel == '2' or userSel == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        leaveSave = 2
        while leaveSave > 1:
            file = open('save.txt','r+')
            for snum in range(3):
                save[snum] = file.readline() # load save names

            for jump in range(3):
                stat[jump] = file.readline() # load save datas
            leaveSave = 1
            saveNum = int(input(' [Saves] \n\n Choose an empty save to start a new game: \n 1. {save1}\n 2. {save2}\n 3. {save3}\n (type 4 to delete save): '.format(save1=save[0],save2=save[1],save3=save[2])))
            if saveNum > 3: # user choose to delete saves
                delSave = int(input(' Select a save to delete: '))
                file.seek(0)
                file.truncate()

                for userNum in range(3):
                    if userNum == (delSave-1):
                        file.write('Empty\n')
                    else:
                        file.write(save[userNum])

                for statsNum in range(3):
                    if statsNum == (delSave-1):
                        file.write('200 100 0\n')
                    else:
                        file.write(stat[statsNum])
                file.close()
                os.system('cls' if os.name == 'nt' else 'clear')
                leaveSave = 2
            
            elif save[saveNum-1] == 'Empty\n': 
                username = input(' Enter name: ')
                username += '\n'
                file.seek(0)
                file.truncate()
                for userNum in range(3):
                    if userNum == (saveNum-1):
                        file.write(username)
                    else:
                        file.write(save[userNum])

                for statsNum in range(3):
                    file.write(stat[statsNum])
               


            else:
                #fuel gold stage

                

                statList = stat[saveNum-1].split(' ')
                fuel = int(statList[0])
                score = int(statList[1])
                stage = int(statList[2])
                stage -= 1


    file.close()

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
            print('\n\n',end=' ')
            x = input(' [ Stage {Stage} ]\n\n\n{Start}\n\n 2. Buy fuel\n\n 3. Upgrades\n\n 4. Quit\n\n Select: '.format(Start = orContinue,Stage=stage))
            if x == '0':
                os.system('cls' if os.name == 'nt' else 'clear')
                stage -= 1
                menu = 1
            if x == '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('\n\n Upgrades:\n\n\n 1. 10% less fuel\n [199 Gold]\n')
                bonus = int(input(' 2. 20% less fuel\n [399 Gold] \n\n 3. 40% less fuel\n [799 Gold]\n\n Select number\n (0 to return): '))
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
            elif x == '5':
                menu = 1
            else:
                fuel = grid.buyFuel(fuel,score,x)
                value = fuel - temp
                score -= value / 2

            file = open('save.txt','r+')
            for snum in range(3):
                save[snum] = file.readline()

            for jump in range(3):
                stat[jump] = file.readline()

            file.seek(0)
            file.truncate()

            for userNum in range(3):
                file.write(save[userNum])

            for statsNum in range(3):
                if statsNum == (saveNum-1):
                    stats = "{f} {s} {sg}\n".format(f=fuel,s=int(score),sg=stage)
                    file.write(stats)
                else:
                    file.write(stat[statsNum])
                print()
            file.close()





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




