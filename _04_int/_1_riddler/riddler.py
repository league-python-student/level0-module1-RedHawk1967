
from tkinter import messagebox, simpledialog, Tk
'''
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got correct
'''
if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    riddle1 = simpledialog.askstring(title="", prompt="The more you take, the more you leave behind. What am I?")
    riddle2 = simpledialog.askstring(title="",prompt="What has a head, a tail, is brown, and has no legs?")
    riddle3 = simpledialog.askstring(title="",prompt="David's father has three sons: Snap, Crackle, and _____?")

    correct = 0
    con_correct = str(correct)
    if riddle1 == "footsteps":
        correct+1

    if riddle2 == "penny":
        correct+1

    if riddle3 == "david":
        correct+1

    messagebox.showinfo(title="", message="Nice you got "+con_correct+" riddles correct")