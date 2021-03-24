from tkinter import messagebox, simpledialog, Tk
# Write a Python program that asks the user for two numbers.
# Then ask the user if the would like to add, subtract, multiply, or divide.
# Use if-else statements to provide the desired math operation on the numbers and display the result.
if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    num1 = simpledialog.askstring(title="", prompt="Enter a number")
    num2 = simpledialog.askstring(title="", prompt="Enter a number")

    operation = simpledialog.askstring(title="", prompt="would you like to add, subtract, multiply, or divide?")

    if operation == "add":
        sum = float(num1) + float(num2)
    elif operation == "subtract":
        sum = float(num1) - float(num2)
    elif operation == "multiply":
        sum = float(num1) * float(num2)
    else:
        sum = float(num1) / float(num2)

    messagebox.showinfo(title="", message=sum)