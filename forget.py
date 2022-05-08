from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from PIL import Image,ImageTk,ImageDraw,ImageFont
import os
from tkinter import filedialog
import acceuil
import sqlite3
from tkinter import messagebox as ms
def main_forget():
    window=Tk()
    window.geometry('1166x718')
    window.state('zoomed')
    window.resizable(0,0)
    window.configure(background="black")
    text='Mot de passe oublié'
    heading=Label(window,text=text,font=('yu gothic ui' ,25,'bold'),bg='#040405',fg='white')
    heading.place(x=540,y=50)
    pen_image=Image.open('.\\pen.png')
    resize_image_pen = pen_image.resize((50,50))
    photo=ImageTk.PhotoImage(resize_image_pen)
    pen_image_label=Label(window,image=photo,bg='#040405',width=400,height=450)
    pen_image_label.image=photo
    pen_image_label.place(x=1080,y=440)
    #************************************************************************************
    plan=Label(window,bg="#DCDCDC",width=69,height=35)
    plan.place(x=450,y=170)
    plan1=Label(window,bg="#A9A9A9",width=67,height=35)
    plan1.place(x=450,y=160)
    plan2=Label(window,bg="#808080",width=65,height=35)
    plan2.place(x=450,y=150)
    email_label=Label(plan2,text='Entrer votre adresse email',bg='#808080',font=('yu gothic ui',14,'bold'),fg='#0E0E0E')
    email_label.place(x=60,y=60)
    email_entry=Entry(plan2,highlightthickness=0,relief= FLAT,bg='#808080',fg='black',font=('yu gothic ui',12,'bold'),cursor='xterm')
    email_entry.place(x=90,y=100,width=270)
    email_line=Canvas(plan2,width=300,height=2.0,bg='#bdb9b1',highlightthickness=0)
    email_line.place(x=65,y=130)
    #*****************************************
    email_icon=Image.open('.\\e_icon.png')
    resize_image_user = email_icon.resize((25,25))
    photo=ImageTk.PhotoImage(resize_image_user)
    email_icon_label=Label(plan2,image=photo,bg='#808080')
    email_icon_label.image=photo
    email_icon_label.place(x=60,y=100)
    #*****************************************
    def send():
        global email
        conn = sqlite3.connect('.\\db\\db.db')
        email = email_entry.get()
        with conn:
                cursor = conn.cursor()
        cursor.execute('select * from register where email= "'+email+'"')
        result=cursor.fetchall()
        print(result)
        
        if (email==''):
            messagebox.showinfo("Erreur",'Remplit le champ')
        else:
            if(result):
                user=email
                with conn:
                    cursor = conn.cursor()
                cursor.execute('select password from register where email= "'+email+'"')
                result1=cursor.fetchall()
                for results in result1:
                    print(results)
                    txte=results
            
                try:
                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    server.login("ARC.app1@gmail.com", "Hassena1")
                    server.sendmail("expediteur@address.com",user,  "subject: test \nce message vient de python")
                    server.quit()
                except:
                    messagebox.showerror("Error",'Email Not Send')
                    email_label=Label(plan2,text='Nom d\'utilisateur',bg='#808080',font=('yu gothic ui',13,'bold'),fg='#4f4e4d')
                    email_label.place(x=60,y=60)
                    email_line=Canvas(plan2,width=300,height=2.0,bg='#bdb9b1',highlightthickness=0)
                    email_line.place(x=65,y=130)
                    #*****************************************
                    email_icon=Image.open('.\\user_icon.png')
                    resize_image_user = email_icon.resize((25,25))
                    photo=ImageTk.PhotoImage(resize_image_user)
                    email_icon_label=Label(plan2,image=photo,bg='#808080')
                    email_icon_label.image=photo
                    email_icon_label.place(x=60,y=100)
                    psw_label=Label(plan2,text='votre Mot de passe ',bg='#808080',font=('yu gothic ui',14,'bold'),fg='#0E0E0E')
                    psw_label.place(x=60,y=350)
                    ent_label=Label(plan2,text=txte,bg='#808080',font=('yu gothic ui',13,'bold'),fg='black')
                    ent_label.place(x=60,y=380)
                    pwd_line=Canvas(plan2,width=300,height=2.0,bg='#bdb9b1',highlightthickness=0)
                    pwd_line.place(x=65,y=410)
                
            else:
               ms.showerror('Erreur', 'Cette adresse n\'existe pas!!!')
    #*****************************************************
    btn_inscrire=Image.open('.\\btn_inscrire.png')
    photo_inscrire=ImageTk.PhotoImage(btn_inscrire)
    inscrire=Button(window,text='Envoyer', font=('yu gothic ui',15,'bold'),width=18,height=2,bd=4,bg='grey',cursor='hand2',activebackground='white',command=send)
    inscrire.place(x=570,y=370)
    
    def retour_acceuil():
        window.destroy()
        acceuil.main_home()
    btn_fleche=Image.open('.\\flecheRetour.png')
    resize_btn_fleche = btn_fleche.resize((80,60))
    photo_fleche=ImageTk.PhotoImage(resize_btn_fleche)
    login=Button(window,image=photo_fleche, font=('yu gothic ui',13,'bold'),width=80,height=60,bd=0,bg='#040405',cursor='hand2',activebackground='#040405',command=retour_acceuil)
    login.place(x=30,y=30)
    # simage=PhotoImage(file='sent.png')
    # sent_email=Button(plan2,text='Send Email',font=('times new roman',15,'bold'),relief=GROOVE,bd=2,command=lambda:send())
    # sent_email.place(x=730,y=400,width=180)
    # sent_email.config(plan2,compound=LEFT)
    
    window.mainloop()
  
# main_forget()        

