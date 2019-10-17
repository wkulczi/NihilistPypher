from tkinter import *

root = Tk()

frame = Frame(root)

Label(root, text="First Name").grid(row=0, sticky=W, padx=4)
Entry(root).grid(row=0,column=1,sticky=E,pady=4)

Label(root, text="Second Name").grid(row=1, sticky=W, padx=4)
Entry(root).grid(row=1,column=1,sticky=E,pady=4)

Button(root,text="Submit").grid(row=3)

if __name__ == '__main__':
    root.mainloop()
