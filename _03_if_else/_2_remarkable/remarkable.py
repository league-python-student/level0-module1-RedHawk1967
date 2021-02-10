from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    window=Tk()
    window.withdraw()

    name= simpledialog.askstring(title="Question", prompt="Type in your name")
    remarkable = simpledialog.askstring(title="Question", prompt="Type in something remarkable about yourself")

    ask=simpledialog.askstring(title="Question", prompt="Enter one of these names, "+ name)
    if ask==name:
        messagebox.showinfo(message=remarkable)
