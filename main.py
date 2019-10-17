from tkinter import *

window = Tk()

lab1 = Label(window, text="Labe1", bg="red")
lab2 = Label(window, text="Labe2", bg="yellow")
entry1 = Entry(window)
entry2 = Entry(window)
entry3 = Entry(window)
entry4 = Entry(window)
lab1.grid(row=0, sticky=E)
lab2.grid(row=1)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

c = Checkbutton(window, text="oh hello there")
c.grid(row=2, column=0, rowspan = 2)
if __name__ == '__main__':
    window.mainloop()
