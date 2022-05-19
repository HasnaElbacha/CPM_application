from tkinter import *
from PIL import ImageTk , Image
from tkinter import messagebox as ms
import tkinter as tk
from tkinter import ttk
from click import command
from numpy import place
from tkinter.ttk import Progressbar
import home_win_admin
import admin_register
import admin_expl
import parametre
import exploitants
import auto_admin
import auto_admin
# import script
import table
comp=True
def main_win():
   secondfenetre =Tk()
   secondfenetre.iconbitmap('lo.ico')
   secondfenetre.title('ARC')
   secondfenetre.state("zoomed")
   # secondfenetre.config(background="#FFFFFF")
   buttons_label = Label(secondfenetre, bg="black" ,height=237,width=45)
   buttons_label.place(x=0,y=0)

   #***************************************
   user_icon=Image.open('.\\compte_.png')
   resize_image = user_icon.resize((40,40))
   photo=ImageTk.PhotoImage(resize_image)
   user_icon_label=Label(buttons_label,image=photo,bg='#040405')
   user_icon_label.image=photo
   user_icon_label.place(x=70,y=70)
   txt="Admin"
   compte=Label(secondfenetre,text=txt,bg="black",fg="grey",width=6,height=1,font=('yu gothic ui',16,'bold'))
   compte.place(x=120,y=75)
#*******************************************
   cpu=Image.open('.\\bac1.png')
   resize_cpu = cpu.resize((1070,690))
   photocpu=ImageTk.PhotoImage(resize_cpu)
   label_img=Label(secondfenetre,image=photocpu,bg="white",width=1070,height=690,font=('yu gothic ui',11,'bold'))
   label_img.place(x=320,y=-5) 
   plan1=Label(label_img,image=photocpu,bg="white",width=1070,height=690,font=('yu gothic ui',11,'bold'))
   plan1.place(x=-10,y=-5) 
#********************************************
   def manuel():
       secondfenetre.destroy()
       table.main_win()
   def automatic():
       secondfenetre.destroy()
       auto_admin.main_win()
   mode_manuel=Button(plan1,text="Mode manuel",font=('yu gothic ui' ,17,'bold'),bg='#e1a451',fg='white',width=27,height=2, border=0 ,cursor='hand2',takefocus=3,command=manuel)
   mode_manuel.place(x=360,y=240) 
   mode_automatique=Button(plan1,text="Mode automatique",font=('yu gothic ui' ,17,'bold'),bg='white',fg='#170f61',width=27,height=2, border=0,cursor='hand2',takefocus=3,command=automatic)
   mode_automatique.place(x=360,y=360)
   lien_maison=Image.open('.\\maison_noir.png')
   photo1=ImageTk.PhotoImage(lien_maison)
   def passehome():
      secondfenetre.destroy()
      home_win_admin.main_win()
   icon1=Button(buttons_label,image=photo1,bg='#3488FF', border=2,width=80,height=50)
   icon1.place(x=10,y=200)
   icon1_lb=Button(buttons_label,text="Acceuil" ,bg='#040405',fg='#3488FF', border=1,width=15,height=1,font=('yu gothic ui',15,'bold'))
   icon1_lb.place(x=110,y=200)
#********************************************
   def passregister():
      secondfenetre.destroy()
      admin_register.main_win()
   lien_maison=Image.open('.\\register_grey.png')
   photo2=ImageTk.PhotoImage(lien_maison)
   icon2=Button(buttons_label,image=photo2,bg='#040405', border=2,width=80,height=50,command=passregister)
   icon2.place(x=10,y=290)
   icon2_lb=Button(buttons_label,text="Enregistrer" ,bg='#040405',fg='#E5E4E2', border=1,width=15,height=1,font=('yu gothic ui',15,'bold'),command=passregister)
   icon2_lb.place(x=110,y=290)

#********************************************
   def passepara():
      secondfenetre.destroy()
      parametre.main_win()
   lien_maison=Image.open('.\\parametre_grey.png')
   photo3=ImageTk.PhotoImage(lien_maison)
   icon3=Button(buttons_label,image=photo3,bg='#040405', border=2,width=80,height=50,command=passepara)
   icon3.place(x=10,y=380)
   icon3_lb=Button(buttons_label,text="Paramètre" ,bg='#040405',fg='#E5E4E2', border=1,width=15,height=1,font=('yu gothic ui',15,'bold'),command=passepara)
   icon3_lb.place(x=110,y=380)
   
#*******************************************
   def passexp():
      secondfenetre.destroy()
      exploitants.main_win()
   lien_maison=Image.open('.\\expl_grey.png')
   photo4=ImageTk.PhotoImage(lien_maison)
   icon4=Button(buttons_label,image=photo4,bg='#040405', border=2,width=80,height=50,command=passexp)
   icon4.place(x=10,y=470)
   icon4_lb=Button(buttons_label,text="Exploitants" ,bg='#040405',fg='#E5E4E2', border=1,width=15,height=1,font=('yu gothic ui',15,'bold'),command=passexp)
   icon4_lb.place(x=110,y=470)
#*******************************************
   user_icon=Image.open('.\\logo_back_remove.gif')
   resize_image = user_icon.resize((170,120))
   photo=ImageTk.PhotoImage(resize_image)
   user_icon_label=Label(buttons_label,image=photo,bg='#040405')
   user_icon_label.image=photo
   user_icon_label.place(x=50,y=580)
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
   loginm.place(x=5,y=10)
   secondfenetre.mainloop()
# main_win()