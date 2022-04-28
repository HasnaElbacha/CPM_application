from cProfile import label
from pydoc import importfile
from tkinter import *
from tkinter.ttk import Progressbar
import sys
import file_page
from turtle import width
from tkinter.filedialog import askopenfilename


def main():
   secondfenetre =Tk()
   secondfenetre.state("zoomed")
   secondfenetre.config(background="#363D4D")
   def pass_file():
       
       fichier = open("networkinfo.log", "r")
       content = fichier.read()
       fichier.close()
      #  content="ggggg"
       label_file=Label(secondfenetre,bg="green" ,text=content,width=70,height=50)
       label_file.grid(column=1, row=1, padx=6, pady=6, sticky="nw")
       label_file.place(x=200,y=0)
       
   buttons_label = Label(secondfenetre, bg="yellow" ,width=30,height=90)
   buttons_label.place(x=0,y=0)
   bouton1=Button(buttons_label, text="ouvrer",width=30,height=11,command=lambda:pass_file())
   bouton2=Button(buttons_label, text="Fermer",width=30,height=11)
   bouton3=Button(buttons_label, text="quiter",width=30,height=11)
   bouton4=Button(buttons_label, text="JSP",width=30,height=11)
   bouton1.pack()
   bouton2.pack()
   bouton3.pack()
   bouton4.pack()
   secondfenetre.mainloop()
   file_page.commandsoutput()
   