from tkinter import *

window = Tk()

lab1 = Label(window, text="Labe1", bg="red")
lab2 = Label(window, text="Labe2", bg="yellow")
lab3 = Label(window, text="Labe3", bg="blue")

lab3.pack(side=LEFT, fill=Y)
lab1.pack(side=RIGHT, fill=Y)
lab2.pack(fill=X)

if __name__ == '__main__':
    window.mainloop()
