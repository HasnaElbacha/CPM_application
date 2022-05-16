from lll import ggg
from tkinter import *
fenetre =Tk()
fenetre.resizable(0,0)
height = 470
width = 660
x=(fenetre.winfo_screenwidth()//2)-(width//2)
y=(fenetre.winfo_screenheight()//2)-(height//2)
fenetre.geometry('{}x{}+{}+{}'.format(width,height,x,y))
fenetre.wm_attributes('-topmost',True)
fenetre.overrideredirect(1)
fenetre.config(background='#FFFFFF')
loginn_icon_label=Label(fenetre,text=ggg(),bg='#FFFFFF')
loginn_icon_label.place(x=50,y=50)
fenetre.mainloop()