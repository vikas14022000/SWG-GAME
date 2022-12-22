import random
import re

def gamewin(comp,your):
    if comp == your:
        return 
    elif comp == 's':
        if your == 'w':
            return False
        elif your == 'g':
            return True
    elif comp == 'w':
        if your == 'g':
            return False
        elif your == 's':
            return True
    elif comp == 'g':
        if your == 's':
            return False
        elif your == 'w':
            return True
print("Comp turn : Snake(s) Water(w) Gun(g)")
randno = random.randint(1,3)
if randno == 1:
    comp = 's'
elif randno == 2:
    comp = 'w'
elif randno == 3:
    comp = 'g'
your = input("Your turn : Snake(s) Water(w) Gun(g) = ")

a = gamewin(comp, your)



print(f"Computer choice : {comp}")
print(f"Your Choice : {your}")

if a == None:
    print("The game is tie !")

if a == True:
    print("You won the game")

if a == False:
    print("You loose the game")

