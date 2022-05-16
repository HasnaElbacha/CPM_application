from tkinter import *
from PIL import ImageTk , Image
from tkinter import messagebox as ms
import tkinter as tk
from tkinter import ttk
from click import command
from numpy import place
from tkinter.ttk import Progressbar
import parametre
import sqlite3
import home_win_admin
import mode
import exploitants
comp=True
def main_win():
   
   register =Tk()
   register.state("zoomed")
   register.config(background="#FFFFFF")
   buttons_label = Label(register, bg="black" ,height=237,width=45)
   buttons_label.place(x=0,y=0)

   #***************************************
   user_icon=Image.open('.\\compte_.png')
   resize_image = user_icon.resize((40,40))
   photo=ImageTk.PhotoImage(resize_image)
   user_icon_label=Label(buttons_label,image=photo,bg='#040405')
   user_icon_label.image=photo
   user_icon_label.place(x=50,y=50)
   txt="Admin"
   compte=Label(register,text=txt,bg="black",fg="grey",width=14,height=1,font=('yu gothic ui',16,'bold'))
   compte.place(x=95,y=55)
  
#********************************************
   
   def passemode():
      register.destroy()
      mode.main_win()
   lienn_maison=Image.open('.\\maison_grey.png')
   photoo=ImageTk.PhotoImage(lienn_maison)
   icon1=Button(buttons_label,image=photoo,bg='#040405', border=2,width=80,height=50)
   icon1.place(x=10,y=200)
   icon1_lb=Button(buttons_label,text="Acceuil" ,bg='#040405',fg='#E5E4E2', border=1,width=15,height=1,font=('yu gothic ui',15,'bold'),command=passemode)
   icon1_lb.place(x=110,y=200)
#********************************************
   lien_maison=Image.open('.\\register_noir.png')
   photo2=ImageTk.PhotoImage(lien_maison)
   icon2=Button(buttons_label,image=photo2,bg='#3488FF', border=2,width=80,height=50)
   icon2.place(x=10,y=290)
   icon2_lb=Button(buttons_label,text="Enregistrer" ,bg='#040405',fg='#3488FF', border=1,width=15,height=1,font=('yu gothic ui',15,'bold'))
   icon2_lb.place(x=110,y=290)

#********************************************
   def passepara():
      register.destroy()
      parametre.main_win()
   lien_maison=Image.open('.\\parametre_grey.png')
   photo3=ImageTk.PhotoImage(lien_maison)
   icon3=Button(buttons_label,image=photo3,bg='#040405', border=2,width=80,height=50,command=passepara)
   icon3.place(x=10,y=380)
   icon3_lb=Button(buttons_label,text="Paramètre" ,bg='#040405',fg='#E5E4E2', border=1,width=15,height=1,font=('yu gothic ui',15,'bold'),command=passepara)
   icon3_lb.place(x=110,y=380)
   
#*******************************************
   def passeepx():
      register.destroy()
      exploitants.main_win()
   lien_maison=Image.open('.\\expl_grey.png')
   photo4=ImageTk.PhotoImage(lien_maison)
   icon4=Button(buttons_label,image=photo4,bg='#040405', border=2,width=80,height=50,command=passeepx)
   icon4.place(x=10,y=470)
   icon4_lb=Button(buttons_label,text="Exploitants" ,bg='#040405',fg='#E5E4E2', border=1,width=15,height=1,font=('yu gothic ui',15,'bold'),command=passeepx)
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
   label_bar=Label(register,text=tt,bg="black",fg="grey",width=140,height=2,font=('yu gothic ui',11,'bold'))
   label_bar.place(x=260,y=660)
#****************************************
   
   label_img=Label(register, bg="white",width=1050,height=33,font=('yu gothic ui',11,'bold'))
   label_img.place(x=320,y=0) 
