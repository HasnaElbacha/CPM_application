
from tkinter import *
from tkinter.ttk import Progressbar
import sys
from turtle import width
from PIL import ImageTk , Image
import mode
import admin_login_name
import exp_login_name
def mainadminempl():
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
   def exit_window():
     sys.exit(fenetre.destroy())
    
   img=PhotoImage(file='.\\logo_back_remove.gif')
   bg_label=Label(fenetre,image=img,bg='black')
   bg_label.place(x=150,y=30)  
   exit_btn=Button(fenetre,text='X',command=lambda:exit_window(),font=("yu gothic ui",13,'bold'),fg='white',bg='black',bd=0,activebackground='grey')
   exit_btn.place(x=626,y=0)
   def home():
       fenetre.destroy()
       admin_login_name.mainlogin_name()
   def homee():
       fenetre.destroy()
       exp_login_name.mainlogin_name()
   btn_admin=Image.open('.\\adminblue.png')
   resize_btn_admin = btn_admin.resize((90,100))
   photo_admin=ImageTk.PhotoImage(resize_btn_admin)
   loginad=Button(fenetre,image=photo_admin, font=('yu gothic ui',13,'bold'),width=90,height=100,bd=0,bg='#040405',cursor='hand2',activebackground='#040405',command=home)
   loginad.place(x=150,y=240)
   headingad=Button(fenetre,text='Admin',font=('yu gothic ui' ,15,'italic'),bg='#040405',fg='white', border=0 ,cursor='hand2',takefocus=0,command=home)
   headingad.place(x=150,y=350)

   btn_empl=Image.open('.\\employeeblue.png')
   resize_btn_empl = btn_empl.resize((90,100))
   photo_empl=ImageTk.PhotoImage(resize_btn_empl)
   loginem=Button(fenetre,image=photo_empl, font=('yu gothic ui',13,'bold'),width=90,height=100,bd=0,bg='#040405',cursor='hand2',activebackground='#040405',command=homee)
   loginem.place(x=400,y=240)
   headingem=Button(fenetre,text='Employées',font=('yu gothic ui' ,15,'italic'),bg='#040405',fg='white', border=0 ,cursor='hand2',takefocus=0,command=homee)
   headingem.place(x=395,y=350)
   fenetre.mainloop()

# mainadminempl()