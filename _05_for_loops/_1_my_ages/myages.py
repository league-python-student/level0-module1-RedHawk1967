from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    age = simpledialog.askinteger(title="", prompt="How old are you?")

    for i in range(age+1):
        print("I am "+str(i)+" years old")

