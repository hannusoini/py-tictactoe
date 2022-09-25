"""
Python noughts and crosses v1
Simple text based w/ functions
"""
import random

def initGrid(): # finish grid initialisation
    Grid = ['1', '2', '3','4', '5', '6', '7', '8', '9']
    # Grid = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    #Grid = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
    return Grid

def main(Grid):  #
    displayGrid(Grid)
    while True:
        Grid=MakeSelection(Grid)
        displayGrid(Grid)
        if IsGameOver(Grid, 'X'):
            break
        Grid=ComputerSelection(Grid)
        displayGrid(Grid)
        if IsGameOver(Grid, 'O'):
            break
    return

def IsGameOver(Grid, Player):
    # Check for rows 3
    if Grid[0]==Grid[1]==Grid[2] or Grid[3]==Grid[4]==Grid[5] or Grid[6]==Grid[7]==Grid[8]:
        print("Player ",Player," wins!")
        return True
    # check for columns 3
    elif Grid[0]==Grid[3]==Grid[6] or Grid[1]==Grid[4]==Grid[7] or Grid[2]==Grid[5]==Grid[8]:
        print("Player ", Player, " wins!")
        return True
    # check for diagonals 2
    elif Grid[0] == Grid[4] == Grid[8] or Grid[2] == Grid[4] == Grid[6]:
        print("Player ", Grid[0], " wins!")
        return True
    # check for tie (no avail squares)
    cnt=0
    for i in range(len(Grid)):
        if Grid[i]=='X' or Grid[i]=='O':
            cnt=cnt+1
    if cnt==9:
        print("It's a tie!")
        return True
    return False

def ComputerSelection(OldGrid):
    while True:
        Choice = random.randint(1,9)
        print("Computer chose: ", Choice)
        ValidSelection = IsValidChoice(Grid, int(Choice) - 1)
        if ValidSelection:
            NewGrid = ModifyGrid('O', int(Choice) - 1, OldGrid)
            break
    return NewGrid

def displayGrid(Grid):
    print('--------------')
    cnt = 0
    for i in range(3):
        print('¦ ',end='')
        for j in range(3):
            print(Grid[cnt],'¦ ',end='')
            cnt = cnt +1
        print('')
        print('--------------')

def IsValidChoice(Grid,Choice):
    if Grid[Choice]=='X' or Grid[Choice]=='O':
        return False
    return True
def MakeSelection(OldGrid):
    while True:
        Choice=input("Choose a grid position 1-9 or Q to quit?: ").lower()
        print("You chose ",Choice)
        if Choice == "q":
            exit()
        ValidSelection=IsValidChoice(Grid,int(Choice)-1)
        if ValidSelection:
            NewGrid=ModifyGrid('X',int(Choice)-1,OldGrid)
            break
        print("Invalid choice.")
    return NewGrid

def ModifyGrid(Player,Choice,Grid):
   Grid[Choice]=Player
   return Grid

WelcomeMsg = "Welcome to Noughts and Crosses"

print(WelcomeMsg)
Grid=initGrid()
main(Grid)
