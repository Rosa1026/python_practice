import math as mt
import turtle as t

#1
for i in range(1,301,30):
    print("log({}) = {:.3f}".format(i, mt.log(i)))

#2
def line(x1,y1,x2,y2):
    t.up()
    t.goto(x1,y1)
    t.down()
    t.goto(x2,y2)

    return

def write(x,y,text):
    t.up()
    t.goto(x,y)
    t.down()
    t.write(text)
    
    return

#좌표계
line(-500,0,500,0)
line(0,-500,0,500)

# x축 눈금 그리기
i=-500
while i <= 500:
    line(i,-5,i,5)
    if i != 0:
        write(i-10,-20,i)
    i += 100

# y축 눈금 그리기
i = -500
while i <= 500:
    line(-5, i, 5, i)
    if i!=0:
        write(7, i-5, i)
    i += 100

t.home()

for i in range(1,301,30):
    t.color('red')
    t.forward(i)
    t.left(mt.log(i))
