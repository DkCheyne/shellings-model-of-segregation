import random
import time
import sys
import numpy
import pygame

# Setting the seed for random from OS time
random.seed()

# Set display size 
gameDisplay=pygame.display.set_mode((800, 800))

# Defining some colors 
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
cyan = (0,255,255)
yellow = (255,255,0)

# Creating list for the entire thing
fullList = []
neighborList = []
Neighbor = [] 

global i

# Defining loop
for i in range(64):
     
     # Individual list for each block's neighbor list
     neighborList.append([i])
     # Creating the value for the "Neighbor" at each position
     listNow = [i, numpy.random.random_integers(1,6)]

     if listNow[1] == 1 or listNow[1] == 2:
          listNow[1] = green

     elif listNow[1] == 3 or listNow[1] == 4:
          listNow[1] = yellow

     elif listNow[1] == 5 or listNow[1] == 6:
          listNow[1] = cyan 
     else: 
         print("WTF")

     # Making a list of list so we can access the "Neighbor"
     fullList.append(listNow)



# Checking the exit conditions
def exitCheck():

    # Checking to see if exit was pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


# Defining the drawing definition
def drawLines():
    for i in range(64): 
        if i <= 7:
            pygame.draw.rect(gameDisplay, black,(80 + i*80, 80, 80, 80),5)
            pygame.draw.rect(gameDisplay, white,(80 + i*80, 80, 80, 80),1)
        if i >= 8 and i < 16:
            pygame.draw.rect(gameDisplay, black,(i*80-560, 160, 80, 80),5)
            pygame.draw.rect(gameDisplay, white,(i*80-560, 160, 80, 80),1)
        if i >= 16 and i < 24:
            pygame.draw.rect(gameDisplay, black,(i*80-1200, 240, 80, 80),5)
            pygame.draw.rect(gameDisplay, white,(i*80-1200, 240, 80, 80),1)
        if i >= 24 and i < 32:
            pygame.draw.rect(gameDisplay, black,(i*80-1840, 320, 80, 80),5)
            pygame.draw.rect(gameDisplay, white,(i*80-1840, 320, 80, 80),1)
        if i >= 32 and i < 40:
            pygame.draw.rect(gameDisplay, black,(i*80-2480, 400, 80, 80),5)
            pygame.draw.rect(gameDisplay, white,(i*80-2480, 400, 80, 80),1)
        if i >= 40 and i < 48:
            pygame.draw.rect(gameDisplay, black,(i*80-3120, 480, 80, 80),5)
            pygame.draw.rect(gameDisplay, white,(i*80-3120, 480, 80, 80),1)
        if i >= 48 and i < 56:
            pygame.draw.rect(gameDisplay, black,(i*80-3760, 560, 80, 80),5)
            pygame.draw.rect(gameDisplay, white,(i*80-3760, 560, 80, 80),1)
        if i >= 56 and i < 64:
            pygame.draw.rect(gameDisplay, black,(i*80-4400, 640, 80, 80),5)
            pygame.draw.rect(gameDisplay, white,(i*80-4400, 640, 80, 80),1)

# Drawing the colored box's the first time.
def drawFirst():
    for i in range(64): 
        if i <= 7:
            pygame.draw.rect(gameDisplay, fullList[i][1],(80 + i*80, 80, 80, 80),0)
        if i >= 8 and i < 16:
            pygame.draw.rect(gameDisplay, fullList[i][1],(i*80-560, 160, 80, 80),0)
        if i >= 16 and i < 24:
            pygame.draw.rect(gameDisplay, fullList[i][1],(i*80-1200, 240, 80, 80),0)
        if i >= 24 and i < 32:
            pygame.draw.rect(gameDisplay, fullList[i][1],(i*80-1840, 320, 80, 80),0)
        if i >= 32 and i < 40:
            pygame.draw.rect(gameDisplay, fullList[i][1],(i*80-2480, 400, 80, 80),0)
        if i >= 40 and i < 48:
            pygame.draw.rect(gameDisplay, fullList[i][1],(i*80-3120, 480, 80, 80),0) 
        if i >= 48 and i < 56:
            pygame.draw.rect(gameDisplay, fullList[i][1],(i*80-3760, 560, 80, 80),0) 
        if i >= 56 and i < 64:
            pygame.draw.rect(gameDisplay, fullList[i][1],(i*80-4400, 640, 80, 80),0)


