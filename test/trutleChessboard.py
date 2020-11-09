import turtle

x = (-270,-240,-210,-180,-150,-120,-90,-60,-30,0,30,60,90,120,150,180,210,240,270)
#绘制折线
l = -270
turtle.penup()
turtle.goto(-20,300)
turtle.pendown()
turtle.write('中国围棋')    #画围棋棋盘
for i in range(len(x)):
    turtle.penup()
    turtle.goto(x[i],abs(l))
    turtle.pendown()
    turtle.goto(x[i],l)
    turtle.penup()
    turtle.goto(l,x[i] )
    turtle.pendown()
    turtle.goto(abs(l),x[i])
turtle.done()