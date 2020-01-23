# Simple Analog Clock (Python 3)

# import turtle graphics
import turtle 

#import time
import time

wn = turtle.Screen() # Create Screen
wn.bgcolor("black") # background color
wn.setup(width=600, height=600) # dimensions of screen
wn.title("Simple Analog Clock by @iNode.code") # title
wn.tracer(0) # turns off animation

# Create drawing pen
pen = turtle.Turtle()
pen.hideturtle() # Hide Turtle from screen
pen.speed(0) # Animation speed as fast as possible
pen.pensize(3) # width of line being drawn


#Function
def draw_clock(h, m, s, pen): # Defining function, draw a clock, using pen turtle that was created h, m, s, = Hours, Minutes, Seconds

    # Draw clock face
    pen.up() # Dont want to draw a line
    pen.goto(0, 210) # Placement of pen tool
    pen.setheading(180) # turtle facing to the eft
    pen.color("white") # Color
    pen.pendown() # I want a line drawn at this point
    pen.circle(210) # Draw circle 210 is radius of circle


    # Draw hands
    pen.penup() # Stop drawing line
    pen.goto(0,0) # Go to center
    pen.setheading(90) # Face up

    # For Loop
    # Place holder
    for _ in range(12): # 12 Hours on dial
        pen.fd(190)
        pen.pendown() # Draw
        pen.fd(20) # Length of tick marks
        pen.penup() # Stop Drawing
        pen.goto(0,0) # Go to center
        pen.rt(30) # 30x12 is 360 = evenly spaced lines around cirle

    # Draw Hour Hand
    pen.penup() # Stop Drawing
    pen.goto(0,0) # Go to center
    pen.color("white") # Pen color
    pen.setheading(90) # 90 is straight up
    angle = (h / 12) * 360 # The angle equals the hour, divided by 12 * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

        # Draw minute Hand
    pen.penup() # Stop Drawing
    pen.goto(0,0) # Go to center
    pen.color("blue") # Pen color
    pen.setheading(90) # 90 is straight up
    angle = (m / 60) * 360 # The angle equals the minute, divided by 60(60 minutes in hour) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(150) # Length of minute hand

        # Draw second Hand
    pen.penup() # Stop Drawing
    pen.goto(0,0) # Go to center
    pen.color("gold") # Pen color
    pen.setheading(90) # 90 is straight up
    angle = (s / 60) * 360 # The angle equals the second, divided by 60(60 seconds in minute) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(60) # Length of second hand

#Gives us time in string format, %I gives us the hour from 0-12
while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M")) 
    s = int(time.strftime("%S"))  

    # Call Function
    draw_clock(h, m, s, pen) # 10o'clock, 15 minutes, 0 seconds
    # Side note Everything is drawn into memory, the update pulls everything to screen
    wn.update()

    #Sleep for one second
    time.sleep(1)

    #Clear the last checked clock time
    pen.clear() 


wn.mainloop()