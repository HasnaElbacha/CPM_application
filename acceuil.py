from itertools import count
from tkinter import *
from PIL import ImageTk , Image
import login_name
import register
count=0
def main_home():
    window=Tk()
    window.geometry('1166x718')
    window.state('zoomed')
    window.resizable(0,0)
  
    
    our_images=[
        ".\\1.png",
        ".\\2.png",
        ".\\3.png",
        ".\\4.png"
    ]
    btn_login=Image.open('.\\btn_login2.png')
    photo_login=ImageTk.PhotoImage(btn_login)
    btn_inscrire=Image.open('.\\btn_register1.png')
    photo_inscrire=ImageTk.PhotoImage(btn_inscrire)
    def next():
        global count
        if count==3:
            count=0
        else:
            count=count+1
            print(count)
            images=Image.open(our_images[count])
            resize_image = images.resize((1400,740))
            photo=ImageTk.PhotoImage(resize_image)
            images_label=Label(window,image=photo,bg='#A2ADB9')
            images_label.image=photo
            images_label.place(x=0,y=0)
        window.after(3000,next)
        
        login=Button(images_label,image=photo_login, font=('yu gothic ui',13,'bold'),width=245,height=65,bd=0,cursor='hand2',activebackground='#A2ADB9',command=passlogin)
        login.place(x=555,y=275)
        inscrire=Button(images_label,image=photo_inscrire, font=('yu gothic ui',13,'bold'),width=245,height=65,bd=0,cursor='hand2',activebackground='#A2ADB9',command=passinscrire)
        inscrire.place(x=555,y=355)

#*****************************************
    def passlogin():
        window.destroy()
        login_name.main_login_name()

    
   

#*****************************************
    def passinscrire():
        window.destroy()
        register.main_register()
    
    next()
    window.mainloop()
# main_home()