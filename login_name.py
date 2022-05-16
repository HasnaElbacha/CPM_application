
from tkinter import *
from PIL import ImageTk , Image
from setuptools import Command
import login_pwd
import acceuil
import register
from tkinter import messagebox as ms
import sqlite3


def main_login_name():
    window=Tk()
    window.geometry('1166x718')
    window.state('zoomed')
    window.resizable(0,0)
    window.configure(background="black")
    class Example(Frame):
        def __init__(self, master, *pargs):
            Frame.__init__(self, master, *pargs)
            self.background = Label(self,bg='#040405' )
            self.background.pack(fill=BOTH, expand=YES)

        def _resize_image(self,event):
            new_width = event.width
            new_height = event.height
            self.image = self.img_copy.resize((new_width, new_height))
            self.background_image = ImageTk.PhotoImage(self.image)
            self.background.configure(image =  self.background_image)
    global username_entry
    e = Example(window)
    e.pack(fill=BOTH, expand=YES)
    droit_label=Label(window,bg='white',width=0,height=40)
    droit_label.place(x=650,y=90)
    text='Connexion'
    heading=Label(window,text=text,font=('yu gothic ui' ,25,'bold'),bg='#040405',fg='white')
    heading.place(x=900,y=80)
    side_image=Image.open('.\\user_key.png')
    photo=ImageTk.PhotoImage(side_image)
    side_image_label=Label(window,image=photo,bg='#040405',width=400,height=450)
    side_image_label.image=photo
    side_image_label.place(x=100,y=200)
    username_label=Label(window,text='Nom d\'utilisateur',bg='#040405',font=('yu gothic ui',14,'bold'),fg='#ACACAC')
    username_label.place(x=750,y=240)
    username_entry=Entry(window,highlightthickness=0,relief= FLAT,bg='#040405',fg='white',font=('yu gothic ui',12,'bold'),cursor='xterm')
    username_entry.place(x=785,y=280,width=270)
    username_line=Canvas(window,width=400,height=2.0,bg='#bdb9b1',highlightthickness=0)
    username_line.place(x=755,y=314)
    #*****************************************
    user_icon=Image.open('.\\user_icon.png')
    resize_image = user_icon.resize((25,25))
    photo=ImageTk.PhotoImage(resize_image)
    user_icon_label=Label(window,image=photo,bg='#040405')
    user_icon_label.image=photo
    user_icon_label.place(x=750,y=280)
    #*****************************************
    btn_login=Image.open('.\\btn_login-w.png')
    photo_login=ImageTk.PhotoImage(btn_login)

    #*****************************************
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
                   print("showerreur user")
                   ms.showerror('Erreur', 'ce nom d\'utilisateur n\'existe pas')
                   
    #************************************************************************************            
    def passloginpwd():
        window.destroy()
        login_pwd.main_login_pwd()
    login=Button(window,image=photo_login, font=('yu gothic ui',13,'bold'),width=210,height=50,bd=0,bg='#040405',cursor='hand2',activebackground='#040405',command=Search)
    login.place(x=800,y=410)

    def retour_acceuil():
        window.destroy()
        acceuil.main_home()
           
    btn_fleche=Image.open('.\\flecheRetour.png')
    resize_btn_fleche = btn_fleche.resize((80,60))
    photo_fleche=ImageTk.PhotoImage(resize_btn_fleche)
    login=Button(window,image=photo_fleche, font=('yu gothic ui',13,'bold'),width=80,height=60,bd=0,bg='#040405',cursor='hand2',activebackground='#040405',command=retour_acceuil)
    login.place(x=30,y=30) 
    def passregister():
        window.destroy()
        register.main_register()

    txt='J\'ai pas un compte !'
    heading=Button(window,text=txt,font=('yu gothic ui' ,15,'italic'),bg='#040405',fg='white', border=0 ,cursor='hand2',takefocus=0,command=passregister)
    heading.place(x=1050,y=415)
     
    window.mainloop()
    
    
# main_login_name()

