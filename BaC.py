from random import randint
import time

def secret():
    scd=''
    while len(scd)<4:
        a=str(randint(0,10))
        if str(a) not in scd:
            scd+=a
    return int(scd)

def bull(x,y):
    count=0
    x=list(str(x))
    y=list(str(y))
    for i in range(len(x)):
        if x[i]==y[i]:
            count+=1
    return str(count)+" bulls"

def cow(x,y):
    count=0
    x=list(str(x))
    y=list(str(y))
    for i in range(len(x)):
        if x[i]!=y[i] and x[i] in y:
            count+=1
    return str(count)+" cows"

scd = secret()
guess=0
attempt=10

print("Welcome to Bulls and Cows! In this game you will try to guess the secret code.\nSecret code is 4-digit number, and every digit is various.\nYou have 10 chances to guess.\nGood luck!")
time.sleep(1)
print("Loading....")
time.sleep(5)

while guess!=scd and attempt!=0:
    guess=int(input('Guess: '))
    if guess==scd:
        print(f'Secret code is {guess}. You guessed right!!! Congratulations!!!')
        break
    else:
        print("Response: "+bull(guess,scd)+', '+cow(guess,scd))
        attempt-=1
        print("Attempt number you have:",attempt)
if attempt==0:
        print('You losed :(\nSecret code is',scd,'\nSee you next time ;)')