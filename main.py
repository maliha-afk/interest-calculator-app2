
from tkinter import *


screen=Tk()
screen.title("interest calculator")
screen.config(bg="springgreen2")
screen.geometry("500x500")

Label(screen,text="Welcome to Interest Calculator App",font=("Arial",15,"bold"),fg="white",bg="springgreen2").place(x=80,y=10)

amount_la=Label(screen,text="enter principle amount: ",font=("Arial",15,"bold"),fg="white",bg="springgreen2")
amount_la.place(x=10,y=70)
amount=Entry(screen,font=("Arial",15,"bold"))
amount.place(x=250,y=70,width=200)

time_la=Label(screen,text="enter duration in year: ",font=("Arial",15,"bold"),fg="white",bg="springgreen2")
time_la.place(x=10,y=110)
time=Entry(screen,font=("Arial",15,"bold"))
time.place(x=250,y=110,width=200)


interest_la=Label(screen,text="enter interest value: ",font=("Arial",15,"bold"),fg="white",bg="springgreen2")
interest_la.place(x=10,y=150)
intereste=Entry(screen,font=("Arial",15,"bold"))
intereste.place(x=250,y=150,width=200)

def calcint():
    try:
     interest=(int(amount.get()))*(int(time.get()))*(int(intereste.get()))/100
     totalamount=interest+(int(amount.get()))
     myamount.config(text=f"interest value: {interest} INR \n total amount: {totalamount} INR",fg="black")

    except:
       myamount.config(text=f"please enter valid input",fg="red")


def refresh():
    myamount.config(text="")
    

       

simpleintbut=Button(screen,text="calculate simple interest ",font=("Arial",15,"bold"),fg="white",bg="springgreen4",relief="raised",command=calcint)
simpleintbut.place(x=200,y=230)

resetb=Button(screen,text="RESET",font=("Arial",15,"bold"),fg="white",bg="springgreen4",relief="raised",command=refresh)
resetb.place(x=50,y=230)

myamount=Label(screen,font=("Arial",15,"bold"),fg="black",bg="springgreen2",relief="ridge",highlightthickness=2,highlightbackground="black")
myamount.place(x=100,y=300)


credit=Label(screen,text="Created By Atiya Maliha ",font=("Arial",7,"bold"),fg="black",bg="springgreen2")
credit.place(x=380,y=480)






screen.mainloop()