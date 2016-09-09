import turtle #import the drawing tool
r = 'r' #these are to save keystrokes
l = 'l'
old = r #setting these up for the first iteration
new = r
i=1
while i<10: #this loop generates the steps all at once. 
    new = old + r #add a 'right' to the new one before changing it
    old = old[::-1] #reverse the list
    for j in range(0,len(old)): #invert the steps (l=r and r=l)
        if old[j] == r:
            old = old[:j]+ l + old[j+1:]
        elif old[j] == l:
            old = old[:j] + r + old[j+1:]
    new = new + old #add that changed list to the previous step (plus 'right')
    old = new #now get ready for the next step
    i+=1

turtle.ht() #hides the turtle
turtle.speed(0) #set to fastest speed
turtle.color('white') #line=white
turtle.bgcolor('black') #background=black
turtle.down() #put pen down
turtle.forward(10) # make the first step
for step in range(0,len(new)):
    if new[step] == (r): #if right turn right and move
        turtle.right(90)
        turtle.forward(10)
    elif new[step] == (l): #if left turn left and move
        turtle.left(90)
        turtle.forward(10)

turtle.up() #put pen up
turtle.goto(100,100) #go to 100,100 to write text
turtle.write("Click to exit", font=("Arial", 16, "normal")) #add some text so they know to click to exit
turtle.exitonclick() #exit on click