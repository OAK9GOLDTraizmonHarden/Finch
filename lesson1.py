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
    bird.setMove('F',100,50)
    bird.setTurn('L',15,100)
    bird.setMove('F',100,30)
    bird.setTurn('R',15,50)

def exercise3():
    bird.setTurn('L',360,50)
    bird.setTurn('R',360,100)

 

"""
move forward
turn right
move forward
turn right
move forward
turn right
move forward
"""
def exercise4():
    bird.setMove('F',25,50)
    bird.setTurn('R',90,50)
    bird.setMove('F',25,50)
    bird.setTurn('R',90,50)
    bird.setMove('F',25,50)
    bird.setTurn('R',90,50)
    bird.setMove('F',25,50)

def exercise5():
    bird.setMove('F',15,30)
    bird.setTurn('R',120,30)
    bird.setMove('F',15,30)
    bird.setTurn('R',120,30)
    bird.setMove('F',15,30)
exercise5()
