
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
text='Connexion'
heading=Label(lgn_frame,text=text,font=('yu gothic ui' ,25,'bold'),bg='#040405',fg='white')
heading.place(x=590,y=70)
side_image=Image.open('.\\user_key.png')
photo=ImageTk.PhotoImage(side_image)
side_image_label=Label(lgn_frame,image=photo,bg='#040405',width=400,height=450)
side_image_label.image=photo
side_image_label.place(x=40,y=130)

password_label=Label(lgn_frame,text='Mot de passe',bg='#040405',font=('yu gothic ui',13,'bold'),fg='#4f4e4d')
password_label.place(x=550,y=240)
password_entry=Entry(lgn_frame,highlightthickness=0,relief= FLAT,bg='#040405',fg='#6b6a69',font=('yu gothic ui',12,'bold'),cursor='xterm')
password_entry.place(x=570,y=280,width=270)
password_line=Canvas(lgn_frame,width=300,height=2.0,bg='#bdb9b1',highlightthickness=0)
password_line.place(x=550,y=314)
#*****************************************
paswd_icon=Image.open('.\\paswd_icon.png')
resize_image = paswd_icon.resize((25,25))
photo=ImageTk.PhotoImage(resize_image)
paswd_icon_label=Label(lgn_frame,image=photo,bg='#040405')
paswd_icon_label.image=photo
paswd_icon_label.place(x=540,y=280)
#*****************************************
btn_login=Image.open('.\\btn_login-w.png')

photo_login=ImageTk.PhotoImage(btn_login)

#*****************************************
login=Button(lgn_frame,image=photo_login, font=('yu gothic ui',13,'bold'),width=210,height=50,bd=0,bg='#040405',cursor='hand2',activebackground='#040405')
login.place(x=590,y=410)

def show():
    hide_code=Button(lgn_frame,image=photo,bg='#040405',activebackground='#040405',cursor='hand2',bd=0,command=hide)
    hide_code.image=photo
    hide_code.place(x=860,y=280)
    password_entry.config(show='')

def hide():
    show_code=Button(lgn_frame,image=photo1,bg='#040405',activebackground='#040405',cursor='hand2',bd=0,command=show)
    show_code.image=photo1
    show_code.place(x=860,y=280)
    password_entry.config(show='*')
show_code=Image.open('.\\eye_open.png')
resize_image_show = show_code.resize((25,25))
photo1=ImageTk.PhotoImage(resize_image_show)
show_button=Button(lgn_frame,image=photo1,bg='#040405',activebackground='#040405',cursor='hand2',bd=0,command=show)
show_button.image=photo1
show_button.place(x=860,y=280)

hide_code=Image.open('.\\eye_close.png')
resize_image_hide = hide_code.resize((25,25))
photo=ImageTk.PhotoImage(resize_image_hide)


window.mainloop()