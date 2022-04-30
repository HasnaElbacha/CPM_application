
from tkinter import *
from tkinter.ttk import Progressbar
import sys
from turtle import width
import acceuil
fenetre =Tk()
fenetre.resizable(0,0)
height = 430
width = 530
x=(fenetre.winfo_screenwidth()//2)-(width//2)
y=(fenetre.winfo_screenheight()//2)-(height//2)
fenetre.geometry('{}x{}+{}+{}'.format(width,height,x,y))
fenetre.wm_attributes('-topmost',True)
fenetre.overrideredirect(1)
fenetre.config(background='#000000')
exit_btn=Button(fenetre,text='X',command=lambda:exit_window(),font=("yu gothic ui",13,'bold'),fg='white',bg='black',bd=0,activebackground='grey')
exit_btn.place(x=510,y=0)
welcome_label=Label(fenetre,text='Bienvenue dans ARC',font=("yu gothic ui",13,'bold'),fg='white',bg='black')
welcome_label.place(x=170,y=40)
img=PhotoImage(file='.\\logo_back_remove.gif')
bg_label=Label(fenetre,image=img,bg='black')
bg_label.place(x=80,y=110)
progress_label=Label(fenetre,text='S\'il vous plaît, attendez ... ',font=("yu gothic ui",13,'bold'),fg='white',bg='black')
progress_label.place(x=150,y=350)
progress=Progressbar(fenetre,orient=HORIZONTAL,length=500,mode='determinate')
progress.place(x=15,y=390)

def exit_window():
    sys.exit(fenetre.destroy())

def passage_window():
    fenetre.destroy()
    acceuil.main_home()

i=0
def load():
    global i
    if i <= 10:
        txt='S\'il vous plaît, attendez ...'+(str(10*i)+'%')
        progress_label.config(text=txt)
        progress_label.after(1000,load)
        progress['value']=10*i
        i=i+1
        
fenetre.after(10000,passage_window)
       
load()
fenetre.mainloop()