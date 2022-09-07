import turtle as t

#1
color = ['blue','yellow','black','green','red']
for i in range(5):
    t.color(color[i])
    t.pensize(5)
    t.circle(50)
    t.penup()
    if i == 4:
        break
    if i % 2 == 1:
        t.forward(55)
        t.left(90)
        t.forward(55)
        t.right(90)
    
    else:
        t.forward(55)
        t.right(90)
        t.forward(55)
        t.left(90)
    t.pendown()

#2
t.color('black')
t.forward(120)
t.pendown()
    
for i in range(4):
    t.pensize(5)
    t.circle(50)
    t.penup()
    if i == 3:
        break
    t.forward(70)
    t.pendown()
    
