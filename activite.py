

# from tkinter import *
# from PIL import Image, ImageTk
# import time
# import activity2
# window = Tk()
# window.title("Activité report control")
# window.geometry("600x400")

# class Example(Frame):
#     def __init__(self, master, *pargs):
#         Frame.__init__(self, master, *pargs)
#         self.image = Image.open("./logo_arc.gif")
#         self.img_copy= self.image.copy()
#         self.background_image = ImageTk.PhotoImage(self.image)
#         self.background = Label(self, image=self.background_image)
#         self.background.pack(fill=BOTH, expand=YES)
#         self.background.bind('<Configure>', self._resize_image)

#     def _resize_image(self,event):
#         new_width = event.width
#         new_height = event.height
#         self.image = self.img_copy.resize((new_width, new_height))
#         self.background_image = ImageTk.PhotoImage(self.image)
#         self.background.configure(image =  self.background_image)


    
# e = Example(window)
# e.pack(fill=BOTH, expand=YES)
# def passage_window():
#     window.destroy()
#     activity2.main()
# window.after(3000,passage_window)
# window.mainloop()