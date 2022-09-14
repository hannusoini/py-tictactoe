"""
Python noughts and crosses v1

"""
def initGrid(): # finish grid initialisation
    #Grid = [['1', '2', '3'],['4', '5', '6'],['7', '8', '9']]
    Grid = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
    return Grid


def main():  # todo finish this function
    hello = 0
    while hello < 100:
        print(hello)
        hello = hello + 1
    return False


def displayGrid(Grid):
    print('--------------')
    for i in range(3):
        print('¦ ',end='')
        for j in range(3):
            print(Grid[i][j],'¦ ',end='')
        print('')
        print('--------------')

def MakeSelection():
    Choice=input("Choose a grid position 1-9?")
    print("You chose ",Choice)
    NewGrid=ModifyGrid('X',Choice,Grid)
    return NewGrid

def ModifyGrid(Player,Choice,Grid):
    cnt=0
    for i in range(3):
        for j in range(3):
            if cnt==Choice:
                Grid[i][j]=Player
            cnt=cnt+1
    return Grid

WelcomeMsg = "Welcome to Noughts and Crosses"

print(WelcomeMsg)
Grid=initGrid()
GameOver=False
while GameOver==False:
    displayGrid(Grid)
    Grid=MakeSelection()



# main()
