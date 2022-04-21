from turtle import *
import turtle as t
import colorsys
#for circle

# bgcolor('black') 
# speed(0) #spped of circle
# hideturtle()
# for i in range(120):
#     #for outer circle
#     color('red')
#     circle(i)
#     #for inner circle
#     color('orange')
#     circle(i*0.8)
#     right(3)
#     forward(3)
# done()

# # for squre

# bgcolor('black')
# col=('white','orange','red','yellow','green','blue','cyan')
# speed(0)
# for i in range(200):
#     forward(i*4)
#     right(91)
#     color(col[i%7])
#     for b in range(3):
#         forward(i*4)
#         right(91)
#         for c in range(2):
#             forward(i*4)
#             right(91)


#for virus pattern
speed(0.3)
color('cyan')
bgcolor('black')
b=200
while b>0:
    left(b)
    forward(b*3)
    b=b-1


s=t.Screen()
s.bgcolor('black')
t.speed(0)
n=36
h=0
for i in range(360):
    c=colorsys.hsv_to_rgb(h,1,0.8)
    h+=1/n
    t.color(c)
    t.left(10)
    for j in range(5):
        t.forward(200)
        t.left(144)