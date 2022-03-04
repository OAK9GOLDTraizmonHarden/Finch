"""
Author:Traizmon Harden
File Name:Lesson1.py
Date: 3.3.2022
"""
from BirdBrain import Finch

bird = Finch()


def exercise1():
    bird.setMove('F',10,50)

def exercise2():
    bird.setMove('F',15,10)
    bird.setMove('B',15,100)
    bird.setMove('F',15,30)
    bird.setMove('B',15,50)
    



def exercise3():
    bird.setTurn('L',360,50)
    bird.setTurn('R',360,100)

exercise3() 

"""
move forward
turn right
move forward
turn right
move forward
turn right
move forward
"""
   
