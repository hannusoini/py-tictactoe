# import pygame
# pygame.init()
import array as arr

"""
Fix import
"""


def initGrid(): # finish grid initialisation
    Grid = [['1', '2', '3'],['4', '5', '6'],['7', '8', '9']]
    return Grid


def main():  # todo finish this function
    hello = 0
    while hello < 100:
        print(hello)
        hello = hello + 1
    return False


def displayGrid(Grid):
    for i in range(2):
        for j in range(0:2):
            print(Grid[i][j])

    # print(Grid[0][1], Grid[0][2])
    # print('X', 'X', 'X')
    # print('X', 'X', 'X')



WelcomeMsg = "Welcome to Noughts and Crosses"

print(WelcomeMsg)


InitialGrid=initGrid()
displayGrid(InitialGrid)
# main()
