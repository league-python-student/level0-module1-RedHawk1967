from tkinter import messagebox, simpledialog, Tk
# Write a Python program that asks the user for two numbers.
# Then display the sum of the two numbers

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    num1 = simpledialog.askstring(title="",prompt="Enter a number")
    num2 = simpledialog.askstring(title="", prompt="Enter a number")