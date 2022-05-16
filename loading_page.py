
from tkinter import *
from tkinter.ttk import Progressbar
import sys
from turtle import width
from threading import Thread
import admin_expl
import script
i=0
def mmain():
    fenetre =Tk()
    fenetre.resizable(0,0)
    height = 470
    width = 660
    x=(fenetre.winfo_screenwidth()//2)-(width//2)
    y=(fenetre.winfo_screenheight()//2)-(height//2)
    fenetre.geometry('{}x{}+{}+{}'.format(width,height,x,y))
    fenetre.wm_attributes('-topmost',True)
    fenetre.overrideredirect(1)
    fenetre.config(background='#000000')
    exit_btn=Button(fenetre,text='X',command=lambda:exit_window(),font=("yu gothic ui",13,'bold'),fg='white',bg='black',bd=0,activebackground='grey')
    exit_btn.place(x=626,y=5)
   #  welcome_label=Label(fenetre,text='Bienvenue dans ARC',font=("yu gothic ui",13,'bold'),fg='white',bg='black')
   #  welcome_label.place(x=250,y=40)
    img=PhotoImage(file='.\\logo_back_remove.gif')
    bg_label=Label(fenetre,image=img,bg='black')
    bg_label.place(x=150,y=80)
    progress_label=Label(fenetre,text='S\'il vous plaît, attendez ... ',font=("yu gothic ui",13,'bold'),fg='white',bg='black')
    progress_label.place(x=210,y=350)
    progress=Progressbar(fenetre,orient=HORIZONTAL,length=625 ,mode='determinate')
    progress.place(x=15,y=390)

    def exit_window():
       sys.exit(fenetre.destroy())
    
    def passage_window():
       fenetre.destroy()
       admin_expl.mainadminempl()
    
    def load():
       global i
       if i <= 10:
        txt='S\'il vous plaît, attendez ... '+(str(10*i)+'%')
        progress_label.config(text=txt)
        progress_label.after(1000,load)
        progress['value']=10*i
        i=i+1
    fenetre.after(10000,passage_window)
       
    load()
    fenetre.mainloop()
# mmain()    
if __name__ == '__main__':
    Thread(target = mmain).start()
    Thread(target = script.script).start()