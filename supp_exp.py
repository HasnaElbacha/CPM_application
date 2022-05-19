from tkinter import *
from PIL import ImageTk , Image
from tkinter import messagebox as ms
import tkinter as tk
from tkinter import ttk
from click import command
from numpy import place
from tkinter.ttk import Progressbar
import table
import sqlite3
from tkinter import messagebox
import admin_register
# import admin_register
import mode
import exploitants
import home_win_admin

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
   user_icon_label.place(x=70,y=70)
   txt="Admin"
   compte=Label(secondfenetre,text=txt,bg="black",fg="grey",width=6,height=1,font=('yu gothic ui',16,'bold'))
   compte.place(x=120,y=75)
  
#********************************************
   def passregister():
      secondfenetre.destroy()
      admin_register.main_win()
   def passacceuil():
       secondfenetre.destroy()
       mode.main_win()
   lien_maison=Image.open('.\\maison_noir.png')
   photo1=ImageTk.PhotoImage(lien_maison)
   icon1=Button(buttons_label,image=photo1,bg='#3488FF', border=2,width=80,height=50,command=passacceuil)
   icon1.place(x=10,y=200)
   icon1_lb=Button(buttons_label,text="Acceuil" ,bg='#040405',fg='#3488FF', border=1,width=15,height=1,font=('yu gothic ui',15,'bold'),command=passacceuil)
   icon1_lb.place(x=110,y=200)
#********************************************
   lien_maison=Image.open('.\\register_grey.png')
   photo2=ImageTk.PhotoImage(lien_maison)
   icon2=Button(buttons_label,image=photo2,bg='#040405', border=2,width=80,height=50,command=passregister)
   icon2.place(x=10,y=290)
   def passregister():
      secondfenetre.destroy()
      admin_register.main_win()
   icon2_lb=Button(buttons_label,text="Enregistrer" ,bg='#040405',fg='#E5E4E2', border=1,width=15,height=1,font=('yu gothic ui',15,'bold'),command=passregister)
   icon2_lb.place(x=110,y=290)

#********************************************
   lien_maison=Image.open('.\\parametre_grey.png')
   photo3=ImageTk.PhotoImage(lien_maison)
   icon3=Button(buttons_label,image=photo3,bg='#040405', border=2,width=80,height=50)
   icon3.place(x=10,y=380)
   icon3_lb=Button(buttons_label,text="Paramètre" ,bg='#040405',fg='#E5E4E2', border=1,width=15,height=1,font=('yu gothic ui',15,'bold'))
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
   user_icon_label.place(x=50,y=580)
#******************************************
   tt="ARC_2022"
   label_bar=Label(secondfenetre,text=tt,bg="black",fg="grey",width=140,height=2,font=('yu gothic ui',11,'bold'))
   label_bar.place(x=260,y=660)
#****************************************
   label_img=Label(secondfenetre, bg="white",width=1050,height=33,font=('yu gothic ui',11,'bold'))
   label_img.place(x=320,y=0) 
   def retour_acceuil():
      secondfenetre.destroy()
      exploitants.main_win()
   label_img=Label(secondfenetre, bg="white",width=1050,height=33,font=('yu gothic ui',11,'bold'))
   label_img.place(x=320,y=0)  
   btn_flechem=Image.open('.\\play.png')
   resize_btn_flechem = btn_flechem.resize((30,30))
   photo_flechem=ImageTk.PhotoImage(resize_btn_flechem)
   loginm=Button(buttons_label,image=photo_flechem,width=30,height=30,bd=0,bg='black',cursor='hand2',activebackground='#e2bc74',command=retour_acceuil)
   loginm.place(x=5,y=10) 
   def GetValue(event):
      e1.delete(0, END)
      e2.delete(0, END)
   
      row_id = listBox.selection()[0]
      select = listBox.set(row_id)
      e1.insert(0,select['id'])
      e2.insert(0,select['email'])
 

   def delete():
     id = e1.get()
     email=e2.get()
     conn = sqlite3.connect('.\\db\\db.db')
     cursor = conn.cursor()
     try:
       cursor.execute('delete from register where id ='+id+'AND email="'+email+'"')
       conn.commit()
       messagebox.showinfo("information", "L'exploitant supprimé avec succès...")
       e1.delete(0, END)
       e2.delete(0, END)
       e1.focus_set()
     except Exception as e:
       print(e)
       conn.rollback()
       conn.close()

   def show():
        conn = sqlite3.connect('.\\db\\db.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id,username,email,password FROM register ')
        records = cursor.fetchall()
        print(records)
        for i, (id,username,email,password) in enumerate(records, start=1):
            listBox.insert("", "end", values=(id,username, email,password))
            conn.close()
 
   global e1
   global e2
   cpu=Image.open('.\\bar_titre.png')
   resize_cpu = cpu.resize((1070,70))
   photocpu=ImageTk.PhotoImage(resize_cpu)
   label_titre=Label(label_img,image=photocpu,width=1070,height=70,font=('yu gothic ui',11,'bold'))
   label_titre.place(x=-5,y=-5) 
   tk.Label(label_img, text="ID", fg="#040405",bg="white" ,font=("Helvetica",13,"bold")).place(x=350, y=130)
   Label(label_img, text="Email", fg="#040405",bg="white" ,font=("Helvetica",13,"bold")).place(x=550, y=130)
  
  
   e1 = Entry(label_img,border=3,width=25)
   e1.place(x=350, y=180)
 
   e2 = Entry(label_img,border=3,width=25)
   e2.place(x=550, y=180)
 
   def actialiser():
       secondfenetre.destroy()
       main_win()

          
   Button(label_img, text="Supprimer",command = delete,height=1, width= 13,bg='#3488FF',font=("Helvetica",14,"bold"),fg="white").place(x=340, y=260)
   Button(label_img, text="Acualiser",command = actialiser,height=1, width= 13,bg='#3488FF',font=("Helvetica",14,"bold"),fg="white").place(x=540, y=260)
   
   cols = ('Id', 'Nom d\'exploitant', 'Email','Mot de passe')
   listBox = ttk.Treeview(label_img, columns=cols, show='headings' )
 
   for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=120, y=370)
 
   show()
   listBox.bind('<Double-Button-1>',GetValue)
   secondfenetre.mainloop()
# main_win()