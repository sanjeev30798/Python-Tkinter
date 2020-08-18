from tkinter import * # importing the entire tkinter

#creating the application main window. 
root=Tk() 
root.title("Tkinter1") # appears on title bar

frame1=Frame(root) # first frame
#pack widget organises widget in the block
frame1.pack()

button=Button(frame1,text="button1",padx="2px",pady="3px",border="2px",relief=RAISED,activebackground="yellow",background="violetred")
button.pack(side=LEFT)

button=Button(frame1,text="button2",padx="2px",pady="3px",border="2.5px",relief=RAISED,activebackground="purple",background="cyan")
button.pack(side=RIGHT)

frame2=Frame() # for second frame
frame2.pack()

button=Button(frame2,text="button3",padx="2px",pady="3px",border="2px",relief=RAISED,activebackground="seagreen",background="greenyellow")
button.pack(side=LEFT)

button=Button(frame2,text="button4",padx="2px",pady="3px",border="2px",relief=RAISED,activebackground="oldlace",background="khaki1")
button.pack(side=RIGHT)

#Entering the event main loop
root.mainloop()