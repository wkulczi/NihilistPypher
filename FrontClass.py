from tkinter import *
from tkinter.scrolledtext import ScrolledText


# self.scroll_txt_list[0].insert(INSERT, "hello")

class Front:
    def _hello(self):
        self.str = self.scroll_txt_list[0].get('1.0', END)
        print(self.str)

    def setChoice(self):
        print(self.x.get())

    def __init__(self):
        self.root = Tk()
        self.root.title("NihilistPypher main")
        self.root.geometry("900x600+200+200")
        self.root.resizable(FALSE, FALSE)
        self.x = IntVar()
        self.y = IntVar()
        self.str = ""
        self.button_list = self.setButtonList()
        self.scroll_txt_list = self.setSTxtList()
        self.txt_list = self.setTxtList()
        self.label_list = self.setLabelList()
        self.radio_list = self.setRadioList()

    def setSTxtList(self):
        ST = [ScrolledText(self.root, width=50, height=13, wrap=WORD),
              ScrolledText(self.root, state='disabled', width=50, height=13, wrap=WORD),
              ScrolledText(self.root, state='disabled', width=40, height=16, wrap=WORD)]
        return ST

    def setTxtList(self):
        T = [Text(self.root, width=50, height=1, wrap=WORD), Text(self.root, width=50, height=1, wrap=WORD)]
        return T

    def setLabelList(self):
        L = [Label(self.root, text="Input text"), Label(self.root, text="Key"), Label(self.root, text="Matrix word"),
             Label(self.root, text="Output"), Label(self.root, text="Substitute letters"),
             Label(self.root, text="Source:")]
        return L

    def setRadioList(self):
        R = [Radiobutton(self.root, text="v<=>w", padx=20, variable=self.x,command=self.setChoice, value=0),
             Radiobutton(self.root, text="w<=>v", padx=20, variable=self.x,command=self.setChoice, value=1),
             Radiobutton(self.root, text="c<=>k", padx=20, variable=self.x,command=self.setChoice, value=2),
             Radiobutton(self.root, text="k<=>c", padx=20, variable=self.x,command=self.setChoice, value=3),
             Radiobutton(self.root, text="j<=>i", padx=20, variable=self.x,command=self.setChoice, value=4),
             Radiobutton(self.root, text="From text area", padx=20, variable=self.y, value=0),
             Radiobutton(self.root, text="From file", padx=20, variable=self.y, value=1),
             Radiobutton(self.root, text="i<=>j", padx=20, variable=self.x,command=self.setChoice, value=5)]
        return R

    def setButtonList(self):
        B = [Button(self.root, text="Code", command=self._hello), Button(self.root, text="Decode", command=self._hello),
             Button(self.root, text="Generate grids", command=self._hello)]
        return B

    def run(self):
        self.scroll_txt_list[0].place(x=450, y=40)
        self.scroll_txt_list[1].place(x=450, y=360)
        self.scroll_txt_list[2].place(x=20, y=316)
        self.txt_list[0].place(x=450, y=280)
        self.txt_list[1].place(x=450, y=320)
        self.label_list[0].place(x=375, y=40)
        self.label_list[1].place(x=402, y=320)
        self.label_list[2].place(x=360, y=280)
        self.label_list[3].place(x=382, y=360)
        self.label_list[4].place(x=20, y=40)
        self.label_list[5].place(x=200, y=40)
        self.radio_list[0].place(x=40, y=70)
        self.radio_list[1].place(x=40, y=100)
        self.radio_list[2].place(x=40, y=130)
        self.radio_list[3].place(x=40, y=160)
        self.radio_list[4].place(x=40, y=190)
        self.radio_list[7].place(x=40, y=220)
        self.radio_list[5].place(x=180, y=70)
        self.radio_list[6].place(x=180, y=100)
        self.button_list[0].place(x=200, y=160)
        self.button_list[1].place(x=200, y=190)
        self.button_list[2].place(x=20, y=280)
