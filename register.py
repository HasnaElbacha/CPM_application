from tkinter import *
from PIL import ImageTk , Image
from tkinter import messagebox as ms
import sqlite3
import acceuil
def main_register():
    window=Tk()
    window.geometry('1166x718')
    window.state('zoomed')
    window.resizable(0,0)
    window.configure(background="black")
    class Example(Frame):
        def __init__(self, master, *pargs):
            Frame.__init__(self, master, *pargs)
            self.background = Label(self,bg='#040405')
            self.background.pack(fill=BOTH, expand=YES)
            self.background.bind('<Configure>', self._resize_image)

        def _resize_image(self,event):
            new_width = event.width
            new_height = event.height
            self.image = self.img_copy.resize((new_width, new_height))
            self.background_image = ImageTk.PhotoImage(self.image)
            self.background.configure(image =  self.background_image)

    e = Example(window)
    e.pack(fill=BOTH, expand=YES)
    text='S\'inscrire'
    heading=Label(window,text=text,font=('yu gothic ui' ,25,'bold'),bg='#040405',fg='white')
    heading.place(x=600,y=50)
    pen_image=Image.open('.\\pen.png')
    resize_image_pen = pen_image.resize((50,50))
    photo=ImageTk.PhotoImage(resize_image_pen)
    pen_image_label=Label(window,image=photo,bg='#040405',width=400,height=450)
    pen_image_label.image=photo
    pen_image_label.place(x=1050,y=400)
    #************************************************************************************
    plan=Label(window,bg="#DCDCDC",width=104,height=35)
    plan.place(x=310,y=170)
    plan1=Label(window,bg="#A9A9A9",width=102,height=35)
    plan1.place(x=310,y=160)
    plan2=Label(window,bg="#808080",width=100,height=35)
    plan2.place(x=310,y=150)
    username_label=Label(plan2,text='Nom d\'utilisateur',bg='#808080',font=('yu gothic ui',13,'bold'),fg='#0E0E0E')
    username_label.place(x=60,y=60)
    username_entry=Entry(plan2,highlightthickness=0,relief= FLAT,bg='#808080',fg='black',font=('yu gothic ui',12,'bold'),cursor='xterm')
    username_entry.place(x=90,y=100,width=270)
    username_line=Canvas(plan2,width=300,height=2.0,bg='#bdb9b1',highlightthickness=0)
    username_line.place(x=65,y=130)
    #*****************************************
    user_icon=Image.open('.\\u_icon.png')
    resize_image_user = user_icon.resize((25,25))
    photo=ImageTk.PhotoImage(resize_image_user)
    user_icon_label=Label(plan2,image=photo,bg='#808080')
    user_icon_label.image=photo
    user_icon_label.place(x=60,y=100)
    #*****************************************
    #************************************************************************************
    password_label=Label(plan2,text='Mot de passe',bg='#808080',font=('yu gothic ui',13,'bold'),fg='#0E0E0E')
    password_label.place(x=60,y=290)
    password_entry=Entry(plan2,highlightthickness=0,relief= FLAT,bg='#808080',fg='black',font=('yu gothic ui',12,'bold'),cursor='xterm')
    password_entry.place(x=90,y=330,width=270)
    password_line=Canvas(plan2,width=300,height=2.0,bg='#bdb9b1',highlightthickness=0)
    password_line.place(x=65,y=360)
    #*****************************************
    password_icon=Image.open('.\\p_icon.png')
    resize_image_pass = password_icon.resize((25,25))
    photo=ImageTk.PhotoImage(resize_image_pass)
    password_icon_label=Label(plan2,image=photo,bg='#808080')
    password_icon_label.image=photo
    password_icon_label.place(x=60,y=330)
    #*****************************************
    #************************************************************************************
    confipass_label=Label(plan2,text='Confirmation de mot de passe',bg='#808080',font=('yu gothic ui',13,'bold'),fg='#0E0E0E')
    confipass_label.place(x=60,y=420)
    confipass_entry=Entry(plan2,highlightthickness=0,relief= FLAT,bg='#808080',fg='black',font=('yu gothic ui',12,'bold'),cursor='xterm')
    confipass_entry.place(x=90,y=460,width=270)
    confipass_line=Canvas(plan2,width=300,height=2.0,bg='#bdb9b1',highlightthickness=0)
    confipass_line.place(x=65,y=490)
    #*****************************************
    confipass_icon=Image.open('.\\p_icon.png')
    resize_image_pass = confipass_icon.resize((25,25))
    photo=ImageTk.PhotoImage(resize_image_pass)
    confipass_icon_label=Label(plan2,image=photo,bg='#808080')
    confipass_icon_label.image=photo
    confipass_icon_label.place(x=60,y=460)
    #*****************************************
    #************************************************************************************
    email_label=Label(plan2,text='Email',bg='#808080',font=('yu gothic ui',13,'bold'),fg='#0E0E0E')
    email_label.place(x=60,y=170)
    email_entry=Entry(plan2,highlightthickness=0,relief= FLAT,bg='#808080',fg='black',font=('yu gothic ui',12,'bold'),cursor='xterm')
    email_entry.place(x=90,y=210,width=270)
    email_line=Canvas(plan2,width=300,height=2.0,bg='#bdb9b1',highlightthickness=0)
    email_line.place(x=65,y=240)
    #*****************************************
    email_icon=Image.open('.\\e_icon.png')
    resize_image_email = email_icon.resize((25,25))
    photo=ImageTk.PhotoImage(resize_image_email)
    email_icon_label=Label(plan2,image=photo,bg='#808080')
    email_icon_label.image=photo
    email_icon_label.place(x=60,y=210)
    #*****************************************
    def database():
      
        # Getting entries
        username = username_entry.get()
        email = email_entry.get()
        password=password_entry.get()
        password_conf=confipass_entry.get()
        # Validating Entries
        validation = []

        # Adding information to the list
        validation.append(username)
        validation.append(email)
        validation.append(username)
        validation.append(password)
        validation.append(password_conf)

        # Boolean for condition
        condition = True
        
        # Looping and checking conditions
        for ele in validation:
            if ele == '':
                condition = False
                break

        if condition:
            # Checking for password match
            if password != password_conf:
                ms.showerror('Erreur', 'Mots de passe de sont pas identiques!!!')    
            else:
                # Making connection
                conn = sqlite3.connect('.\\db\\db.db')
                #Creating cursor
                with conn:
                    cursor = conn.cursor()
                cursor.execute('select * from register where username= "'+username+'"and email="'+email+'" and password="'+password_conf+'"')
                result=cursor.fetchall()
                if(result):
                    ms.showinfo('Erreir', 'Compte existe déjà')
                else:
                    cursor.execute('INSERT INTO register (username,email,password,password_conf) VALUES ("'+username+'","'+email+'","'+password+'","'+password_conf+'")')
                    conn.commit()
                    # Showing success message
                    ms.showinfo('Réussi', 'Compte créé avec succès !! Vous pouvez maintenant vous connecter au système !!')
                    # Closing the window
                    window.destroy()
            
        else:
            ms.showerror('Erreur', 'Veuillez remplir tous les champs de saisie')
    #*****************************************************
    btn_inscrire=Image.open('.\\btn_inscrire.png')
    photo_inscrire=ImageTk.PhotoImage(btn_inscrire)
    inscrire=Button(window,image=photo_inscrire, font=('yu gothic ui',13,'bold'),width=235,height=50,bd=0,bg='grey',cursor='hand2',activebackground='#040405',command=database)
    inscrire.place(x=730,y=400)
    #*******************************************
    def show_pswd():
        hide_code=Button(window,image=photo,bg='grey',activebackground='grey',cursor='hand2',bd=0,command=hide_pswd)
        hide_code.image=photo
        hide_code.place(x=650,y=484)
        password_entry.config(show='')

    def hide_pswd():
        show_code=Button(window,image=photo1,bg='grey',activebackground='grey',cursor='hand2',bd=0,command=show_pswd)
        show_code.image=photo1
        show_code.place(x=650,y=484)
        password_entry.config(show='*')

    show_code=Image.open('.\\eye_open.png')
    resize_image_show = show_code.resize((25,25))
    photo1=ImageTk.PhotoImage(resize_image_show)
    show_button=Button(window,image=photo1,bg='grey',activebackground='grey',cursor='hand2',bd=0,command=show_pswd)
    show_button.image=photo1
    show_button.place(x=650,y=484)
    hide_code=Image.open('.\\eye_close.png')
    resize_image_hide = hide_code.resize((25,25))
    photo=ImageTk.PhotoImage(resize_image_hide)

    def show_confi():
        hide_code=Button(window,image=photo,bg='grey',activebackground='grey',cursor='hand2',bd=0,command=hide_confi)
        hide_code.image=photo
        hide_code.place(x=650,y=615)
        confipass_entry.config(show='')

    def hide_confi():
        show_code=Button(window,image=photo1,bg='grey',activebackground='grey',cursor='hand2',bd=0,command=show_confi)
        show_code.image=photo1
        show_code.place(x=650,y=615)
        confipass_entry.config(show='*')

    show_code=Image.open('.\\eye_open.png')
    resize_image_show = show_code.resize((25,25))
    photo1=ImageTk.PhotoImage(resize_image_show)
    show_button=Button(window,image=photo1,bg='grey',activebackground='grey',cursor='hand2',bd=0,command=show_confi)
    show_button.image=photo1
    show_button.place(x=650,y=615)
    hide_code=Image.open('.\\eye_close.png')
    resize_image_hide = hide_code.resize((25,25))
    photo=ImageTk.PhotoImage(resize_image_hide)

    def retour_acceuil():
        window.destroy()
        acceuil.main_home()
    btn_fleche=Image.open('.\\flecheRetour.png')
    resize_btn_fleche = btn_fleche.resize((80,60))
    photo_fleche=ImageTk.PhotoImage(resize_btn_fleche)
    login=Button(window,image=photo_fleche, font=('yu gothic ui',13,'bold'),width=80,height=60,bd=0,bg='#040405',cursor='hand2',activebackground='#040405',command=retour_acceuil)
    login.place(x=30,y=30)
    window.mainloop()
# main_register()