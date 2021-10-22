import pyperclip
from tkinter import *
tk = Tk()
nulklein = "₀"
eenklein = "₁"
tweeklein = "₂"
drieklein = "₃"
vierklein = "₄"
vijfklein = "₅"
zesklein = "₆"
zevenklein = "₇"
achtklein = "₈"
negenklein = "₉"
nulgroot = "⁰"
eengroot = "¹"
tweegroot = "²"
driegroot = "³"
viergroot = "⁴"
vijfgroot = "⁵"
zesgroot = "⁶"
zevengroot = "⁷"
achtgroot = "⁸"
negengroot = "⁹"
posklein = "₊"
negklein = "₋"
posgroot = "⁺"
neggroot = "⁻"
def copynulklein():
    pyperclip.copy(nulklein)
def copyeenklein():
    pyperclip.copy(eenklein) 
def copytweeklein():
    pyperclip.copy(tweeklein)
def copydrieklein():
    pyperclip.copy(drieklein)
def copyvierklein():
    pyperclip.copy(vierklein)
def copyvijfklein():
    pyperclip.copy(vijfklein)
def copyzesklein():
    pyperclip.copy(zesklein) 
def copyzevenklein():
    pyperclip.copy(zevenklein)
def copyachtklein():
    pyperclip.copy(achtklein)
def copynegenklein():
    pyperclip.copy(negenklein)
def copyposklein():
    pyperclip.copy(posklein)
def copynegklein():
    pyperclip.copy(negklein) 
def copynulgroot():
    pyperclip.copy(nulgroot) 
def copyeengroot():
    pyperclip.copy(eengroot) 
def copytweegroot():
    pyperclip.copy(tweegroot)
def copydriegroot():
    pyperclip.copy(driegroot)
def copyviergroot():
    pyperclip.copy(viergroot)
def copyvijfgroot():
    pyperclip.copy(vijfgroot)
def copyzesgroot():
    pyperclip.copy(zesgroot) 
def copyzevengroot():
    pyperclip.copy(zevengroot)
def copyachtgroot():
    pyperclip.copy(achtgroot)
def copynegengroot():
    pyperclip.copy(negengroot)
def copyposgroot():
    pyperclip.copy(posgroot) 
def copyneggroot():
    pyperclip.copy(neggroot) 
b1 = Button(tk, text="₀", highlightbackground='#3E4149', command= copynulklein )
b2 = Button(tk, text="₁", highlightbackground='#3E4149', command= copyeenklein )
b3 = Button(tk, text="₂", highlightbackground='#3E4149', command= copytweeklein )
b4 = Button(tk, text="₃", highlightbackground='#3E4149', command= copydrieklein )
b5 = Button(tk, text="₄", highlightbackground='#3E4149', command= copyvierklein )
b6 = Button(tk, text="₅", highlightbackground='#3E4149', command= copyvijfklein )
b7 = Button(tk, text="₆", highlightbackground='#3E4149', command= copyzesklein )
b8 = Button(tk, text="₇", highlightbackground='#3E4149', command= copyzevenklein )
b9 = Button(tk, text="₈", highlightbackground='#3E4149', command= copyachtklein )
b10 = Button(tk, text="₉", highlightbackground='#3E4149', command= copynegenklein )
b11 = Button(tk, text="₊", highlightbackground='#3E4149', command= copyposklein )
b12 = Button(tk, text="₋", highlightbackground='#3E4149', command= copynegklein )
b13 = Button(tk, text="⁰", highlightbackground='#3E4149', command= copynulgroot )
b14 = Button(tk, text="¹", highlightbackground='#3E4149', command= copyeengroot )
b15 = Button(tk, text="²", highlightbackground='#3E4149', command= copytweegroot )
b16 = Button(tk, text="³", highlightbackground='#3E4149', command= copydriegroot )
b17 = Button(tk, text="⁴", highlightbackground='#3E4149', command= copyviergroot )
b18 = Button(tk, text="⁵", highlightbackground='#3E4149', command= copyvijfgroot )
b19 = Button(tk, text="⁶", highlightbackground='#3E4149', command= copyzesgroot )
b20 = Button(tk, text="⁷", highlightbackground='#3E4149', command= copyzevengroot )
b21 = Button(tk, text="⁸", highlightbackground='#3E4149', command= copyachtgroot )
b22 = Button(tk, text="⁹", highlightbackground='#3E4149', command= copynegengroot )
b23 = Button(tk, text="⁺", highlightbackground='#3E4149', command= copyposgroot )
b24 = Button(tk, text="⁻", highlightbackground='#3E4149', command= copyneggroot )
b1.place(x=50, y=50)
b2.place(x=100, y=50)
b3.place(x=150, y=50)
b4.place(x=200, y=50)
b5.place(x=250, y=50)
b6.place(x=300, y=50)
b7.place(x=350, y=50)
b8.place(x=400, y=50)
b9.place(x=450, y=50)
b10.place(x=500, y=50)
b11.place(x=50, y=100)
b12.place(x=100, y=100)
b13.place(x=50, y=150)
b14.place(x=100, y=150)
b15.place(x=150, y=150)
b16.place(x=200, y=150)
b17.place(x=250, y=150)
b18.place(x=300, y=150)
b19.place(x=350, y=150)
b20.place(x=400, y=150)
b21.place(x=450, y=150)
b22.place(x=500, y=150)
b23.place(x=50, y=200)
b24.place(x=100, y=200)
tk.title("UCC")
tk.geometry("600x300")
tk.mainloop()