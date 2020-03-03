import turtle
import os 
import math
import random

# Setup and defines screen
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Space Invaders')
wn.bgpic('python/python/PythonGames/SpaceInvaders/space_invaders_background.gif')

#Register the shape 
turtle.register_shape('python/python/PythonGames/SpaceInvaders/invader.gif')
turtle.register_shape('python/python/PythonGames/SpaceInvaders/player.gif')

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

# Set the score to 0
score = 0

#Draw the score 
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = 'Score: %s' %score
score_pen.write(scorestring, False, align = 'left', font=('Courier', 18, 'normal'))
score_pen.hideturtle()

# Create the player 
player = turtle.Turtle()
player.shape('python/python/PythonGames/SpaceInvaders/player.gif') 
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 20  

#Set number of enemies
number_of_enemies = 10 
#Create any empty list of enemies
enemies = []

#Add enemies to list 
for i in range(number_of_enemies): 
  #Create the enemy
    enemies.append(turtle.Turtle())

# Creates the invaders
for enemy in enemies: 
    enemy.shape('python/python/PythonGames/SpaceInvaders/invader.gif')
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)
  
enemyspeed = 5

#Create the player's bullet
bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 30

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
    
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False
      
#Create keyboard bindings
wn.listen()
wn.onkey(move_left, 'Left')
wn.onkey(move_right, 'Right')
wn.onkey(fire_bullet, 'space')


# Main Game Loop 
while True: 
  
    for enemy in enemies:
      #Move Enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #Move the enemy back / forth and down
        if enemy.xcor() > 280:
           # moves all enemies down together
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #changes enemy direction
            enemyspeed *= -1

        if enemy.xcor() < -280:
         # moves all enemies down together
            for e in enemies: 
                y =e.ycor()
                y -= 40  
                e.sety(y)
            #changes enemy direction   
            enemyspeed *= -1
           
            #check for collision of bullet with enemy
        if isCollision(bullet, enemy):
            #reset bullet
            bullet.hideturtle()
            bulletstate = 'ready'
            bullet.setposition(0, -400)
            #Reset enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x,y)
            #Update the score
            score += 10
            score_pen.clear()
            scorestring = 'Score: %s' %score
            score_pen.write(scorestring, False, align = 'Left', font=('Courier', 18, 'normal'))
        
        #check for collision with player
        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print('Game Over!')
            break   
          
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