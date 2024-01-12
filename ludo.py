

import random
import time

print("                                                                     THE LUDO \n ")
time.sleep(.2)
name=input("Enter your name: ")
time.sleep(.4)
print("Hello", name, "welcome to the LUDO")
input("Press any key to start LUDO")
print(" loading...\n")
time.sleep(5)
l=[]
attempt=4
flag=1
LUDO1=random.randint(1,6)
LUDO2=random.randint(1,6)
LUDO=LUDO1+LUDO2

while(attempt!=0):
    num=int(input("Guess and enter the sum of two numbers in between of 2 to 12 : "))
    time.sleep(2)
    while(num>12 or num<2):
        if (num>12 or num<2):
            print("Enter the numbers between 2 and 12")
            num=int(input("Guess and enter the sum of two numbers: "))
    if(LUDO==num):
        flag=0
        print("CONGRATULATIONS !!! You win!!!\nThe numbers are: ",LUDO1,"and",LUDO2,"\n""And the sum is : ",LUDO)
        break
    else:
        print(" number was guessed is wrong!!! You lost a chance!\nGuess a new number, loser!")
        print()
        attempt-=1

if flag==1:
    print("You lose, the number was: ",LUDO)
