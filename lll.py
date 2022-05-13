from tkinter import *
#read the file
file = open("file.txt", "r")
courses = file.readlines()
print(courses)

root = Tk()

for course in courses:
    temp_text = courses
    Label(root, text=temp_text,bg="red",fg="black",width=300).pack()

mainloop()