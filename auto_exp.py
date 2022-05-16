from atexit import register
from tkinter import *
from PIL import ImageTk , Image
from tkinter import messagebox as ms
import tkinter as tk
from tkinter import ttk
from click import command
from numpy import place
from tkinter.ttk import Progressbar
import exp_table
import admin_register
import exp_mode
import exp_exploitants
import pandas as pd
comp=True
def main_win():
   
   secondfenetre =Tk()
   secondfenetre.state("zoomed")
   secondfenetre.config(background="#FFFFFF")
   buttons_label = Label(secondfenetre, bg="black" ,height=237,width=45)
   buttons_label.place(x=0,y=0)

   #***************************************
   user_icon=Image.open('.\\compte_.png')
   resize_image = user_icon.resize((40,40))
   photo=ImageTk.PhotoImage(resize_image)
   user_icon_label=Label(buttons_label,image=photo,bg='#040405')
   user_icon_label.image=photo
   user_icon_label.place(x=50,y=50)
   txt="-----"
   compte=Label(secondfenetre,text=txt,bg="black",fg="grey",width=14,height=1,font=('yu gothic ui',16,'bold'))
   compte.place(x=95,y=55)
  
#********************************************
   
   def changecolor():
      global comp
      if(comp==True):
            def saisire():
               secondfenetre.destroy()
               exp_table.main_win()
            saisir=Button(label_img,text="Saisir",font=('yu gothic ui' ,20,'bold'),bg='black',fg='#3488FF',width=20,height=1, border=10 ,cursor='hand2',takefocus=0,command=saisire)
            saisir.place(x=290,y=240) 
            comp=False
            saisir.after(1000,changecolor)
            
      else:
            def saisire():
               secondfenetre.destroy()
               exp_table.main_win()
            saisir=Button(label_img,text="Saisir",font=('yu gothic ui' ,20,'bold'),bg='#3488FF',fg='black',width=20,height=1, border=10 ,cursor='hand2',takefocus=0,command=saisire)
            saisir.place(x=290,y=240) 
            comp=True
            saisir.after(1000,changecolor)
   def passregister():
      secondfenetre.destroy()
      admin_register.main_win()
   def passeacc():
      secondfenetre.destroy()
      exp_mode.main_win()
   lien_maison=Image.open('.\\maison_noir.png')
   photo1=ImageTk.PhotoImage(lien_maison)
   icon1=Button(buttons_label,image=photo1,bg='#3488FF', border=2,width=80,height=50,command=passeacc)
   icon1.place(x=10,y=270)
   icon1_lb=Button(buttons_label,text="Acceuil" ,bg='#040405',fg='#3488FF', border=1,width=15,height=1,font=('yu gothic ui',15,'bold'),command=passeacc)
   icon1_lb.place(x=110,y=270)
#*******************************************
   def passeexp():
      secondfenetre.destroy()
      exp_exploitants.main_win()
   lien_maison=Image.open('.\\expl_grey.png')
   photo4=ImageTk.PhotoImage(lien_maison)
   icon4=Button(buttons_label,image=photo4,bg='#040405', border=2,width=80,height=50,command=passeexp)
   icon4.place(x=10,y=360)
   icon4_lb=Button(buttons_label,text="Exploitants" ,bg='#040405',fg='#E5E4E2', border=1,width=15,height=1,font=('yu gothic ui',15,'bold'),command=passeexp)
   icon4_lb.place(x=110,y=360)
#*******************************************
   user_icon=Image.open('.\\logo_back_remove.gif')
   resize_image = user_icon.resize((170,120))
   photo=ImageTk.PhotoImage(resize_image)
   user_icon_label=Label(buttons_label,image=photo,bg='#040405')
   user_icon_label.image=photo
   user_icon_label.place(x=70,y=580)
#******************************************
   tt="ARC_2022"
   label_bar=Label(secondfenetre,text=tt,bg="black",fg="grey",width=140,height=2,font=('yu gothic ui',11,'bold'))
   label_bar.place(x=260,y=660)
#****************************************
   label_img=Label(secondfenetre,bg="white",width=1050,height=33,font=('yu gothic ui',11,'bold'))
   label_img.place(x=320,y=0) 
   tk.Label(label_img, text="Enrgistrement automatique", fg="#3488FF",bg="white" ,font=("Helvetica",25,"bold")).place(x=300, y=5)
   tk.Label(label_img,bg="#3488FF",width=200,height=0).place(x=0, y=70)
   frame1 = tk.LabelFrame(label_img, text="Données")
   frame1.place(x=200,y=120,height=450, width=650)
   button2 = tk.Button(label_img, text="Load File")
   button2.place(rely=0.65, relx=0.30)
   tv1 = ttk.Treeview(frame1)
   tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).
   treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
   treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
   tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
   treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
   treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget
   """If the file selected is valid this will load the file into the Treeview"""
   file_path =".\\script.csv"
   try:
        excel_filename = r"{}".format(file_path)
        if excel_filename[-4:] == ".csv":
            df = pd.read_csv(excel_filename)
        else:
            df = pd.read_excel(excel_filename)

   except ValueError:
        tk.messagebox.showerror("Information", "The file you have chosen is invalid")
   except FileNotFoundError:
        tk.messagebox.showerror("Information", f"No such file as {file_path}")

   tv1.delete(*tv1.get_children())
   tv1["column"] = list(df.columns)
   tv1["show"] = "headings"
   for column in tv1["columns"]:
      tv1.heading(column, text=column) # let the column heading = column name
    
      df.dropna(subset = ["Adresse IP"], inplace=True)
      df.dropna(subset = ["Date"], inplace=True)
      df.dropna(subset = ["Heures"], inplace=True)
      df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
      for row in df_rows:
         tv1.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
   def actualiser():
      secondfenetre.destroy()
      main_win()
   btnActualiser=Button(label_img,text="Actualiser",command=actualiser)
   btnActualiser.place(x=500,y=590)
   secondfenetre.mainloop()
# main_win()