#***************************************
#*************************************

   # plan=Label(label_img,bg="#DCDCDC",width=144,height=40)
   # plan.place(x=10,y=40)
   cpu=Image.open('.\\arriere.png')
   resize_cpu = cpu.resize((1050,660))
   photocpu=ImageTk.PhotoImage(resize_cpu)
   plan1=Label(label_img,image= photocpu,width=1050,height=660)
   plan1.place(x=0,y=0) 
   plan2=Label(plan1,bg="#808080",width=65,height=60)
   plan2.place(x=280,y=0)

  

   username_label=Label(plan2,text='Nom d\'utilisateur',bg='#808080',font=('yu gothic ui',13,'bold'),fg='#0E0E0E')
   username_label.place(x=60,y=60)
   
   username_entry=Entry(plan2,highlightthickness=0,relief= FLAT,bg='#808080',fg='black',font=('yu gothic ui',12,'bold'),cursor='xterm')
   username_entry.place(x=90,y=100,width=270)
   username_line=Canvas(plan2,width=300,height=2.0,bg='#bdb9b1',highlightthickness=0)
   username_line.place(x=65,y=130)
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
                    register.destroy()
            
        else:
            ms.showerror('Erreur', 'Veuillez remplir tous les champs de saisie')
    #*****************************************************
    #*******************************************
   def show_pswd():
        hide_code=Button(register,image=photo,bg='grey',activebackground='grey',cursor='hand2',bd=0,command=hide_pswd)
        hide_code.image=photo
        hide_code.place(x=980,y=345)
        password_entry.config(show='')

   def hide_pswd():
        show_code=Button(register,image=photo1,bg='grey',activebackground='grey',cursor='hand2',bd=0,command=show_pswd)
        show_code.image=photo1
        show_code.place(x=980,y=345)
        password_entry.config(show='*')

   show_code=Image.open('.\\eye_open.png')
   resize_image_show = show_code.resize((25,25))
   photo1=ImageTk.PhotoImage(resize_image_show)
   show_button=Button(register,image=photo1,bg='grey',activebackground='grey',cursor='hand2',bd=0,command=show_pswd)
   show_button.image=photo1
   show_button.place(x=980,y=345)
   hide_code=Image.open('.\\eye_close.png')
   resize_image_hide = hide_code.resize((25,25))
   photo=ImageTk.PhotoImage(resize_image_hide)

   def show_confi():
        hide_code=Button(register,image=photo,bg='grey',activebackground='grey',cursor='hand2',bd=0,command=hide_confi)
        hide_code.image=photo
        hide_code.place(x=980,y=475)
        confipass_entry.config(show='')

   def hide_confi():
        show_code=Button(register,image=photo1,bg='grey',activebackground='grey',cursor='hand2',bd=0,command=show_confi)
        show_code.image=photo1
        show_code.place(x=980,y=475)
        confipass_entry.config(show='*')

   show_code=Image.open('.\\eye_open.png')
   resize_image_show = show_code.resize((25,25))
   photo1=ImageTk.PhotoImage(resize_image_show)
   show_button=Button(register,image=photo1,bg='grey',activebackground='grey',cursor='hand2',bd=0,command=show_confi)
   show_button.image=photo1
   show_button.place(x=980,y=475)
   hide_code=Image.open('.\\eye_close.png')
   resize_image_hide = hide_code.resize((25,25))
   photo=ImageTk.PhotoImage(resize_image_hide)

   def retour_acceuil():
        register.destroy()
        exploitants.main_win()
   btn_fleche=Image.open('.\\play.png')
   resize_btn_fleche = btn_fleche.resize((30,30))
   photo_fleche=ImageTk.PhotoImage(resize_btn_fleche)
   login=Button(plan2,image=photo_fleche, font=('yu gothic ui',13,'bold'),width=80,height=60,bd=0,bg='#808080',cursor='hand2',activebackground='#040405',command=retour_acceuil)
   login.place(x=0,y=0)

    #*****************************************
   btn_inscrire=Image.open('.\\inscrire.png')
   photo_inscrire=ImageTk.PhotoImage(btn_inscrire)
   inscrire=Button(plan2,image=photo_inscrire, font=('yu gothic ui',13,'bold'),width=235,height=50,bd=0,bg='grey',cursor='hand2',activebackground='#040405',command=database)
   inscrire.place(x=110,y=570)
   register.mainloop()
# main_win()