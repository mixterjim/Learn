from tkinter import *


class Frame0(object):

    def __init__(self):
        self.root = Tk()
        self.root.title('Title')
        self.root.geometry('200x250')
        self.root.resizable(width=False, height=True)
        self.Label_T = Label(self.root, text='Label', bg='red', font=('Arial', 12), width=5, height=2)
        self.Label_T.pack(side=TOP)
        # Frame Start
        self.frm = Frame(self.root)
        # Left Frame
        self.frm_L = Frame(self.frm)
        self.Label_L = Label(self.frm_L, text='Label', bg='green', font=('Arial', 12), width=5, height=2)
        self.Label_L.pack()
        self.frm_L.pack(side=LEFT)
        # Right Frame
        self.frm_R = Frame(self.frm)
        self.Label_R = Label(self.frm_R, text='Label', bg='green', font=('Arial', 12), width=5, height=2)
        self.Label_R.pack()
        self.frm_R.pack(side=RIGHT)
        self.frm.pack()
        # Frame End
        self.txt = Text(self.root, width=30, height=10)
        self.txt.pack()
        self.button = Button(self.root, text='Button', command=self.insert)
        self.button.pack()

    def insert(self):
        self.txt.insert(INSERT, 'INSERT\n')
if __name__ == '__main__':
    d = Frame0()
    d.root.mainloop()
