from atexit import register
from tkinter import *
from PIL import ImageTk , Image
from tkinter import messagebox as ms
import tkinter as tk
from tkinter import ttk
from click import command
from numpy import place
from tkinter.ttk import Progressbar
import exp_table
import admin_register
import exp_mode
import exp_exploitants
comp=True
def main_win():
   
   secondfenetre =Tk()
   secondfenetre.state("zoomed")
   secondfenetre.config(background="#FFFFFF")
   buttons_label = Label(secondfenetre, bg="black" ,height=237,width=45)
   buttons_label.place(x=0,y=0)

   #***************************************
   user_icon=Image.open('.\\compte_.png')
   resize_image = user_icon.resize((40,40))
   photo=ImageTk.PhotoImage(resize_image)
   user_icon_label=Label(buttons_label,image=photo,bg='#040405')
   user_icon_label.image=photo
   user_icon_label.place(x=50,y=50)
   txt="Admin"
   compte=Label(secondfenetre,text=txt,bg="black",fg="grey",width=14,height=1,font=('yu gothic ui',16,'bold'))
   compte.place(x=95,y=55)
  
#********************************************
   
   def changecolor():
      global comp
      if(comp==True):
            def saisire():
               secondfenetre.destroy()
               exp_table.main_win()
            saisir=Button(label_img,text="Saisir",font=('yu gothic ui' ,20,'bold'),bg='black',fg='#3488FF',width=20,height=1, border=10 ,cursor='hand2',takefocus=0,command=saisire)
            saisir.place(x=290,y=240) 
            comp=False
            saisir.after(1000,changecolor)
            
      else:
            def saisire():
               secondfenetre.destroy()
               exp_table.main_win()
            saisir=Button(label_img,text="Saisir",font=('yu gothic ui' ,20,'bold'),bg='#3488FF',fg='black',width=20,height=1, border=10 ,cursor='hand2',takefocus=0,command=saisire)
            saisir.place(x=290,y=240) 
            comp=True
            saisir.after(1000,changecolor)
   def passregister():
      secondfenetre.destroy()
      admin_register.main_win()
   def passeacc():
      secondfenetre.destroy()
      exp_mode.main_win()
   lien_maison=Image.open('.\\maison_noir.png')
   photo1=ImageTk.PhotoImage(lien_maison)
   icon1=Button(buttons_label,image=photo1,bg='#3488FF', border=2,width=80,height=50,command=passeacc)
   icon1.place(x=10,y=270)
   icon1_lb=Button(buttons_label,text="Acceuil" ,bg='#040405',fg='#3488FF', border=1,width=15,height=1,font=('yu gothic ui',15,'bold'),command=passeacc)
   icon1_lb.place(x=110,y=270)
#*******************************************
   def passeexp():
      secondfenetre.destroy()
      exp_exploitants.main_win()
   lien_maison=Image.open('.\\expl_grey.png')
   photo4=ImageTk.PhotoImage(lien_maison)
   icon4=Button(buttons_label,image=photo4,bg='#040405', border=2,width=80,height=50,command=passeexp)
   icon4.place(x=10,y=360)
   icon4_lb=Button(buttons_label,text="Exploitants" ,bg='#040405',fg='#E5E4E2', border=1,width=15,height=1,font=('yu gothic ui',15,'bold'),command=passeexp)
   icon4_lb.place(x=110,y=360)
#*******************************************
   user_icon=Image.open('.\\logo_back_remove.gif')
   resize_image = user_icon.resize((170,120))
   photo=ImageTk.PhotoImage(resize_image)
   user_icon_label=Label(buttons_label,image=photo,bg='#040405')
   user_icon_label.image=photo
   user_icon_label.place(x=70,y=580)
#******************************************
   tt="ARC_2022"
   label_bar=Label(secondfenetre,text=tt,bg="black",fg="grey",width=140,height=2,font=('yu gothic ui',11,'bold'))
   label_bar.place(x=260,y=660)
#****************************************
   label_img=Label(secondfenetre,bg="white",width=1050,height=33,font=('yu gothic ui',11,'bold'))
   label_img.place(x=320,y=0)  
   secondfenetre.mainloop()
# main_win()