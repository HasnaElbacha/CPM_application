from tkinter import *
from tkinter.ttk import Progressbar
import sys
from turtle import width
from PIL import ImageTk , Image
import mode
import login_pwd
import acceuil
import register
from tkinter import messagebox as ms
import sqlite3
import admin_expl
import exp_login_pwd
import os

def mainlogin_name():
    global Username
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
    loginn_icon_label.place(x=270,y=80)
    username_label=Label(fenetre,text='Nom d\'utilisateur',bg='#040405',font=('yu gothic ui',14,'bold'),fg='#ACACAC')
    username_label.place(x=240,y=180)
    username_entry=Entry(fenetre,highlightthickness=0,relief= FLAT,bg='#040405',fg='white',font=('yu gothic ui',12,'bold'),cursor='xterm')
    username_entry.place(x=230,y=225,width=270)
    username_line=Canvas(fenetre,width=200,height=2.0,bg='#bdb9b1',highlightthickness=0)
    username_line.place(x=230,y=250)
    #*****************************************
    user_icon=Image.open('.\\user_icon.png')
    resize_image = user_icon.resize((25,25))
    photo=ImageTk.PhotoImage(resize_image)
    user_icon_label=Label(fenetre,image=photo,bg='#040405')
    user_icon_label.image=photo
    user_icon_label.place(x=200,y=225)
    #*****************************************
    btn_login=Image.open('.\\connexion.png')
    photo_login=ImageTk.PhotoImage(btn_login)
    # user=username_entry.get()
    # global user
    # user="gfffffffff"
    #************************************************************************************  
    def Search():
        
        if username_entry.get() == '': 
            ms.showerror('Erreur', 'Enter votre nom !!')
        else:
            global Username
            Username = username_entry.get()
            conn = sqlite3.connect('.\\db\\db.db')
            with conn:
                cursor = conn.cursor()
            # find_user = ('SELECT username FROM register WHERE username ='+Username)
            cursor.execute('SELECT * FROM register WHERE username ="'+Username+'"')
            results = cursor.fetchall()
            if results:
                passloginpwd()
                
            else:  
                   ms.showerror('Erreur', 'Ce nom d\'utilisateur n\'existe pas')
            var= username_entry.get()         
    #************************************************************************************            
    def passloginpwd():
        global Username
        fenetre.destroy()
        exp_login_pwd.main_login_pwd(Username)
    login=Button(fenetre,image=photo_login, font=('yu gothic ui',13,'bold'),width=210,height=50,bd=0,bg='#040405',cursor='hand2',activebackground='#040405',command=Search)
    login.place(x=220,y=350)
    
    def retour_acceuil():
        fenetre.destroy()
        admin_expl.mainadminempl()
           
    btn_fleche=Image.open('.\\play.png')
    resize_btn_fleche = btn_fleche.resize((25,25))
    photo_fleche=ImageTk.PhotoImage(resize_btn_fleche)
    login=Button(fenetre,image=photo_fleche, font=('yu gothic ui',13,'bold'),width=80,height=60,bd=0,bg='#040405',cursor='hand2',activebackground='#040405',command=retour_acceuil)
    login.place(x=0,y=0) 
    fenetre.mainloop()

# mainlogin_name()

