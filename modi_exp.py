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
   user_icon_label.place(x=50,y=50)
   txt="Admin"
   compte=Label(secondfenetre,text=txt,bg="black",fg="grey",width=14,height=1,font=('yu gothic ui',16,'bold'))
   compte.place(x=95,y=55)
  
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
   user_icon_label.place(x=70,y=580)
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
   btn_flechea=Image.open('.\\back.png')
   resize_btn_flechea = btn_flechea.resize((40,40))
   photo_flechea=ImageTk.PhotoImage(resize_btn_flechea)
   logina=Button(label_img,image=photo_flechea,width=40,height=40,bd=0,bg='white',cursor='hand2',activebackground='#e2bc74',command=retour_acceuil)
   logina.place(x=0,y=0) 
   def GetValue(event):
      e1.delete(0, END)
      e2.delete(0, END)
      e3.delete(0, END)
      row_id = listBox.selection()[0]
      select = listBox.set(row_id)
      e1.insert(0,select['email'])
      e2.insert(0,select['password'])
      e3.insert(0,select['password'])

   def update():
    email=e1.get()
    password = e2.get()
    password_conf = e3.get()
    conn = sqlite3.connect('.\\db\\db.db')
    cursor = conn.cursor()
    try:
       cursor.execute('Update  register set password="'+password+'",password_conf="'+password_conf+'"where email="'+email+'"')
       conn.commit()
       messagebox.showinfo("information", "Mot de passe Mis à jour avec succés ...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
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
   global e3
   tk.Label(label_img, text="Modifier", fg="#3488FF",bg="white" ,font=("Helvetica",25,"bold")).place(x=25, y=40)
   tk.Label(label_img,bg="#3488FF" ,width=125,height=-3).place(x=195, y=53)
   tk.Label(label_img, text="Email", fg="#040405",bg="white" ,font=("Helvetica",13,"bold")).place(x=250, y=130)
   Label(label_img, text="Mot de passe", fg="#040405",bg="white" ,font=("Helvetica",13,"bold")).place(x=450, y=130)
   Label(label_img, text="Confirmation", fg="#040405",bg="white" ,font=("Helvetica",13,"bold")).place(x=650, y=130)
  
   e1 = Entry(label_img,border=3,width=25)
   e1.place(x=250, y=180)
 
   e2 = Entry(label_img,border=3,width=25)
   e2.place(x=450, y=180)
 
   e3 = Entry(label_img,border=3,width=25)
   e3.place(x=650, y=180)
   def actialiser():
       secondfenetre.destroy()
       main_win()

          
   Button(label_img, text="Modifier",command = update,height=1, width= 13,bg='#3488FF',font=("Helvetica",14,"bold"),fg="white").place(x=340, y=260)
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