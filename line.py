import random

titlescreen = input("PRISON LINE\nKevin Roadarmel\n\nEnter to start: ")
askRules = input("\nRoll digital dice, land on special tiles, chase down prisoners, or run from cops, down to the end of the\nLINE!\n\nThe object of the game is to get down to 0 steps and escape the prison. There are 20 steps in total, good luck!\n\nEnter to continue: ")

diceNum = 0
run = True
global onePiece
global twoPiece
global lastMoved


class B1:
    name = "B1"
    pos = 20
    color = "Blue"
    role = ""
class B2:
    name = "B2"
    pos = 20
    color = "Blue"
    role = ""


class G1:
    name = "G1"
    pos = 20
    color = "Green"
    role = ""
class G2:
    name = "G2"
    pos = 20
    color = "Green"
    role = ""
    
    
class R1:
    name = "R1"
    pos = 20
    color = "Red"
    role = ""
class R2:
    name = "R2"
    pos = 20
    color = "Red"
    role = ""

def roll():
    global diceNum
    dice = random.randrange(1,15)
    diceNum = dice
    
    
    
    
def checkWin():
    if B1.pos <= 0 and B2.pos<=0:
        print("\n" + B1.color + " has won the game of PRISON LINE!")
        run = False
    if G1.pos <= 0 and G2.pos<=0:
        print("\n" + G1.color + " has won the game of PRISON LINE!")
        run = False
    if R1.pos <= 0 and R2.pos<=0:
        print("\n" + R1.color + " has won the game of PRISON LINE!")
        run = False
    
    
    
    
    
def characterChoice():
    global lastMoved
    charChoice = input("\n" + onePiece.color + " has rolled a " + str(diceNum) + "\nWould you like to move " + onePiece.name + " (Step: " + str(onePiece.pos) + ") or " + twoPiece.name + " (Step: " + str(twoPiece.pos) + ")\n")
    if charChoice.upper() == onePiece.name or charChoice == "1":
        if onePiece.pos <=0:
            print("\n"+onePiece.name + " is at the finish line! Cannot be moved.")
            onePiece.pos = 0
            characterChoice()
        
        else:
            onePiece.pos = onePiece.pos - diceNum
            if onePiece.pos < 0:
                onePiece.pos = 0
            print("\n" + onePiece.name + " is now on step " + str(onePiece.pos))
            lastMoved = onePiece
    elif charChoice.upper() == twoPiece.name or charChoice == "2":
        if twoPiece.pos <=0:
            print("\n"+twoPiece.name + " is at the finish line! Cannot be moved.")
            characterChoice()
        else:
            twoPiece.pos = twoPiece.pos - diceNum
            if twoPiece.pos < 0:
                twoPiece.pos = 0
            print("\n" + twoPiece.name + " is now on step " + str(twoPiece.pos))
            lastMoved = twoPiece
    else:
        print("Please type in either " + onePiece.name + " or " + twoPiece.name + "!")
        characterChoice()
        
        
        
        
        
        
        
def checkTile():
    global lastMoved
    compUser = B1
    if lastMoved.role == "Cop" and lastMoved.pos == compUser.pos and lastMoved.color != compUser.color:
        print("\n" + lastMoved.color + " has put " + compUser.name + " back to prison!")
        compUser.pos = 20
    
    compUser = B2
    if lastMoved.role == "Cop" and lastMoved.pos == compUser.pos and lastMoved.color != compUser.color:
        print("\n" + lastMoved.color + " has put " + compUser.name + " back to prison!")
        compUser.pos = 20
    
    compUser = G1
    if lastMoved.role == "Cop" and lastMoved.pos == compUser.pos and lastMoved.color != compUser.color:
        print("\n" + lastMoved.color + " has put " + compUser.name + " back to prison!")
        compUser.pos = 20
    
    compUser = G2
    if lastMoved.role == "Cop" and lastMoved.pos == compUser.pos and lastMoved.color != compUser.color:
        print("\n" + lastMoved.color + " has put " + compUser.name + " back to prison!")
        compUser.pos = 20
    
    compUser = R1
    if lastMoved.role == "Cop" and lastMoved.pos == compUser.pos and lastMoved.color != compUser.color:
        print("\n" + lastMoved.color + " has put " + compUser.name + " back to prison!")
        compUser.pos = 20
    
    compUser = R2
    if lastMoved.role == "Cop" and lastMoved.pos == compUser.pos and lastMoved.color != compUser.color:
        print("\n" + lastMoved.color + " has put " + compUser.name + " back to prison!")
        compUser.pos = 20







def specialTile():
    global lastMoved
    # Divisible by 3
    if (lastMoved.pos%3) == 0 and lastMoved.pos != 0:
        print("\n" + lastMoved.name + " has landed on a prison tile! They have been moved back to prison")
        lastMoved.pos = 20
    if lastMoved.pos%7 == 0:
        print("\n" + lastMoved.name + " gets to go again!")
        roll()
        characterChoice()
        checkTile()
        specialTile()
        
    
        
        
        
        
        
# Beginning of game, role selection
threeChoices = random.randrange(1,4)
if threeChoices == 1:
    B1.role = "Cop"
    B2.role = "Cop"
    G1.role = "Prisoner"
    G2.role = "Prisoner"
    R1.role = "Prisoner"
    R2.role = "Prisoner"
elif threeChoices == 2:
    B1.role = "Prisoner"
    B2.role = "Prisoner"
    G1.role = "Cop"
    G2.role = "Cop"
    R1.role = "Prisoner"
    R2.role = "Prisoner"
elif threeChoices == 3:
    B1.role = "Prisoner"
    B2.role = "Prisoner"
    G1.role = "Prisoner"
    G2.role = "Prisoner"
    R1.role = "Cop"
    R2.role = "Cop"
else:
    print("\nThere has been an error. Restart the game.")
    quit()

input("\n" + B1.color + "'s role is " + B1.role + "\nEnter to continue: ")
input("\n" + G1.color + "'s role is " + G1.role + "\nEnter to continue: ")
input("\n" + R1.color + "'s role is " + R1.role + "\nEnter to continue: ")




while run:
    checkWin()
    roll()
    onePiece = B1
    twoPiece = B2
    characterChoice()
    checkTile()
    specialTile()
    checkWin()
    roll()
    onePiece = G1
    twoPiece = G2
    characterChoice()
    checkTile()
    specialTile()
    checkWin()
    roll()
    onePiece = R1
    twoPiece = R2
    characterChoice()
    checkTile()
    specialTile()
    checkWin()
    
    