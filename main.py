import os
import time

list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
def InputO():
    reading = True
    while reading == True:
        n = int(input("Enter where you wish to mark from (0-8):"))
        if list[n] != ' ':
            print("Not Applicable try again")
            continue
        else:
            list[n] = 'O'
            reading = False

def InputX():
    reading = True
    while reading == True:
        n = int(input("Enter where you wish to mark from (0-8):"))
        if list[n] != ' ':
            print("Not Applicable try again")
            continue
        else:
            list[n] = 'X'
            reading = False

def TicTacToe():
    print("       |            |    ")
    print(list[0], "     |    ", list[1], "     |    ", list[2])
    print("       |            |    ")
    print("-----------------------------")
    print("       |            |    ")
    print(list[3], "     |    ", list[4], "     |    ", list[5])
    print("       |            |    ")
    print("-----------------------------")
    print("       |            |    ")
    print(list[6], "     |    ", list[7], "     |    ", list[8])
    print("       |            |    ")

print("         TIC TAC TOE              ")
print(" This is the tic tac toe board :")
TicTacToe()
count=0
while count!=9:
    if count % 2 == 0:
        InputO()
        time.sleep(1)
        os.system("cls")
        TicTacToe()
        if count>=4 :
            if ((list[0] == list[1] == list[2] and list[0] != ' ') or (
                    list[3] == list[4] == list[5] and list[3] != ' ') or (
                    list[6] == list[7] == list[8] and list[6] != ' ') or (
                    list[0] == list[3] == list[6] and list[0] != ' ') or (
                    list[1] == list[4] == list[7] and list[1] != ' ') or (
                    list[2] == list[5] == list[8] and list[2] != ' ') or (
                    list[0] == list[4] == list[8] and list[4] != ' ') or (
                    list[2] == list[4] == list[6] and list[2] != ' ')):
                print("GAME OVER O WINS")
                break

        count += 1
    else:
        InputX()
        time.sleep(1)
        os.system("cls")
        TicTacToe()
        if count>=4 :
            if ((list[0] == list[1] == list[2] and list[0] != ' ') or (
                    list[3] == list[4] == list[5] and list[3] != ' ') or (
                    list[6] == list[7] == list[8] and list[6] != ' ') or (
                    list[0] == list[3] == list[6] and list[0] != ' ') or (
                    list[1] == list[4] == list[7] and list[1] != ' ') or (
                    list[2] == list[5] == list[8] and list[2] != ' ') or (
                    list[0] == list[4] == list[8] and list[4] != ' ') or (
                    list[2] == list[4] == list[6] and list[2] != ' ')):
                print("GAME OVER X WINS")
                break
        count += 1




