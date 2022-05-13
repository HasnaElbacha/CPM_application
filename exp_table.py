from tkinter import *
from PIL import ImageTk , Image
from tkinter import messagebox as ms
import tkinter as tk
from tkinter import ttk
from click import command
from numpy import place
from tkinter.ttk import Progressbar
import login_name
import sqlite3
from tkinter import messagebox
import admin_register
import register
import exp_mode
import parametre
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
   txt="-------"
   compte=Label(secondfenetre,text=txt,bg="black",fg="grey",width=14,height=1,font=('yu gothic ui',16,'bold'))
   compte.place(x=95,y=55)
  
#********************************************
   def passregister():
      secondfenetre.destroy()
      register.main_register()
   def passacceuil():
       secondfenetre.destroy()
       exp_mode.main_win()
   lien_maison=Image.open('.\\maison_noir.png')
   photo1=ImageTk.PhotoImage(lien_maison)
   icon1=Button(buttons_label,image=photo1,bg='#3488FF', border=2,width=80,height=50,command=passacceuil)
   icon1.place(x=10,y=270)
   icon1_lb=Button(buttons_label,text="Acceuil" ,bg='#040405',fg='#3488FF', border=1,width=15,height=1,font=('yu gothic ui',15,'bold'),command=passacceuil)
   icon1_lb.place(x=110,y=270)

   def passexp():
      secondfenetre.destroy()
      exp_exploitants.main_win()
   lien_maison=Image.open('.\\expl_grey.png')
   photo4=ImageTk.PhotoImage(lien_maison)
   icon4=Button(buttons_label,image=photo4,bg='#040405', border=2,width=80,height=50,command=passexp)
   icon4.place(x=10,y=360)
   icon4_lb=Button(buttons_label,text="Exploitants" ,bg='#040405',fg='#E5E4E2', border=1,width=15,height=1,font=('yu gothic ui',15,'bold'),command=passexp)
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
   
   label_img=Label(secondfenetre, bg="white",width=1050,height=33,font=('yu gothic ui',11,'bold'))
   label_img.place(x=320,y=0)  
   def GetValue(event):
      e1.delete(0, END)
      e2.delete(0, END)
      e3.delete(0, END)
      e4.delete(0, END)
      row_id = listBox.selection()[0]
      select = listBox.set(row_id)
      e1.insert(0,select['id'])
      e2.insert(0,select['ip_address'])
      e3.insert(0,select['date'])
      e4.insert(0,select['time'])
   def Add():
      id=e1.get()
      ip_address = e2.get()
      date = e3.get()
      time = e4.get()
      conn = sqlite3.connect('.\\db\\connec.db')
      cursor = conn.cursor()
      try:
       cursor.execute('INSERT INTO  connection (id,ip_address,date,time) VALUES ('+id+',"'+ip_address+'","'+date+'","'+time+'")')
       conn.commit()
       messagebox.showinfo("information", "L'information insérée avec succès...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()
      except Exception as e:
       print(e)
       conn.rollback()
       conn.close()
 
 
   def update():
    id=e1.get()
    ip_address = e2.get()
    date = e3.get()
    time = e4.get()
    conn = sqlite3.connect('.\\db\\connec.db')
    cursor = conn.cursor()
    try:
       cursor.execute('Update  connection set ip_address="'+ip_address+'",date="'+date+'",time="'+time+'" where id='+id)
       conn.commit()
       messagebox.showinfo("information", "Record Updateddddd successfully...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()
    except Exception as e:  
       print(e)
       conn.rollback()
       conn.close()
 
   def delete():
     id = e1.get()
     conn = sqlite3.connect('.\\db\\connec.db')
     cursor = conn.cursor()
     try:
       cursor.execute('delete from registation where id ='+id)
       conn.commit()
       messagebox.showinfo("information", "Record Deleteeeee successfully...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()
     except Exception as e:
       print(e)
       conn.rollback()
       conn.close()
 
   def show():
        conn = sqlite3.connect('.\\db\\connec.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id,ip_address,date,time FROM connection')
        records = cursor.fetchall()
        print(records)
        for i, (id,ip_address,date,time) in enumerate(records, start=1):
            listBox.insert("", "end", values=(id, ip_address,date, time))
            conn.close()
 
   global e1
   global e2
   global e3
   global e4
   tk.Label(label_img, text="Registation des connexions", fg="#3488FF",bg="white" ,font=("Helvetica",25,"bold")).place(x=300, y=5)
   tk.Label(label_img,bg="#3488FF",width=200,height=0).place(x=0, y=70)
   tk.Label(label_img, text="ID de l'information", fg="#040405",bg="white" ,font=("Helvetica",13,"bold")).place(x=150, y=250)
   Label(label_img, text="Adresse ip", fg="#040405",bg="white" ,font=("Helvetica",13,"bold")).place(x=350, y=250)
   Label(label_img, text="Date", fg="#040405",bg="white" ,font=("Helvetica",13,"bold")).place(x=550, y=250)
   Label(label_img, text="Heurs", fg="#040405",bg="white" ,font=("Helvetica",13,"bold")).place(x=750, y=250)
 
   e1 = Entry(label_img,border=3,width=25)
   e1.place(x=150, y=300)
 
   e2 = Entry(label_img,border=3,width=25)
   e2.place(x=350, y=300)
 
   e3 = Entry(label_img,border=3,width=25)
   e3.place(x=550, y=300)
 
   e4 = Entry(label_img,border=3,width=25)
   e4.place(x=750, y=300)

   def actialiser():
       secondfenetre.destroy()
       main_win()
   Button(label_img, text="Inserer",command = Add,height=2, width= 13,bg='#3488FF',font=("Helvetica",14,"bold"),fg="white").place(x=340, y=440)
   Button(label_img, text="Acualiser",command = actialiser,height=2, width= 13,bg='#3488FF',font=("Helvetica",14,"bold"),fg="white").place(x=540, y=440)

 
   cols = ('Id', 'Ip adresse', 'Date','Heures')
   listBox = ttk.Treeview(label_img, columns=cols, show='headings' )
 
   for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=120, y=700)
 
   show()
   listBox.bind('<Double-Button-1>',GetValue)
   secondfenetre.mainloop()
# main_win()