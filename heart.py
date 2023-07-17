import math 
from turtle import *
def blankA(k):
    return 15*math.sin(k)**3
def blankB(k):
    return 12*math.cos(k)-5*\
    math.cos(2*k)-2*\
    math.cos(3*k)-\
    math.cos(4*k)

speed(0)
bgcolor("black")
for i in range(10000):
    goto(blankA(i)*20,blankB(i)*20)
    for j in range (5):
        color("#ce1f26")
    goto(0,0)
done()


#tryna do a star now