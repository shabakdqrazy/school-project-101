
import random
import time
print("  STONE PAPER SCISSOR GAME ")
time.sleep(1)
print()
user=input("Enter your name: ")
print("Hello",user,"! Welcome to the STONE Paper Scissors Program!")
input("CLICK Enter to start the game")
print("loading...")
time.sleep(3)
result = 0
while result == 0:
    print('''Press 1 for STONE.\nPress 2 for Paper.\nPress 3 for Scissors.''')

    UserInput = int(input("What would you like to play?"))
    try:
        if UserInput not in range(1,4):
            print("Enter the number between 1 and 3 ONLY!!!")
            print()
            time.sleep(2)
            continue
    except ValueError:
        print("We only accept digits")
        continue
    ComputerInput = random.randrange(1,3)
    if (UserInput == 1) and (ComputerInput == 1):
        result = 0
        print("It's a draw, you both played STONE!") 
    if (UserInput == 2) and (ComputerInput == 1):
        result == 1
        print("You win! The computer played STONE!")
    if (UserInput == 3) and (ComputerInput == 1):
        result == 1
        print("You lose! The computer played STONE!")
    if (UserInput == 1) and (ComputerInput == 2):
        result = 1
        print("You lose! The computer played Paper!")
    if (UserInput == 2) and (ComputerInput == 2):
        result == 0
        print("It's a draw, the computer played Paper!")
    if (UserInput == 3) and (ComputerInput == 2):
        result == 1
        print("You win! The computer played Paper!")    
    if (UserInput == 1) and (ComputerInput == 3):
        result = 1
        print("You win! The computer played Scissors!")
    if (UserInput == 2) and (ComputerInput == 3):
        result == 1
        print("You lose! The computer played Scissors!")
    if (UserInput == 3) and (ComputerInput == 3):
        result == 0
        print("It's a draw, the computer played Scissors!")
    print()
    command = int(input("Type 0 to stop the program, type any another number to keep playing"))
    if command == 0:
        break




    
