import turtle
import time
import random
import math

turtle.colormode(255)
def random_color(j):
    r = random.randint(0 , 255)
    g = random.randint(0 , 255)
    b = random.randint(0 , 255)
    j.color(r , g , b)

def set_screen():
    r = turtle.Screen()
    r.title("Arkanoid Game")
    r.bgcolor("black")
    r.setup(width=600 , height= 600)
    r.tracer(0)
    return  r   

def make_jaabe():
    o = turtle.Turtle()
    o.speed(0)
    o.shape("square")
    o.shapesize(1 , 5 , 1)
    o.color("gray")
    o.penup()
    o.setpos(0 , -230)
    o .direction = "stop"
    return o

my_blocks =[]
def draw_tikeha(h):
    for i in range(1 , 13):
        o = str(i)
        o = turtle.Turtle()
        o.shape("square")
        random_color(o)
        o.shapesize(0.5 , 3 , 2)
        o.penup()
        if i<= 12 :
            o.setpos(300-(45 * i) , h)
        my_blocks.append(o)
        
def draw_ball():
    b = turtle.Turtle()
    b.speed(1)
    b.shape("circle")
    b.shapesize(1)
    b.color("red")
    b.penup()
    b.setpos(0 , -220)
    b.direction = "stop"
    return b 

def move_jaabe(j):
    x , y = j.position()
    if j.direction == "right":
        j.setposition(x+20, y)
    
    if j.direction == "left":
        j.setposition(x-20, y)

def keyboard_listening(r):
    r.listen()
    r.onkey(go_right , "Right")
    r.onkey(go_left , "Left")

def go_right():
    j.direction = "right"

def go_left():
    j.direction = "left"

def hazf_tikeha(b , blocks):
    for o in blocks:
        xo , yo = o.position()
        xb , yb = b.position()
        if abs(xb - xo) < 20 and abs(yb - yo) < 20 :
            o.setpos(1000,1000)
            return o 

def hit_wall1(ball):
    xb = ball.xcor()
    if xb > 240 or xb < -240 :
        return True

def hit_wall2(ball):
    yb = ball.ycor()
    if yb > 240:
        return True

def hit_wall3(ball):
    yb = ball.ycor()
    if yb < -250 :
        return True

def hit_jabe(ball):
    yb = ball.ycor()
    xb = ball.xcor()
    yj = j.ycor()
    xj = j.xcor()               
    if xj-40<xb<xj+40 and  yj-40<yb<yj+40 :
        return True

def lose_game(ball):
    j.setpos(0 , -250)
    ball.setpos(0 , -220)
    ball.direction = "stop"

x0 = 0
y0 = -2
def move_ball(ball):
    global x0
    global y0
    t = 1
    x0 = Vx * t + x0
    y0 = Vy * t + y0
    ball.setposition(x0 , y0)
    return ball

def update_score():
    score_writer.undo()
    score_writer.hideturtle()
    score_writer.setpos(0 , 260)
    score_writer.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

def reset_score():
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    return pen

p = set_screen()
j = make_jaabe()
ball = draw_ball()
o = turtle.Turtle()
m = [250 , 200 , 150 , 100]
for i in m:
    draw_tikeha(i)
V0 = 15 * (2**(1/2))
theta = 50
Vx = V0 * math.cos(theta * math.pi / 180)
Vy = V0 * math.sin(theta * math.pi / 180)
keyboard_listening(p)
score = 0
score_writer = reset_score()

while True :
    move_jaabe(j)
    move_ball(ball)
    if hit_jabe(ball):
        Vy = Vy * (-1)
    if hit_wall1(ball) :
        Vx = Vx * (-1)
    if hit_wall2(ball) :
        Vy = Vy * (-1)
    if hit_wall3(ball):
        lose_game(ball)
    if hazf_tikeha(ball ,my_blocks ):
        score = score + 10

    update_score()
    reset_score()
    p.update()
    time.sleep(0.1)