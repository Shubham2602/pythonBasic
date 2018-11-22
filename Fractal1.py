import turtle
turtle.showturtle()
turtle.speed(10)

i=250
n=i+10
t=i+10

for i in range(0,10):
  turtle.pensize(1)
  turtle.goto(0,0)
  turtle.right(90)
  turtle.pendown()
  turtle.forward(n)
  turtle.right(t)

  turtle.forward(n+1)
  turtle.right(t+1)

  turtle.forward(n+2)
  turtle.right(t+2)

  turtle.forward(n+3)
  turtle.right(t+3)

  turtle.forward(n+4)
  turtle.right(t+4)

  if(i==1):
    turtle.pensize(1.5)
  elif(i==2):
    turtle.pensize(2)
  elif(i==4):
    turtle.pensize(2.5)
  elif(i==8):
    turtle.pensize(3)
  elif(i==10):
    turtle.pensize(3.5)
