from tkinter import *
root = Tk()
root.title('Title')
root.geometry('200x100')  # Use 'x' Not '*'
root.resizable(width=False, height=True)
l = Label(root, text='Label', bg='red', font=('Arial', 12), width=5, height=2)
l.pack(side=TOP)
frm = Frame(root)
# Left
frm_L = Frame(frm)
Label(frm_L, text='Label', bg='green', font=(
    'Arial', 12), width=5, height=2).pack()
frm_L.pack(side=LEFT)
# Right
frm_R = Frame(frm)
Label(frm_R, text='Label', bg='green', font=(
    'Arial', 12), width=5, height=2).pack()
frm_R.pack(side=RIGHT)
frm.pack()
root.mainloop()
