import turtle as t
import random as rd

def dis_right(t):
    dis = rd.randrange(1,101)
    rig = rd.randrange(0,361)

    t.right(rig)
    t.penup() #3
    t.forward(dis)
    t.pendown() #3

t1 = t.Turtle()
t1.shape("turtle")
t1.color('black')

t2 = t.Turtle()
t2.shape("turtle")
t2.color('red')

t3 = t.Turtle()
t3.shape("turtle")
t3.color('blue')

t4 = t.Turtle()
t4.shape("turtle")
t4.color('green')

t5 = t.Turtle()
t5.shape("turtle")
t5.color('gray')

t6 = t.Turtle()
t6.shape("turtle")
t6.color('pink')

turtle_lst = [t1,t2,t3,t4,t5,t6]

for i in range(20):
    for j in turtle_lst:
        dis_right(j) #1
        j.stamp() #2
