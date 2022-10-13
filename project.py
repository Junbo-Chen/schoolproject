import random
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
from numpy import dtype


x = "y"
score = 0

while x == "y":
    doublesteen = random.randint(1,6)
    dt = random.randint(7,12) 

    if doublesteen == 1:
        punt = 1
        print("you rolled a 1")
        print("┌─────────┐")
        print("|         |")
        print("|    0    |")
        print("|         |")
        print("└─────────┘")
    if doublesteen == 2:
        punt = 2
        print("you rolled a 2")
        print("┌─────────┐")
        print("|  0      |")
        print("|         |")
        print("|      0  |")
        print("└─────────┘")
    if doublesteen == 3:
        punt = 3
        print("you rolled a 3")
        print("┌─────────┐")
        print("|  0      |")
        print("|    0    |")
        print("|       0 |")
        print("└─────────┘")
    if doublesteen == 4:
        punt = 4
        print("you rolled a 4")
        print("┌─────────┐")
        print("| 0     0 |")
        print("|         |")
        print("| 0     0 |")
        print("└─────────┘")
    if doublesteen == 5:
        punt = 5
        print("you rolled a 5")
        print("┌─────────┐")
        print("| 0     0 |")
        print("|    0    |")
        print("| 0     0 |")
        print("└─────────┘")
    if doublesteen == 6:
        punt = 6
        print("you rolled a 6")
        print("┌─────────┐")
        print("| 0  0  0 |")
        print("|         |")
        print("| 0  0  0 |")
        print("└─────────┘")
    if dt == 7:
        punt2 = 1
        print("machine rolled a 1")
        print("┌─────────┐")
        print("|         |")
        print("|    0    |")
        print("|         |")
        print("└─────────┘")
    if dt == 8:
        punt2 = 2
        print("machine rolled a 2")
        print("┌─────────┐")
        print("|  0      |")
        print("|         |")
        print("|      0  |")
        print("└─────────┘")
    if dt == 9:
        punt2 = 3
        print("machine rolled a 3")
        print("┌─────────┐")
        print("|  0      |")
        print("|    0    |")
        print("|       0 |")
        print("└─────────┘")
    if dt == 10:
        punt2 = 4
        print("machine rolled a 4")
        print("┌─────────┐")
        print("| 0     0 |")
        print("|         |")
        print("| 0     0 |")
        print("└─────────┘")
    if dt == 11:
        punt2 = 5
        print("machine rolled a 5")
        print("┌─────────┐")
        print("| 0     0 |")
        print("|    0    |")
        print("| 0     0 |")
        print("└─────────┘")
    if dt == 12:
        punt2 = 6
        print("machine rolled a 6")
        print("┌─────────┐")
        print("| 0  0  0 |")
        print("|         |")
        print("| 0  0  0 |")
        print("└─────────┘")
    if punt > punt2:
        print("you win")
        score = score + 1
    elif punt < punt2:
        print("you lose")
        score = score - 1
    else:
        print("draw")
        score + 0

    x=input("press y to roll again and n to exit:")
    print("\n")
    if x == "n":
        print("Thanks for playing")
        print("your score is", score)
        if score > 10:
            img = Image.open('img/duim.jpg')
            img.show()
        if(score < 0):
            img = Image.open('img/L.jpg')
            img.show()
