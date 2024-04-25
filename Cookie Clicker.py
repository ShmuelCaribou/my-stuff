import turtle
import time
import threading

wn = turtle.Screen()
wn.title("Cookie Clicker")
wn.bgcolor("Purple")

wn.register_shape("C:\\Users\\iCan Student\\Downloads\\cookie.gif")
wn.register_shape("C:\\Users\\iCan Student\\Downloads\\cursor.gif")
wn.register_shape("C:\\Users\\iCan Student\\Downloads\\grandma.gif")

cookie = turtle.Turtle()
cookie.shape("C:\\Users\\iCan Student\\Downloads\\cookie.gif")
cookie.speed(0)

cursor = turtle.Turtle()
cursor.shape("C:\\Users\\iCan Student\\Downloads\\cursor.gif")
cursor.hideturtle()
cursor.goto(400, 0)
cursor.showturtle()
cursor.speed(0)

Grandma = turtle.Turtle()
Grandma.shape("C:\\Users\\iCan Student\\Downloads\\grandma.gif")
Grandma.hideturtle()
Grandma.goto(-400, 0)
Grandma.showturtle()
Grandma.speed(0)

clicks = 0
increment = 1
cps = 0


pen = turtle.Turtle()
pen.hideturtle()
pen.color("White")
pen.penup()
pen.goto(0, 200)
pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32))

def clicked(x, y):
    global clicks, increment
    clicks += increment
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32))

def granny_clicked(x, y):
    global clicks, cps
    if clicks >= 100:
        clicks -= 100
        cps += 1
        pen.clear()
        pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32))

def time_operation():
    global clicks
    while True:
        time.sleep(1)
        clicks += cps
        pen.clear()
        pen.write(f"Clicks: {clicks}", align ="center", font=("Courier New", 32, "normal"))

def cursorClicked(x, y):
    global clicks, increment
    if clicks >= 50:
        clicks -= 50
        increment += 1
        pen.clear()
        pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32))

t1 = threading.Thread(target=time_operation, name='t1')
t1.start()

cookie.onclick(clicked)
Grandma.onclick(granny_clicked)
cursor.onclick(cursorClicked)



wn.mainloop()
