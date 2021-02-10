from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':

    window=Tk()
    window.withdraw()

    ask = simpledialog.askstring(title = "question", prompt="what day where you born")

    if ask=="2/9":
        messagebox.showinfo(message="Happy Birthday")
    else:
        messagebox.showinfo(message="Unhappybirth")

