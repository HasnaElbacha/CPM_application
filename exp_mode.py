
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
import admin_expl
import exp_login_name
import exp_exploitants
import auto_exp
import table
from  admin_login_name import mainlogin_name
comp=True
user=" "
#Username
def main_win(Username):
   global user
   secondfenetre =Tk()
   secondfenetre.iconbitmap('lo.ico')
   secondfenetre.title('ARC')
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
   user_icon_label.place(x=45,y=110)
   txt=Username
   # txt="Hasna Elbacha"
   compte=Label(secondfenetre,text=txt,bg="black",fg="grey",width=14,height=1,font=('yu gothic ui',16,'bold'))
   compte.place(x=90,y=115)
#*******************************************
   cpu=Image.open('.\\bac1.png')
   resize_cpu = cpu.resize((1070,690))
   photocpu=ImageTk.PhotoImage(resize_cpu)
   label_img=Label(secondfenetre,image=photocpu,bg="white",width=1070,height=690,font=('yu gothic ui',11,'bold'))
   label_img.place(x=300,y=-5) 
#********************************************
   def manuel():
       secondfenetre.destroy()
       exp_table.main_win(Username)
   def automatic():
       secondfenetre.destroy()
       auto_exp.main_win(Username)
   mode_manuel=Button(label_img,text="Mode manuel",font=('yu gothic ui' ,17,'bold'),bg='#e1a451',fg='white',width=27,height=2, border=0 ,cursor='hand2',takefocus=3,command=manuel)
   mode_manuel.place(x=360,y=240) 
   mode_automatique=Button(label_img,text="Mode automatique",font=('yu gothic ui' ,17,'bold'),bg='white',fg='#170f61',width=27,height=2, border=0,cursor='hand2',takefocus=3,command=automatic)
   mode_automatique.place(x=360,y=360)
   lien_maison=Image.open('.\\maison_noir.png')
   photo1=ImageTk.PhotoImage(lien_maison)
   def passehome():
      secondfenetre.destroy()
      exp_table.main_win(Username)
   icon1=Button(buttons_label,image=photo1,bg='#3488FF', border=2,width=80,height=50)
   icon1.place(x=10,y=270)
   icon1_lb=Button(buttons_label,text="Acceuil" ,bg='#040405',fg='#3488FF', border=1,width=15,height=1,font=('yu gothic ui',15,'bold'))
   icon1_lb.place(x=110,y=270)

#*******************************************
   def passexp():
      secondfenetre.destroy()
      exp_exploitants.main_win(Username)
   lien_maison=Image.open('.\\expl_grey.png')
   photo4=ImageTk.PhotoImage(lien_maison)
   icon4=Button(buttons_label,image=photo4,bg='#040405', border=2,width=80,height=50,command=passexp)
   icon4.place(x=10,y=360)
   icon4_lb=Button(buttons_label,text="Exploitants" ,bg='#040405',fg='#E5E4E2', border=1,width=15,height=1,font=('yu gothic ui',15,'bold'),command=passexp)
   icon4_lb.place(x=110,y=360)
#*******************************************
   user_icon=Image.open('.\\logo_back_remove.gif')
   resize_image = user_icon.resize((190,150))
   photo=ImageTk.PhotoImage(resize_image)
   user_icon_label=Label(buttons_label,image=photo,bg='#040405')
   user_icon_label.image=photo
   user_icon_label.place(x=50,y=500)
#******************************************
   tt="ARC_2022"
   label_bar=Label(secondfenetre,text=tt,bg="black",fg="grey",width=140,height=2,font=('yu gothic ui',11,'bold'))
   label_bar.place(x=260,y=660)
#****************************************
   def retour_acceuil():
      secondfenetre.destroy()
      admin_expl.mainadminempl()
   btn_flechem=Image.open('.\\play.png')
   resize_btn_flechem = btn_flechem.resize((30,30))
   photo_flechem=ImageTk.PhotoImage(resize_btn_flechem)
   loginm=Button(buttons_label,image=photo_flechem,width=30,height=30,bd=0,bg='black',cursor='hand2',activebackground='#e2bc74',command=retour_acceuil)
   loginm.place(x=5,y=20)
   secondfenetre.mainloop()
# main_win()