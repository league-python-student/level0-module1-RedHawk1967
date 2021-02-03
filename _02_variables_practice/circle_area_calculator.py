import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    awn = simpledialog.askinteger(title="", prompt="give me a number")
    
    # Make a new turtle
    turtle1 = turtle.Turtle()
    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()
    turtle1.circle(awn)
    # Call the turtle .penup() method
    turtle1.penup()
    # Move your turtle to a new x,y position using .goto()
    turtle1.goto(123,123)
    # Calculate the area of your circle and store it in a variable, you can use math.pi
    area = math.pi*awn**2
    # Write the area of your circle using the turtle .write() method

    turtle1.write(arg= "area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))

    # Hide your turtle
    turtle1.hideturtle()
    # Call turtle.done()
    turtle.done
    window.mainloop()