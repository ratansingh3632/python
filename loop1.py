from turtle import *
pencolor('blue')
pensize(3)
speed('slowest')
for i in range(10):
    fd(120)
    lt(360/10)
    write(i,font=('calibri',25))
hideturtle()
mainloop()