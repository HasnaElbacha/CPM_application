
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

username_label=Label(lgn_frame,text='Nom d\'utilisateur',bg='#040405',font=('yu gothic ui',13,'bold'),fg='#4f4e4d')
username_label.place(x=550,y=240)
username_entry=Entry(lgn_frame,highlightthickness=0,relief= FLAT,bg='#040405',fg='#6b6a69',font=('yu gothic ui',12,'bold'),cursor='xterm')
username_entry.place(x=570,y=280,width=270)
username_line=Canvas(lgn_frame,width=300,height=2.0,bg='#bdb9b1',highlightthickness=0)
username_line.place(x=550,y=314)
#*****************************************
user_icon=Image.open('.\\user_icon.png')
resize_image = user_icon.resize((25,25))
photo=ImageTk.PhotoImage(resize_image)
user_icon_label=Label(lgn_frame,image=photo,bg='#040405')
user_icon_label.image=photo
user_icon_label.place(x=540,y=280)
#*****************************************
btn_login=Image.open('.\\btn_login-w.png')

photo_login=ImageTk.PhotoImage(btn_login)

#*****************************************
login=Button(lgn_frame,image=photo_login, font=('yu gothic ui',13,'bold'),width=210,height=50,bd=0,bg='#040405',cursor='hand2',activebackground='#040405')

login.place(x=590,y=410)
window.mainloop()

