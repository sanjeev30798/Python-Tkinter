from tkinter import * # importing the entire tkinter

#creating the application main window. 
top=Tk()
top.title("Tkinter3") # Renaming of title bar
top.geometry("400x250")

name=Label(top,text="Name").place(x=40,y=30)
email=Label(top,text="Email-id").place(x=40,y=70)
phone=Label(top,text="Contact No.").place(x=40,y=110)

# space or box for entering details
e1=Entry(top,relief=RAISED,border="2.5px").place(x=115,y=30)
e2=Entry(top,relief=RAISED,border="2.5px").place(x=115,y=70)
e3=Entry(top,relief=RAISED,border="2.5px").place(x=115,y=110)

submit=Button(top,text="Submit",padx="2px",pady="1.75px",activebackground="maroon",background="bisque",foreground="darkviolet",border="1.2px")
submit.place(x=40,y=140) #button to accept

#Entering the event main loop
top.mainloop()