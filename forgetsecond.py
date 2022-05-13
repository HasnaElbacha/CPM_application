from tkinter import *
from tkinter.ttk import Progressbar
import sys
from turtle import width
from PIL import ImageTk , Image
import mode
import login_pwd
import smtplib,ssl
import acceuil
from tkinter import messagebox
import register
from tkinter import messagebox as ms
import sqlite3
import admin_expl
import admin_login_pwd
def mainlogin_name():
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
    exit_btn=Button(fenetre,text='X',command=lambda:exit_window(),font=("yu gothic ui",13,'bold'),fg='white',bg='black',bd=0,activebackground='grey')
    exit_btn.place(x=626,y=0)
    global username_entry
    loginn_icon=Image.open('.\\login.png')
    resize_image = loginn_icon.resize((80,80))
    photol=ImageTk.PhotoImage(resize_image)
    loginn_icon_label=Label(fenetre,image=photol,bg='#040405')
    loginn_icon_label.image=photol
    loginn_icon_label.place(x=270,y=50)
#************************************************************************************
    email_label=Label(fenetre,text='Entrer votre adresse email',bg='#040405',font=('yu gothic ui',14,'bold'),fg='#ACACAC')
    email_label.place(x=200,y=140)
    email_entry=Entry(fenetre,highlightthickness=0,relief= FLAT,bg='#040405',fg='white',font=('yu gothic ui',12,'bold'),cursor='xterm')
    email_entry.place(x=230,y=180,width=270)
    email_line=Canvas(fenetre,width=250,height=2.0,bg='#bdb9b1',highlightthickness=0)
    email_line.place(x=200,y=210)
    #*****************************************
    email_icon=Image.open('.\\email_icon.png')
    resize_image_user = email_icon.resize((25,25))
    photo=ImageTk.PhotoImage(resize_image_user)
    email_icon_label=Label(fenetre,image=photo,bg='black')
    email_icon_label.image=photo
    email_icon_label.place(x=195,y=180)
    #************************************************************************************  
    #************************************************************************************            
    def passloginpwd():
        fenetre.destroy()
        admin_login_pwd.main_login_pwd()
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
                    # messagebox.showerror("Réussi",'Voila votre mot de passe')
                    # email_label=Label(fenetre,text='Nom d\'utilisateur',bg='#040405',font=('yu gothic ui',13,'bold'),fg='#ACACAC')
                    # email_label.place(x=60,y=60)
                    # email_line=Canvas(fenetre,width=300,height=2.0,bg='#bdb9b1',highlightthickness=0)
                    # email_line.place(x=65,y=130)
                    #*****************************************
                    # email_icon=Image.open('.\\user_icon.png')
                    # resize_image_user = email_icon.resize((25,25))
                    # photo=ImageTk.PhotoImage(resize_image_user)
                    # email_icon_label=Label(fenetre,image=photo,bg='#808080')
                    # email_icon_label.image=photo
                    # email_icon_label.place(x=60,y=100)
                    psw_label=Label(fenetre,text='votre Mot de passe ',bg='black',font=('yu gothic ui',14,'bold'),fg='#3488FF')
                    psw_label.place(x=60,y=330)
                    ent_label=Label(fenetre,text=txte,bg='black',font=('yu gothic ui',13,'bold'),fg='white')
                    ent_label.place(x=90,y=360)
                    pwd_line=Canvas(fenetre,width=200,height=2.0,bg='#bdb9b1',highlightthickness=0)
                    pwd_line.place(x=65,y=390)
                    email_icon=Image.open('.\\paswd_icon.png')
                    resize_image_user = email_icon.resize((25,25))
                    photo=ImageTk.PhotoImage(resize_image_user)
                    email_icon_label=Label(fenetre,image=photo,bg='black')
                    email_icon_label.image=photo
                    email_icon_label.place(x=55,y=360)
                
            else:
               ms.showerror('Erreur', 'Cette adresse n\'existe pas!!!')
    login=Button(fenetre,text="Envoyer" , font=('yu gothic ui',13,'bold'),width=18,height=2,bd=0,bg='#3488FF',cursor='hand2',activebackground='#040405',command=send)
    login.place(x=220,y=240)
    
    def retour_acceuil():
        fenetre.destroy()
        admin_login_pwd.main_login_pwd()
           
    btn_fleche=Image.open('.\\play.png')
    resize_btn_fleche = btn_fleche.resize((25,25))
    photo_fleche=ImageTk.PhotoImage(resize_btn_fleche)
    login=Button(fenetre,image=photo_fleche, font=('yu gothic ui',13,'bold'),width=80,height=60,bd=0,bg='#040405',cursor='hand2',activebackground='#040405',command=retour_acceuil)
    login.place(x=0,y=0) 
    fenetre.mainloop()

# mainlogin_name()