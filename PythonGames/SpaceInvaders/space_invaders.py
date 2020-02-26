import turtle
import os 

# Setup and defines screen
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Space Invaders')

# Draw Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('white')
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Create the player 
player = turtle.Turtle()
player.color('blue')
player.shape('triangle')
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15 

# Creates the invaders
enemy = turtle.Turtle()
enemy.color('red')
enemy.shape('circle')
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)
enemy.setheading(90)

enemyspeed = 2

#Create the player's bullet
bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

#Define bullet state
#ready - ready to fire
#fire - bullet is firing 
bulletstate = 'ready'

# Move the player left and right
def move_left():
    '''moves player left defines left boundary'''
    x = player.xcor()
    x -= playerspeed
    if x < -280: 
        x = -280
    player.setx(x)
    
def move_right():
    '''moves player right defines right boundary'''  
    x = player.xcor()
    x += playerspeed
    if x > 280: 
        x = 280
    player.setx(x) 
 
 
def fire_bullet():
    '''Declare bulletstate as global, sets bullet'''
    global bulletstate
    if bulletstate == 'ready':
        bulletstate = 'fire'
    #Place the bullet to above the player
    x = player.xcor()
    y = player.ycor() + 10
    bullet.setposition(x, y)
    bullet.showturtle()
 
#Create keyboard bindings
wn.listen()
wn.onkey(move_left, 'Left')
wn.onkey(move_right, 'Right')
wn.onkey(fire_bullet, 'space')


# Main Game Loop 
while True: 
  
    #Move Enemy 
    x = enemy.xcor()
    x+= enemyspeed
    enemy.setx(x)
    
    #Move the enemy back / forth and down
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -=40
        enemyspeed *= -1
        enemy.sety(y)
   
    if enemy.xcor() < -280:
        y =enemy.ycor()
        y -=40  
        enemyspeed *= -1
        enemy.sety(y)
        
    #Move the bullet
    if bulletstate == 'fire': 
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    
    #Bullet Border Checking 
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = 'ready'
    
delay= input('Presen enter to finish')  