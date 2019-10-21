from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
import tkinter as tk

root = Tk()
root.title("NihilistPypher main")
root.geometry("900x600+200+200")
root.resizable(FALSE, FALSE)


def _exit():
    exit()


def _hello():
    print(x.get())
    print(y.get())


def filed():
    dir = filedialog.askopenfilename(initialdir="/", title="Select file",
                                     filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    print(dir)


x = IntVar()
y = IntVar()
label3 = Label(root, text="Input text").place(x=375, y=40)
label4 = Label(root, text="Key").place(x=402, y=320)
label5 = Label(root, text="Matrix word").place(x=360, y=280)
label6 = Label(root, text="Output").place(x=382, y=360)
label7 = Label(root, text="Substitute letters").place(x=20, y=40)
source_label = Label(root, text="Source:").place(x=200, y=40)


sub=list()
sub1 = Radiobutton(root, text="v<=>w", padx=20, variable=x, value=0).place(x=40, y=70)
sub.insert(0,Radiobutton(root, text="w<=>v", padx=20, variable=x, value=1).place(x=40, y=100))
sub.insert(0,Radiobutton(root, text="c<=>k", padx=20, variable=x, value=2).place(x=40, y=130))
sub.insert(0,Radiobutton(root, text="k<=>c", padx=20, variable=x, value=3).place(x=40, y=160))
sub.insert(0,Radiobutton(root, text="j<=>i", padx=20, variable=x, value=4).place(x=40, y=190))
source_button1 = Radiobutton(root, text="From text area", padx=20, variable=y, value=0).place(x=180, y=70)
source_button2 = Radiobutton(root, text="From file", padx=20, variable=y, value=1).place(x=180, y=100)

but1 = Button(root, text="Code", command=_hello).place(x=200, y=160)
but2 = Button(root, text="Decode", command=_hello).place(x=200, y=190)
but3 = Button(root, text="Generate grids", command=_hello).place(x=20, y=280)


#textboxy
txtbox2 = Text(root, width=50, height=1, wrap=tk.WORD).place(x=450, y=280)
txtbox3 = Text(root, width=50, height=1, wrap=tk.WORD).place(x=450, y=320)


#scrolled teksty
txtbox = ScrolledText(root, width=50, height=13, wrap=tk.WORD).place(x=450, y=40)
text = ScrolledText(root, state='disabled', width=50, height=13, wrap=tk.WORD).place(x=450, y=360)
grid = ScrolledText(root, state='disabled', width=40, height=16, wrap=tk.WORD).place(x=20, y=316)

root.mainloop()


#3 scrolled textboxy
#2 texty
#6 labelsów
#7 radio

#buttony