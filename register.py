from tkinter import *
from PIL import ImageTk , Image

window=Tk()
window.geometry('1166x718')
window.state('zoomed')
window.resizable(0,0)
window.configure(background="black")
class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)



        self.image = Image.open(".\\4.png")
        self.img_copy= self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
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

lgn_frame=Frame(window,bg='#040405',width=950,height=600)
lgn_frame.place(x=200,y=70)
text='S\'inscrire'
heading=Label(lgn_frame,text=text,font=('yu gothic ui' ,25,'bold'),bg='#040405',fg='white')
heading.place(x=400,y=70)
pen_image=Image.open('.\\pen.png')
resize_image_pen = pen_image.resize((50,50))
photo=ImageTk.PhotoImage(resize_image_pen)
pen_image_label=Label(lgn_frame,image=photo,bg='#040405',width=400,height=450)
pen_image_label.image=photo
pen_image_label.place(x=650,y=290)
#************************************************************************************
username_label=Label(lgn_frame,text='Nom d\'utilisateur',bg='#040405',font=('yu gothic ui',13,'bold'),fg='#4f4e4d')
username_label.place(x=150,y=140)
username_entry=Entry(lgn_frame,highlightthickness=0,relief= FLAT,bg='#040405',fg='#6b6a69',font=('yu gothic ui',12,'bold'),cursor='xterm')
username_entry.place(x=170,y=180,width=270)
username_line=Canvas(lgn_frame,width=300,height=2.0,bg='#bdb9b1',highlightthickness=0)
username_line.place(x=150,y=214)
#*****************************************
user_icon=Image.open('.\\user_icon.png')
resize_image_user = user_icon.resize((25,25))
photo=ImageTk.PhotoImage(resize_image_user)
user_icon_label=Label(lgn_frame,image=photo,bg='#040405')
user_icon_label.image=photo
user_icon_label.place(x=145,y=180)
#*****************************************
#************************************************************************************
password_label=Label(lgn_frame,text='Mot de passe',bg='#040405',font=('yu gothic ui',13,'bold'),fg='#4f4e4d')
password_label.place(x=150,y=230)
password_entry=Entry(lgn_frame,highlightthickness=0,relief= FLAT,bg='#040405',fg='#6b6a69',font=('yu gothic ui',12,'bold'),cursor='xterm')
password_entry.place(x=170,y=270,width=270)
password_line=Canvas(lgn_frame,width=300,height=2.0,bg='#bdb9b1',highlightthickness=0)
password_line.place(x=150,y=304)
#*****************************************
password_icon=Image.open('.\\paswd_icon.png')
resize_image_pass = password_icon.resize((25,25))
photo=ImageTk.PhotoImage(resize_image_pass)
password_icon_label=Label(lgn_frame,image=photo,bg='#040405')
password_icon_label.image=photo
password_icon_label.place(x=145,y=270)
#*****************************************
#************************************************************************************
confipass_label=Label(lgn_frame,text='Confirmation de mot de passe',bg='#040405',font=('yu gothic ui',13,'bold'),fg='#4f4e4d')
confipass_label.place(x=150,y=320)
confipass_entry=Entry(lgn_frame,highlightthickness=0,relief= FLAT,bg='#040405',fg='#6b6a69',font=('yu gothic ui',12,'bold'),cursor='xterm')
confipass_entry.place(x=170,y=360,width=270)
confipass_line=Canvas(lgn_frame,width=300,height=2.0,bg='#bdb9b1',highlightthickness=0)
confipass_line.place(x=150,y=394)
#*****************************************
confipass_icon=Image.open('.\\paswd_icon.png')
resize_image_pass = confipass_icon.resize((25,25))
photo=ImageTk.PhotoImage(resize_image_pass)
confipass_icon_label=Label(lgn_frame,image=photo,bg='#040405')
confipass_icon_label.image=photo
confipass_icon_label.place(x=145,y=360)
#*****************************************
#************************************************************************************
email_label=Label(lgn_frame,text='Email',bg='#040405',font=('yu gothic ui',13,'bold'),fg='#4f4e4d')
email_label.place(x=150,y=410)
email_entry=Entry(lgn_frame,highlightthickness=0,relief= FLAT,bg='#040405',fg='#6b6a69',font=('yu gothic ui',12,'bold'),cursor='xterm')
email_entry.place(x=170,y=450,width=270)
email_line=Canvas(lgn_frame,width=300,height=2.0,bg='#bdb9b1',highlightthickness=0)
email_line.place(x=150,y=484)
#*****************************************
email_icon=Image.open('.\\email_icon.png')
resize_image_email = email_icon.resize((25,25))
photo=ImageTk.PhotoImage(resize_image_email)
email_icon_label=Label(lgn_frame,image=photo,bg='#040405')
email_icon_label.image=photo
email_icon_label.place(x=145,y=450)
#*****************************************
btn_inscrire=Image.open('.\\btn_inscrire.png')
photo_inscrire=ImageTk.PhotoImage(btn_inscrire)
inscrire=Button(lgn_frame,image=photo_inscrire, font=('yu gothic ui',13,'bold'),width=235,height=50,bd=0,bg='#040405',cursor='hand2',activebackground='#040405')
inscrire.place(x=590,y=310)
#*******************************************
def show_pswd():
    hide_code=Button(lgn_frame,image=photo,bg='#040405',activebackground='#040405',cursor='hand2',bd=0,command=hide_pswd)
    hide_code.image=photo
    hide_code.place(x=420,y=275)
    password_entry.config(show='')

def hide_pswd():
    show_code=Button(lgn_frame,image=photo1,bg='#040405',activebackground='#040405',cursor='hand2',bd=0,command=show_pswd)
    show_code.image=photo1
    show_code.place(x=420,y=275)
    password_entry.config(show='*')
show_code=Image.open('.\\eye_open.png')
resize_image_show = show_code.resize((25,25))
photo1=ImageTk.PhotoImage(resize_image_show)
show_button=Button(lgn_frame,image=photo1,bg='#040405',activebackground='#040405',cursor='hand2',bd=0,command=show_pswd)
show_button.image=photo1
show_button.place(x=420,y=275)
hide_code=Image.open('.\\eye_close.png')
resize_image_hide = hide_code.resize((25,25))
photo=ImageTk.PhotoImage(resize_image_hide)

def show_confi():
    hide_code=Button(lgn_frame,image=photo,bg='#040405',activebackground='#040405',cursor='hand2',bd=0,command=hide_confi)
    hide_code.image=photo
    hide_code.place(x=420,y=365)
    confipass_entry.config(show='')

def hide_confi():
    show_code=Button(lgn_frame,image=photo1,bg='#040405',activebackground='#040405',cursor='hand2',bd=0,command=show_confi)
    show_code.image=photo1
    show_code.place(x=420,y=365)
    confipass_entry.config(show='*')
show_code=Image.open('.\\eye_open.png')
resize_image_show = show_code.resize((25,25))
photo1=ImageTk.PhotoImage(resize_image_show)
show_button=Button(lgn_frame,image=photo1,bg='#040405',activebackground='#040405',cursor='hand2',bd=0,command=show_confi)
show_button.image=photo1
show_button.place(x=420,y=365)
hide_code=Image.open('.\\eye_close.png')
resize_image_hide = hide_code.resize((25,25))
photo=ImageTk.PhotoImage(resize_image_hide)
window.mainloop()