# Making sure .appened don't get out of hand 
whatLoopAmINow = -1
#print(neighborList)
# Logic Def 
def logic():
    time.sleep(.01)
    global whatLoopAmINow
    print(whatLoopAmINow)

    
         
    # Counting variable for number of neighbors 
    neighbor = 0
    whatLoopAmINow = whatLoopAmINow + 1
    # Looking forward one
    if i != 7 and i != 15 and i != 23 and i != 31 and i != 39 and i != 47 and i != 55 and i != 63:
       if fullList[i][1] == fullList[i + 1][1]:
           neighbor = neighbor + 1 
       if i > 8: 
            if fullList[i][1] == fullList [i - 7][1]:
                 neighbor = neighbor + 1    
       if i < 55:
            if fullList[i][1] == fullList [i + 9][1]:
                 neighbor = neighbor + 1 

    # Looking back one
    if i != 0 and i != 8 and i != 16 and i != 24 and i != 32 and i != 40 and i != 48 and i != 56:
        if fullList[i][1] == fullList [i - 1][1]:
            neighbor = neighbor + 1
        if i > 8: 
            if fullList[i][1] == fullList [i - 9][1]:
                 neighbor = neighbor + 1
        if i < 55:
            if fullList[i][1] == fullList [i + 7][1]:
                 neighbor = neighbor + 1
    # Looking up 
    if i > 8:
        if fullList[i][1] == fullList [i - 8][1]:
                 neighbor = neighbor + 1
    # Looking down 
    if i < 55:
        if fullList[i][1] == fullList [i + 8][1]:
                 neighbor = neighbor + 1
    #Neighbor.append([neighbor])
    if whatLoopAmINow < 64:
        neighborList[i].append(neighbor)
    elif whatLoopAmINow >= 64:
        del neighborList[i][1]
           #print(neighborList)
            #try:
             #   del neighborList[i][1]
            #except: 
                #neighborList[i].append(neighbor)
            #else:
        neighborList[i].append(neighbor)
        print(neighborList)
        #if k == 1:
        #    print(neighborList[i][1])   

            
        #print(neighbor)
         #   time.sleep(.01)
   
    if not True == True: 
        # Picking what "neighbor" is going to move
        i = numpy.random.random_integers(0,63)
        tempCount = 0
        # Getting the neighbor count in a way that we can add too
        tempCount = neighborList[i][1]
        #print(i)
        #print(neighborList)
        # Just Declaring that we have to assume there is a possible move unless proved otherwise
        possibleSpot = True 
           
    
        # Evaluating the first special case the first corner
        if i == 0:
  
            if fullList[i + 1][1] != cyan and fullList[i + 8][1] != cyan and fullList[i + 9][1] != cyan or fullList[i][1] == cyan:
                possibleSpot = False

            # Checking for empty spots (cyan) and switching places 
            while possibleSpot == True:
                whatSpot = random.randint(0,2)
                if whatSpot == 0 and fullList[i + 1][1] == cyan: 
                    fullList[i + 1][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan
                    possibleSpot = False 
                if whatSpot == 1 and fullList[i + 8][1] == cyan:
                    fullList[i + 8][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan 
                    possibleSpot = False
                if whatSpot == 2 and fullList[i + 9][1] == cyan:
                    fullList[i + 9][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan 
                    possibleSpot = False
            neighborList[i][1] = tempCount
         #   print("loop 1")

        # The first middle row 
        if i > 0 and i < 7:
            if fullList[i-7][1] != cyan and fullList[i + 1][1] != cyan and fullList[i + 7][1] != cyan and fullList[i + 8][1] != cyan and fullList[i+9]  or fullList[i][1] == cyan:
                possibleSpot = False
 
            # Checking for empty spots (cyan) and switching places
            while possibleSpot == True: 
                whatSpot = random.randint(0, 4)
                if whatSpot == 0 and fullList[i - 1][1] == cyan: 
                    fullList[i - 1][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan
                    possibleSpot = False 
                if whatSpot == 1 and fullList[i + 1][1] == cyan:
                    fullList[i + 1][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan 
                    possibleSpot = False
                if whatSpot == 2 and fullList[i + 7][1] == cyan:
                    fullList[i + 7][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan 
                    possibleSpot = False     
                if whatSpot == 3 and fullList[i + 8][1] == cyan: 
                    fullList[i + 8][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan 
                    possibleSpot = False 
                if whatSpot == 4 and fullList[i + 9][1] == cyan:
                    fullList[i + 9][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan 
                    possibleSpot = False 
            neighborList[i][1] = tempCount
          #  print("loop 2")
        # The Last Spot in the first row
        if i == 7:

            if fullList[i - 1][1] != cyan and fullList[i + 7][1] != cyan and fullList[i + 8][1] != cyan or fullList[i][1] == cyan:
                possibleSpot = False

            # Checking for empty spots (cyan) and switching places 
            while possibleSpot == True:
                whatSpot = random.randint(0,2)
                if whatSpot == 0 and fullList[i - 1][1] == cyan: 
                    fullList[i - 1][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan
                    possibleSpot = False 
                if whatSpot == 1 and fullList[i + 7][1] == cyan:
                    fullList[i + 7][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan 
                    possibleSpot = False
                if whatSpot == 2 and fullList[i + 8][1] == cyan:
                    fullList[i + 8][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan 
                    possibleSpot = False 
            neighborList[i][1] = tempCount
           # print("loop 3")
        # The first spot in the middle rows 
        if i == 8 or i == 16 or i == 24 or i == 32 or i == 40 or i == 48:
            
            if fullList[i - 8][1] != cyan and fullList[i - 7][1] != cyan and fullList[i + 1][1] != cyan and fullList[i + 8] != cyan and fullList[i + 9] != cyan  or fullList[i][1] == cyan:
                possibleSpot = False    
 
            while possibleSpot == True:               
                whatSpot = random.randint(0,4)

                if whatSpot == 0 and fullList[i - 8][1] == cyan: 
                    fullList[i - 8][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan
                    possibleSpot = False 
                if whatSpot == 1 and fullList[i - 7][1] == cyan:
                    fullList[i - 7][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan 
                    possibleSpot = False
                if whatSpot == 2 and fullList[i + 1][1] == cyan:
                    fullList[i + 1][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan 
                    possibleSpot = False     
                if whatSpot == 3 and fullList[i + 8][1] == cyan: 
                    fullList[i + 8][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan 
                    possibleSpot = False 
                if whatSpot == 4 and fullList[i + 9][1] == cyan:
                    fullList[i + 9][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan 
                    possibleSpot = False 
            neighborList[i][1] = tempCount
            #    print("loop 4")
        # The last spot in the middle rows
        if i == 15 or i == 23 or i == 31 or i == 39 or i == 47 or i == 55:
        
            if fullList[i - 9][1] != cyan and fullList[i - 8][1] != cyan and fullList[i - 1][1] != cyan and fullList[i + 7][1] != cyan and fullList[i + 8][1] != cyan or fullList[i][1] == cyan:
                possibleSpot = False 
            
            while possibleSpot == True:
                whatSpot = random.randint(0,4)
                           
                if whatSpot == 0 and fullList[i - 9][1] == cyan: 
                    fullList[i - 9][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan
                    possibleSpot = False 
                if whatSpot == 1 and fullList[i - 8][1] == cyan:
                    fullList[i - 8][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan 
                    possibleSpot = False
                if whatSpot == 2 and fullList[i - 1][1] == cyan:
                    fullList[i - 1][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan 
                    possibleSpot = False     
                if whatSpot == 3 and fullList[i + 8][1] == cyan: 
                    fullList[i + 8][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan 
                    possibleSpot = False 
                if whatSpot == 4 and fullList[i + 7][1] == cyan:
                    fullList[i + 7][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan 
                    possibleSpot = False
                neighborList[i][1] = tempCount
                
        # The middle spots 
        if i > 8 and i < 15 or i > 16 and i < 23 or i > 24 and i < 31 or i > 32 and i < 39 or i > 40 and i < 47 or i > 48 and i < 55:
            
            if fullList[i - 9][1] != cyan and fullList[i - 8][1] != cyan and fullList[i - 7][1] != cyan and fullList[i - 1][1] != cyan and fullList[i + 1][1] != cyan and fullList[i + 7][1] != cyan and fullList[i + 8][1] != cyan and fullList[i + 9][1] or fullList[i][1] == cyan:
                possibleSpot = False     
   
            k = 0
            while possibleSpot == True:
                k = k + 1
                whatSpot = random.randint(0,7)
                if whatSpot == 0 and fullList[i - 9][1] == cyan: 
                    fullList[i - 9][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan
                    possibleSpot = False 
                if whatSpot == 1 and fullList[i - 8][1] == cyan:
                    fullList[i - 8][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan 
                    possibleSpot = False               
                if whatSpot == 2 and fullList[i - 7][1] == cyan:
                    fullList[i - 7][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan 
                    possibleSpot = False
                if whatSpot == 3 and fullList[i - 1][1] == cyan: 
                    fullList[i - 1][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan
                    possibleSpot = False
                if whatSpot == 4 and fullList[i + 1][1] == cyan:
                    fullList[i + 1][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan 
                    possibleSpot = False 
                if whatSpot == 5 and fullList[i + 7][1] == cyan:
                    fullList[i + 7][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan 
                    possibleSpot = False
                if whatSpot == 6 and fullList[i + 8][1] == cyan:
                    fullList[i + 8][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan 
                    possibleSpot = False 
                if whatSpot == 7 and fullList[i + 9][1] == cyan:
                    fullList[i + 9][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan 
                    possibleSpot = False
                neighborList[i][1] = tempCount
              #  if k < 25:
             #       print("loop 6")

        # The first spot in the last row
        if i == 55:
  
            if fullList[i + 1][1] != cyan and fullList[i - 8][1] != cyan and fullList[i - 7][1] != cyan or fullList[i][1] == cyan:
                possibleSpot = False

            # Checking for empty spots (cyan) and switching places 
            while possibleSpot == True:
                whatSpot = random.randint(0,2)
                if whatSpot == 0 and fullList[i + 1][1] == cyan: 
                    fullList[i + 1][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan
                    possibleSpot = False 
                if whatSpot == 1 and fullList[i - 8][1] == cyan:
                    fullList[i - 8][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan 
                    possibleSpot = False
                if whatSpot == 2 and fullList[i -7][1] == cyan:
                    fullList[i - 7][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan 
                    possibleSpot = False
            neighborList[i][1] = tempCount  
            #print("loop 7")
        # The last spot in the last row 
        if i == 63:
  
            if fullList[i - 1][1] != cyan and fullList[i - 8][1] != cyan and fullList[i - 9][1] != cyan or fullList[i][1] == cyan:
                possibleSpot = False

            # Checking for empty spots (cyan) and switching places 
            while possibleSpot == True:
                whatSpot = random.randint(0,2)
                if whatSpot == 0 and fullList[i - 1][1] == cyan: 
                    fullList[i - 1][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan
                    possibleSpot = False 
                if whatSpot == 1 and fullList[i - 8][1] == cyan:
                    fullList[i - 8][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan 
                    possibleSpot = False
                if whatSpot == 2 and fullList[i -7][1] == cyan:
                    fullList[i + 9][1] = fullList[i][1]
                    tempCount = tempCount + 1 
                    fullList[i][1] = cyan 
                    possibleSpot = False
            neighborList[i][1] = tempCount
            print(fullList[i][1])
        #    print("loop 8")
    
    
    
 
# Making sure Program is responsive 
#clock = pygame.time.Clock()
#time = clock.tick(5)



 
# Will equal true when all the neighbors are satisfied 
sortingDone = False 
#firstLoop = True
# the main drawing loop and logic loop
while sortingDone == False:
    
    
     
     
    #if firstLoop == True:
      #  drawFirst()
      #  logic()
       # drawLines()
    # Update the screen 
       # pygame.display.update()
       # 
       # firstLoop = False
        #sortingDone = True

    # Debug must get rid of 
    logic()
    drawFirst()
    drawLines()
    pygame.display.update()
    


    # Check to see if exit button was pressed
    exitCheck()

    # Slow down the refresh rate 
    #time.sleep(50)



