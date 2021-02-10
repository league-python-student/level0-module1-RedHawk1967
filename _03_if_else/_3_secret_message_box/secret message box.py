from tkinter  import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window=Tk()
    window.withdraw()

    password="abc123"

    ask=simpledialog.askstring(title="Question",prompt="Enter a SECRET MESSAGE!!!")
    vault=simpledialog.askstring(title="Question",prompt="Enter the password to see your SECRET MESSAGE")

    if vault==password:
        messagebox.showinfo(message=ask)
