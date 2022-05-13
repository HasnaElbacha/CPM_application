
from tkinter import *
from tkinter.ttk import Progressbar
import sys
from turtle import width
import admin_expl
from PIL import ImageTk , Image
from tkinter import messagebox as ms
import sqlite3
import admin_expl
import mode
import forgetsecond
a=1
def main_login_pwd():
   import admin_expl
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
   exit_btn=Button(fenetre,text='X',command=lambda:exit_window(),font=("yu gothic ui",13,'bold'),fg='white',bg='black',bd=0,activebackground='grey')
   exit_btn.place(x=626,y=5)
   def exit_window():
      sys.exit(fenetre.destroy())
   def retour_acceuil():
        fenetre.destroy()
        admin_expl.mainadminempl()
   btn_fleche=Image.open('.\\play.png')
   resize_btn_fleche = btn_fleche.resize((25,25))
   photo_fleche=ImageTk.PhotoImage(resize_btn_fleche)
   login=Button(fenetre,image=photo_fleche, font=('yu gothic ui',13,'bold'),width=80,height=60,bd=0,bg='#040405',cursor='hand2',activebackground='#040405',command=retour_acceuil)
   login.place(x=0,y=0) 
   loginn_icon=Image.open('.\\login.png')
   resize_image = loginn_icon.resize((80,80))
   photol=ImageTk.PhotoImage(resize_image)
   loginn_icon_label=Label(fenetre,image=photol,bg='#040405')
   loginn_icon_label.image=photol
   loginn_icon_label.place(x=270,y=80)
   password_label=Label(fenetre,text='Mot de passe',bg='#040405',font=('yu gothic ui',14,'bold'),fg='#ACACAC')
   password_label.place(x=255,y=180)
   password_entry=Entry(fenetre,highlightthickness=0,relief= FLAT,bg='#040405',fg='white',font=('yu gothic ui',12,'bold'),cursor='xterm')
   password_entry.place(x=230,y=225,width=270)
   password_line=Canvas(fenetre,width=200,height=2.0,bg='#bdb9b1',highlightthickness=0)
   password_line.place(x=230,y=250)
   paswd_icon=Image.open('.\\paswd_icon.png')
   resize_image = paswd_icon.resize((25,25))
   photo=ImageTk.PhotoImage(resize_image)
   paswd_icon_label=Label(fenetre,image=photo,bg='#040405')
   paswd_icon_label.image=photo
   paswd_icon_label.place(x=200,y=225)
#***************************************
   btn_login=Image.open('.\\connexion.png')
   photo_login=ImageTk.PhotoImage(btn_login)
   def Searchpwd():
        global a
        if password_entry.get() == '': 
            ms.showerror('Erreur', 'Enter le mots de passe !!')
            
        else:
            global password
            password = password_entry.get()
            

            # Making connection
            conn = sqlite3.connect('.\\db\\db.db')

            # Creating cursor
            with conn:
                cursor = conn.cursor()

            cursor.execute('SELECT * FROM register WHERE password ="'+password+'"')
            results = cursor.fetchall()
            # if user then new window
            if (password=="admincpm"):
                # retour_acceuil()
                fenetre.destroy()
                mode.main_win()
                print("retouuur")
            # if user do not exist
            else:
                if(a<=3):
                    ms.showerror('Erreur', 'Mot de passe incorrect ')
                    password_entry.delete(0,END)
                    print(a)
                    a=a+1
                else:
                   ms.showerror('Erreur', 'Les tentatives sont limités')
                   retour_acceuil()
   login=Button(fenetre,image=photo_login, font=('yu gothic ui',13,'bold'),width=210,height=50,bd=0,bg='#040405',cursor='hand2',activebackground='#040405',command=Searchpwd)
   login.place(x=75,y=350)
        
   def passforget():
      fenetre.destroy()
      forgetsecond.mainlogin_name()
   txt2='J\'ai oublié le mot de passe !'
   heading=Button(fenetre,text=txt2,font=('yu gothic ui' ,15,'italic'),bg='#040405',fg='white',cursor='hand2' , border=0 ,takefocus=0,command=passforget)
   heading.place(x=360,y=350)
   def show():
        hide_code=Button(fenetre,image=photo,bg='#040405',activebackground='#040405',cursor='hand2',bd=0,command=hide)
        hide_code.image=photo
        hide_code.place(x=440,y=230)
        password_entry.config(show='')

   def hide():
        show_code=Button(fenetre,image=photo1,bg='#040405',activebackground='#040405',cursor='hand2',bd=0,command=show)
        show_code.image=photo1
        show_code.place(x=440,y=230)
        password_entry.config(show='*')

   show_code=Image.open('.\\eye_open.png')
   resize_image_show = show_code.resize((25,25))
   photo1=ImageTk.PhotoImage(resize_image_show)
   show_button=Button(fenetre,image=photo1,bg='#040405',activebackground='#040405',cursor='hand2',bd=0,command=show)
   show_button.image=photo1
   show_button.place(x=440,y=230)
   hide_code=Image.open('.\\eye_close.png')
   resize_image_hide = hide_code.resize((25,25))
   photo=ImageTk.PhotoImage(resize_image_hide)

   fenetre.mainloop()
# main_login_pwd()