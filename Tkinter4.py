from tkinter import *

def calculate():
    num1=number1.get() # method to fetch data from entry box
    num2=number2.get()
    num1=int(num1) # converting to int as value is in string form
    num2=int(num2)
    num1=num1*(num2+100)/100 # calculating selling price
    num1=str(num1)
    label3=Label(top,text=num1,background="yellow",height=2,width=5,font={"Georgia",25,"bold"}).place(x=120,y=120) #display bill amount or selling price
    number1.set("")
    number2.set("") #resetting value

#creating the application main window.  
top=Tk()
top.title("Tkinter4") #name of the file or title of window
top.geometry("400x200") #size of small window

number1=StringVar() #declaring variable for storing price
number2=StringVar() #declaring variable for profit %

label1=Label(top,text="Cost",background="magenta2",font=("Candara",14,"italic"),width=10,padx="5px",pady="3.5px",justify=CENTER,relief=RIDGE,border="4px").grid(row=2,column=1)
label2=Label(top,text="Profit%",background="tan1",font=("Georgia",12,"italic"),width=8,padx="12px",pady="3.5px",justify=CENTER,relief=RIDGE,border="4px").grid(row=8,column=1)

entry1=Entry(top,textvariable=number1,width=25,fg="black",relief=RAISED,border="1.55px").place(x=140,y=15)
entry2=Entry(top,textvariable=number2,width=25,fg="black",relief=RAISED,border="1.55px").place(x=140,y=50)


but1=Button(top,activebackground="Seagreen3",text="Result",padx="3px",pady="5px",font={"Calibiri",16,"italic"},border="2px",relief=RAISED,command=calculate)
but1.place(x=25,y=100) #placing the result button
 
top.mainloop()