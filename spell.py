import tkinter
from tkinter import *
from textblob import TextBlob

root=Tk()
root.title("Mb Spelling Checker")
root.geometry("700x400")
root.config(background="blue")

def check():
    word=textfield.get()
    a=TextBlob(word)
    right=str(a.correct())

    cs=Label( root ,text="Correct text is :" , font=("poppins" ,20) ,bg="blue", fg="cyan" )
    cs.place(x=100 ,y=250)
    spell.config(text=right)

heading=Label(root , text= "Mb Spelling Checker", font=("Arial" , 30 , "bold") , bg= "gray", fg= "green")
heading.pack(pady=(50,0))

textfield=Entry(root , justify='center', width=30 , font=("poppins" ,25 ) , bg="white" , border=2)
textfield.pack(pady=10)
textfield.focus()

button=Button(root ,text="Check", font=("Times new roman" , 20,"bold") ,fg="white", bg="red" , command=check )
button.pack()

spell=Label( root ,font=("times new roman" , 20) ,bg="gray" , fg="green")
spell.place(x=350 ,y= 250)

root.mainloop()