from tkinter import simpledialog, messagebox, Tk
import math
# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    radius = simpledialog.askinteger(title="",prompt="give me a radius of a circle")
    aorc = simpledialog.askstring(title="", prompt="Do you want to calculate the area or circumference of the circle ")
    if aorc == "area":
        messagebox.showinfo(title="", message=math.pi*radius**2 )
    if aorc == "circumference":
        messagebox.showinfo(title="", message=2*math.pi*radius)