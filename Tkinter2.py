from tkinter import *
from PIL import ImageTk, Image
import os
import webbrowser # for opening url

def func1():
    cnf=messagebox.askokcancel("Confirm","Do you want to send mail?")
    if(cnf==True):
        webbrowser.open_new_tab("https://mail.google.com/")
    
    
def func2():
    cnf=messagebox.askokcancel("Confirm","Do you want to login to desktop whatsapp?")
    if(cnf==True):
        webbrowser.open_new_tab("https://web.whatsapp.com/")
    
def func3():
    cnf=messagebox.askokcancel("Confirm","Do you want to go to GeeksforGeeks?")
    if(cnf==True):
        webbrowser.open_new_tab("https://www.geeksforgeeks.org/")

def func4():
    cnf=messagebox.askokcancel("Confirm","Do you want to go to Github?")
    if(cnf==True):
        webbrowser.open_new_tab("https://github.com/")
def func5():
    cnf=messagebox.askokcancel("Confirm","Do you want to go to instagram?")
    if(cnf==True):
        webbrowser.open_new_tab("https://facebook.com/")

def func6():
    cnf=messagebox.askokcancel("Confirm","Do you want to go to Gaana.com?")
    if(cnf==True):
        webbrowser.open_new_tab("https://gaana.com/")



#creating the application main window.   
top=Tk() 
top.geometry("350x250") #geometry manager organizes the widgets to the specific x and y coordinates

top.title("Tkinter2") # name of the window

#button to open Gmail
b1=Button(top,font="5px",text="Gmail",padx="27px",background="Gold",activebackground="green",foreground="crimson",pady="10px",border="3px",command=func1,relief=RAISED)
b1.place(x=25,y=30)

#button to open whatsaap
b2=Button(top,font="6px",text="Whatsapp",padx="16px",background="tomato",activebackground="green",foreground="black",pady="10px",border="3px",command=func2,relief=RAISED)
b2.place(x=25,y=100)

#button to open GFG
b3=Button(top,font="1.5px",text="GeeksforGeeks",background="thistle1",padx="5px",pady="10px",activebackground="green",foreground="purple",border="3.5px",command=func3,relief=RAISED)
b3.place(x=165,y=30)

#button to open Github
b4=Button(top,font="5px",text="Github",padx="29px",background="royalblue",pady="10px",activebackground="green",foreground="wheat1",border="3.5px",command=func4,relief=RAISED)
b4.place(x=165,y=100)

#button to open facebook
b5=Button(top,font="5px",text="Facebook",padx="16px",background="cornsilk2",pady="10px",activebackground="green",foreground="magenta",border="3px",command=func5,relief=RAISED)
b5.place(x=25,y=175) 

#button to open Gaana
b6=Button(top,font="5px",text="Gaana",padx="29px",pady="10px",background="burlywood1",activebackground="green",foreground="brown3",border="3.5px",command=func6,relief=RAISED)
b6.place(x=165,y=175)


top.mainloop()
