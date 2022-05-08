
from re import A
from tkinter import *
from PIL import ImageTk , Image
import login_name
from tkinter import messagebox as ms
import sqlite3
import acceuil
import register

a=1

def main_login_pwd():
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
    e = Example(window)
    e.pack(fill=BOTH, expand=YES)
    text='Connexion'
    heading=Label(window,text=text,font=('yu gothic ui' ,25,'bold'),bg='#040405',fg='white')
    heading.place(x=900,y=80)
    side_image=Image.open('.\\user_key.png')
    photo=ImageTk.PhotoImage(side_image)
    side_image_label=Label(window,image=photo,bg='#040405',width=400,height=450)
    side_image_label.image=photo
    side_image_label.place(x=100,y=200)

    droit_label=Label(window,bg='white',width=0,height=40)
    droit_label.place(x=650,y=90)
    password_label=Label(window,text='Mot de passe',bg='#040405',font=('yu gothic ui',14,'bold'),fg='#ACACAC')
    password_label.place(x=750,y=240)
    password_entry=Entry(window,highlightthickness=0,relief= FLAT,bg='#040405',fg='white',font=('yu gothic ui',12,'bold'),cursor='xterm')
    password_entry.place(x=785,y=280,width=270)
    password_line=Canvas(window,width=400,height=2.0,bg='#bdb9b1',highlightthickness=0)
    password_line.place(x=755,y=314)
    #*****************************************
    paswd_icon=Image.open('.\\paswd_icon.png')
    resize_image = paswd_icon.resize((25,25))
    photo=ImageTk.PhotoImage(resize_image)
    paswd_icon_label=Label(window,image=photo,bg='#040405')
    paswd_icon_label.image=photo
    paswd_icon_label.place(x=750,y=280)
    #*****************************************
    btn_login=Image.open('.\\btn_login-w.png')
    photo_login=ImageTk.PhotoImage(btn_login)

    #*****************************************


    def show():
        hide_code=Button(window,image=photo,bg='#040405',activebackground='#040405',cursor='hand2',bd=0,command=hide)
        hide_code.image=photo
        hide_code.place(x=1130,y=280)
        password_entry.config(show='')

    def hide():
        show_code=Button(window,image=photo1,bg='#040405',activebackground='#040405',cursor='hand2',bd=0,command=show)
        show_code.image=photo1
        show_code.place(x=1130,y=280)
        password_entry.config(show='*')

    show_code=Image.open('.\\eye_open.png')
    resize_image_show = show_code.resize((25,25))
    photo1=ImageTk.PhotoImage(resize_image_show)
    show_button=Button(window,image=photo1,bg='#040405',activebackground='#040405',cursor='hand2',bd=0,command=show)
    show_button.image=photo1
    show_button.place(x=1130,y=280)
    hide_code=Image.open('.\\eye_close.png')
    resize_image_hide = hide_code.resize((25,25))
    photo=ImageTk.PhotoImage(resize_image_hide)

    def retour_acceuil():
        window.destroy()
        login_name.main_login_name()

    #*********************************************
    
    
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
            if results:
                retour_acceuil()
                print("retouuur")
            # if user do not exist
            else:
                if(a<=3):
                  
                    ms.showerror('Erreur', 'Mot de passe incorrect ')
                    password_entry.delete(0,END)
                    print(a)
                    a=a+1
                else:
                   ms.showerror('Erreur', 'Consultez vous l\'administrateur ')
                   window.destroy()
                   acceuil.main_home()
                   
    #*********************************************
    login=Button(window,image=photo_login, font=('yu gothic ui',13,'bold'),width=210,height=50,bd=0,bg='#040405',cursor='hand2',activebackground='#040405',command=Searchpwd)
    login.place(x=890,y=430)
          
    btn_fleche=Image.open('.\\flecheRetour.png')
    resize_btn_fleche = btn_fleche.resize((80,60))
    photo_fleche=ImageTk.PhotoImage(resize_btn_fleche)
    back=Button(window,image=photo_fleche, font=('yu gothic ui',13,'bold'),width=80,height=60,bd=0,bg='#040405',cursor='hand2',activebackground='#040405',command=retour_acceuil)
    back.place(x=30,y=30) 
    def passregister():
        window.destroy()
        register.main_register()
    txt1='J\'ai pas un compte !'
    heading=Button(window,text=txt1,font=('yu gothic ui' ,15,'italic'),bg='#040405',fg='white',cursor='hand2' ,border=0 ,takefocus=0,command=passregister)
    heading.place(x=750,y=545)
    #**********************************
    

       
    txt2='J\'ai oublié le mot de passe !'
    heading=Button(window,text=txt2,font=('yu gothic ui' ,15,'italic'),bg='#040405',fg='white',cursor='hand2' , border=0 ,takefocus=0)
    heading.place(x=1040,y=545)
    window.mainloop()

# main_login_pwd()