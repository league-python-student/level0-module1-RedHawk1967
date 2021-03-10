import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    my_turtle = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title="",prompt="Enter a common shape")
    # Draw the shape requested by the user using if-elif-else statements
    if shape == "circle":

        for i in range(360):
            my_turtle.forward(1)
            my_turtle.right(1)
    if shape == "square":

        for i in range(4):
            my_turtle.forward(90)
            my_turtle.right(90)

    if shape == "rhombus":

        for i in range(2):
            my_turtle.right(45)
            my_turtle.forward(50)
            my_turtle.right(135)
            my_turtle.forward(50)
    # Call the turtle .done() method
    
    window.mainloop()