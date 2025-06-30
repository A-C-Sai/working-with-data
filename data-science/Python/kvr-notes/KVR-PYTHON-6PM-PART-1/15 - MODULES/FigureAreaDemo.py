#FigureAreaDemo.py
import sys
from FigMenu import menu
from Circle import area as ca
from Rect import area as ra
from Square import area
while(True):
    menu()
    ch=input("Enter Ur Choice:")
    match(ch):
        case 'C'| 'c':ca()
        case 'S'| 's': area()
        case 'R'| 'r':ra()
        case "E"|'e':
            print("Tq For Using this Proghram")
            sys.exit()
        case _:
            print("Ur Selection of Operation is wrong-try again")