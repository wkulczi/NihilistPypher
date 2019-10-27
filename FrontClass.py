from tkinter import *
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
import BackClass
from Util import isdefined


class Front:
    def cipher(self):
        text = self.scroll_txt_list[0].get('1.0', END).strip()
        key = self.txt_list[1].get('1.0', END).strip()
        matrixword = self.txt_list[0].get('1.0', END).strip()
        filepath = ""
        if self.choice_source==1:
            self.scroll_txt_list[1].configure(state="normal")
            self.scroll_txt_list[0].configure(state="normal")
        if isdefined(key) and (isdefined(text) or isdefined(filepath)):
            wynik=self.backbone.cipher(key,matrixword,text)
            self.scroll_txt_list[1].configure(state="normal")
            self.scroll_txt_list[1].delete('1.0',END)
            self.scroll_txt_list[1].insert(END, wynik)
            self.scroll_txt_list[1].configure(state="disabled")
        else:
            if not isdefined(key):
                self.txt_list[1].insert('1.0',"KEY MISSING, INSERT KEY")
            if not isdefined(text):
                self.scroll_txt_list[0].insert('1.0', "INSERT WORD TO CIPHER")
    def decipher(self):
        text = self.scroll_txt_list[0].get('1.0', END).strip()
        key = self.txt_list[1].get('1.0', END).strip()
        matrixword = self.txt_list[0].get('1.0', END).strip()
        filepath = ""
        if isdefined(key) and (isdefined(text) or isdefined(filepath)):
            wynik=self.backbone.decipher(key,text,matrixword)
            self.scroll_txt_list[1].configure(state="normal")
            self.scroll_txt_list[1].delete('1.0',END)
            self.scroll_txt_list[1].insert(END, wynik)
            self.scroll_txt_list[1].configure(state="disabled")

    def setChoiceSource(self):  # 0=text 1=file
        self.choice_source = self.y.get()
        self.backbone.setFromfile(self.choice_source)
        if self.choice_source==1:
            self.scroll_txt_list[0].configure(state="normal")
            self.scroll_txt_list[0].delete('1.0',END)
            self.scroll_txt_list[0].insert(END, "Set file path.")
            self.scroll_txt_list[1].configure(state="disabled")
            self.scroll_txt_list[0].configure(state="disabled")
        else:
            self.scroll_txt_list[1].configure(state="normal")
            self.scroll_txt_list[0].configure(state="normal")
    def clearall(self):
        self.scroll_txt_list[0].configure(state="normal")
        self.scroll_txt_list[0].delete('1.0',END)
        self.scroll_txt_list[1].configure(state="normal")
        self.scroll_txt_list[1].delete('1.0',END)
        self.scroll_txt_list[2].configure(state="normal")
        self.scroll_txt_list[2].delete('1.0',END)
        self.scroll_txt_list[1].configure(state="disabled")
        self.scroll_txt_list[2].configure(state="disabled")
        self.txt_list[0].delete('1.0',END)
        self.txt_list[1].delete('1.0',END)
    def setChoiceSub(self):
        self.choice_sub = self.choice_list[self.x.get()]
        self.backbone.setSubstitute(self.choice_sub)
    def generategrids(self):
        if isdefined(self.backbone.matrix_parsed):
            self.scroll_txt_list[2].configure(state="normal")
            self.scroll_txt_list[2].delete('1.0', END)
            self.scroll_txt_list[2].insert(END, self.backbone.matrix_parsed)
            self.scroll_txt_list[2].insert(END, "\n TRANSLATED WORD: \n ")
            self.scroll_txt_list[2].insert(END, self.backbone.cyphered_word)
            self.scroll_txt_list[2].insert(END, "\n TRANSLATED KEY: \n ")
            self.scroll_txt_list[2].insert(END, self.backbone.cyphered_key)
            self.scroll_txt_list[2].configure(state="disabled")

        else:
            self.scroll_txt_list[2].configure(state="normal")
            self.scroll_txt_list[2].delete('1.0', END)
            if not isdefined(self.txt_list[1].get('1.0', END).strip()) and not isdefined(self.scroll_txt_list[0].get('1.0', END).strip()):
                self.scroll_txt_list[2].insert(END, "NO GRIDS FOUND. INSERT KEY AND WORDS TO CIPHER.")
            elif not isdefined(self.scroll_txt_list[0].get('1.0', END).strip()):
                self.scroll_txt_list[2].insert(END, "NO GRIDS FOUND. INSERT WORDS TO CIPHER.")
            elif not isdefined(self.txt_list[1].get('1.0', END).strip()):
                self.scroll_txt_list[2].insert(END, "NO GRIDS FOUND. INSERT KEY.")
            else:
                self.scroll_txt_list[2].insert(END, "PRESS CYPHER/DECYPHER BUTTON FIRST.")
            self.scroll_txt_list[2].configure(state="disabled")

    def setfilepath(self):
        if self.choice_source==1:
            self.filepath=filedialog.askopenfilename(initialdir="/", title="Select file to cipher", filetypes= (("txt files","*.txt"),("all files","*.*")))
            try:
                file=open(self.filepath,"r")
                fromfile=file.read()
                self.scroll_txt_list[0].configure(state="normal")
                self.scroll_txt_list[0].delete('1.0', END)
                self.scroll_txt_list[0].insert('1.0', fromfile)
                self.scroll_txt_list[0].configure(state="disabled")
            except:
                self.scroll_txt_list[0].configure(state="normal")
                self.scroll_txt_list[0].delete('1.0', END)
                self.scroll_txt_list[0].insert('1.0', "NO FILE AT: \""+self.filepath+"\" FOUND.")
                self.scroll_txt_list[0].configure(state="disabled")
        else:
            self.scroll_txt_list[0].configure(state="normal")
            self.scroll_txt_list[0].delete('1.0', END)
            self.scroll_txt_list[0].insert('1.0', "Change to \"From file\" first")
            self.scroll_txt_list[0].configure(state="disabled")
    def savetofile(self):
        self.scroll_txt_list[1].configure(state="normal")
        cypheredmatrix=self.scroll_txt_list[1].get('1.0', END).strip()
        if isdefined(cypheredmatrix):
            self.savefilepath=filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("txt files",".txt"),("all files","*.*")))
            self.savefilepath=self.savefilepath+".txt"
            savefile=open(self.savefilepath,"w+")
            savefile.write(cypheredmatrix)
        else:
            self.scroll_txt_list[1].insert('1.0',"NO CYPHERED TEXT FOUND.")
        self.scroll_txt_list[1].configure(state="disabled")
    def __init__(self):
        self.filepath=""
        self.root = Tk()
        self.root.title("NihilistPypher")
        self.root.geometry("900x600+200+200")
        self.root.geometry("900x600+200+200")
        self.root.resizable(FALSE, FALSE)
        self.x = IntVar()
        self.y = IntVar()
        self.str = ""
        self.choice_list = [("v", "w"), ("w", "v"), ("c", "k"), ("k", "c"), ("j", "i"), ("i", "j")]
        self.button_list = self.setButtonList()
        self.scroll_txt_list = self.setSTxtList()
        self.txt_list = self.setTxtList()
        self.label_list = self.setLabelList()
        self.radio_list = self.setRadioList()
        self.choice_sub = []
        self.choice_source = int()
        self.backbone = BackClass.Back()

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
             Label(self.root, text="Source")]
        return L

    def setRadioList(self):
        R = [Radiobutton(self.root, text="v<=>w", padx=20, variable=self.x, command=self.setChoiceSub, value=0),
             Radiobutton(self.root, text="w<=>v", padx=20, variable=self.x, command=self.setChoiceSub, value=1),
             Radiobutton(self.root, text="c<=>k", padx=20, variable=self.x, command=self.setChoiceSub, value=2),
             Radiobutton(self.root, text="k<=>c", padx=20, variable=self.x, command=self.setChoiceSub, value=3),
             Radiobutton(self.root, text="j<=>i", padx=20, variable=self.x, command=self.setChoiceSub, value=4),
             Radiobutton(self.root, text="From text area", padx=20, variable=self.y, command=self.setChoiceSource,
                         value=0),
             Radiobutton(self.root, text="From file", padx=20, variable=self.y, command=self.setChoiceSource, value=1),
             Radiobutton(self.root, text="i<=>j", padx=20, variable=self.x, command=self.setChoiceSub, value=5)]
        return R

    def setButtonList(self):
        B = [Button(self.root, text="Code", command=self.cipher),
             Button(self.root, text="Decode", command=self.decipher),
             Button(self.root, text="Generate grids", command=self.generategrids),
             Button(self.root, text="Import file", command=self.setfilepath),
             Button(self.root, text="Export to file", command=self.savetofile),
             Button(self.root, text="Clear all containers", command=self.clearall)]
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
        self.button_list[3].place(x=364, y=100)
        self.button_list[4].place(x=360, y=420)
        self.button_list[5].place(x=320, y=200)
