from BirdBrain import Finch

bird=Finch()

def exercise1():
    print("Distance: ", bird.getDistance())

def exercise2():
    getLight('R')
    getLight('L')
    getButton('A')
    getOrientation()
    getEncoder('R')

def exercise3():
    print(type(bird.getDistance()))
    print(type(bird.getLight('R')))
    print(type(bird.getLight('L')))
    print(type(bird.getButton('A')))
    print(type(bird.getOrientation()))
    print(type(bird.getEncoder('R')))

exercise3()
