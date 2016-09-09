import turtle
r = 'r'
l = 'l'
old = r 
new = r
i=1
while i<10:
    new = old + r
    old = old[::-1]
    for j in range(0,len(old)):
        if old[j] == r:
            old = old[:j]+ l + old[j+1:]
        elif old[j] == l:
            old = old[:j] + r + old[j+1:]
    new = new + old
    old = new
    i+=1

turtle.ht()
turtle.speed(0)
turtle.color('white')
turtle.bgcolor('black')
turtle.down()
turtle.forward(10)
for step in range(0,len(new)):
    if new[step] == (r):
        turtle.right(90)
        turtle.forward(10)
    elif new[step] == (l):
        turtle.left(90)
        turtle.forward(10)

turtle.up()
turtle.goto(100,100)
turtle.write("Click to exit", font=("Arial", 16, "normal"))
turtle.exitonclick()
