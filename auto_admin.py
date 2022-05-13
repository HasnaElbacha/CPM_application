from atexit import register
from tkinter import *
from PIL import ImageTk , Image
from tkinter import messagebox as ms
import tkinter as tk
from tkinter import ttk
from click import command
from numpy import place
from tkinter.ttk import Progressbar
import table
import admin_register
import parametre
import exploitants
import mode
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
               table.main_win()
            saisir=Button(label_img,text="Saisir",font=('yu gothic ui' ,20,'bold'),bg='black',fg='#3488FF',width=20,height=1, border=10 ,cursor='hand2',takefocus=0,command=saisire)
            saisir.place(x=290,y=240) 
            comp=False
            saisir.after(1000,changecolor)
            
      else:
            def saisire():
               secondfenetre.destroy()
               table.main_win()
            saisir=Button(label_img,text="Saisir",font=('yu gothic ui' ,20,'bold'),bg='#3488FF',fg='black',width=20,height=1, border=10 ,cursor='hand2',takefocus=0,command=saisire)
            saisir.place(x=290,y=240) 
            comp=True
            saisir.after(1000,changecolor)
   def passregister():
      secondfenetre.destroy()
      admin_register.main_win()
   def passeacc():
      secondfenetre.destroy()
      mode.main_win()
   lien_maison=Image.open('.\\maison_noir.png')
   photo1=ImageTk.PhotoImage(lien_maison)
   icon1=Button(buttons_label,image=photo1,bg='#3488FF', border=2,width=80,height=50,command=passeacc)
   icon1.place(x=10,y=200)
   icon1_lb=Button(buttons_label,text="Acceuil" ,bg='#040405',fg='#3488FF', border=1,width=15,height=1,font=('yu gothic ui',15,'bold'),command=passeacc)
   icon1_lb.place(x=110,y=200)
#********************************************
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
   def passeexp():
      secondfenetre.destroy()
      exploitants.main_win()
   lien_maison=Image.open('.\\expl_grey.png')
   photo4=ImageTk.PhotoImage(lien_maison)
   icon4=Button(buttons_label,image=photo4,bg='#040405', border=2,width=80,height=50,command=passeexp)
   icon4.place(x=10,y=470)
   icon4_lb=Button(buttons_label,text="Exploitants" ,bg='#040405',fg='#E5E4E2', border=1,width=15,height=1,font=('yu gothic ui',15,'bold'),command=passeexp)
   icon4_lb.place(x=110,y=470)
#*******************************************
   user_icon=Image.open('.\\logo_back_remove.gif')
   resize_image = user_icon.resize((170,120))
   photo=ImageTk.PhotoImage(resize_image)
   user_icon_label=Label(buttons_label,image=photo,bg='#040405')
   user_icon_label.image=photo
   user_icon_label.place(x=70,y=580)
#******************************************
   label_img=Label(secondfenetre, bg="white",width=1050,height=33,font=('yu gothic ui',11,'bold'))
   label_img.place(x=320,y=0) 
   tk.Label(label_img, text="Enrgistrement automatique", fg="#3488FF",bg="white" ,font=("Helvetica",25,"bold")).place(x=300, y=5)
   tk.Label(label_img,bg="#3488FF",width=200,height=0).place(x=0, y=70)

   barh=Image.open('.\\bar.png')
   resize_barh = barh.resize((602,2))
   photo_resize_barh=ImageTk.PhotoImage(resize_barh)
   tk.Label(label_img,image=photo_resize_barh,width=602,height=2).place(x=160, y=150)
   tk.Label(label_img,image=photo_resize_barh,width=602,height=2).place(x=160, y=200)
   barw=Image.open('.\\bar.png')
   resize_barw = barw.resize((2,450))
   photo_resize_barw=ImageTk.PhotoImage(resize_barw)  
   tk.Label(label_img,image=photo_resize_barw,width=2,height=450).place(x=160, y=150)
   tk.Label(label_img,image=photo_resize_barw,width=2,height=450).place(x=160, y=150) 
#******************************************
   tt="ARC_2022"
   label_bar=Label(secondfenetre,text=tt,bg="black",fg="grey",width=140,height=2,font=('yu gothic ui',11,'bold'))
   label_bar.place(x=260,y=660)
#****************************************
 
   secondfenetre.mainloop()
main_win()