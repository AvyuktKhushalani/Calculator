from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("570x600")
root.resizable(False,False)
root.configure(background = "black")

equation = ""
#Hello World

def Show(value):
    global equation
    equation+=value
    label_result.config(text=equation)


def clear():
    global equation
    equation = ""
    label_result.config(text=equation)


def solve():
    global equation
    result = ""
    if equation != "":
        try:
            equation = equation.replace("X", "*")
            result = eval(equation)
        
        except:
            result = "Error"
            equation = ""

        label_result.config(text=result)    



def exit():
    root.destroy()



label_result = Label(root,width=25,height=2,bg="grey10",fg="white",text="",font=("arial",30))
label_result.place(x=-5,y=7.5)

Button(root,text="EXIT",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="midnight blue",command=lambda: exit() ).place(x=10,y=110)
Button(root,text="C",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="midnight blue",command=lambda: clear()).place(x=150,y=110)
Button(root,text="/",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="grey10",command=lambda: Show("/")).place(x=290,y=110)
Button(root,text="X",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="grey10",command=lambda: Show("X")).place(x=430,y=110)

Button(root,text="7",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="grey10",command=lambda: Show("7")).place(x=10,y=210)
Button(root,text="8",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="grey10",command=lambda: Show("8")).place(x=150,y=210)
Button(root,text="9",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="grey10",command=lambda: Show("9")).place(x=290,y=210)
Button(root,text="+",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="grey10",command=lambda: Show("+")).place(x=430,y=210)

Button(root,text="4",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="grey10",command=lambda: Show("4")).place(x=10,y=310)
Button(root,text="5",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="grey10",command=lambda: Show("5")).place(x=150,y=310)
Button(root,text="6",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="grey10",command=lambda: Show("6")).place(x=290,y=310)
Button(root,text="-",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="grey10",command=lambda: Show("-")).place(x=430,y=310)

Button(root,text="1",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="grey10",command=lambda: Show("1")).place(x=10,y=410)
Button(root,text="2",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="grey10",command=lambda: Show("2")).place(x=150,y=410)
Button(root,text="3",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="grey10",command=lambda: Show("3")).place(x=290,y=410)

Button(root,text="0",width=11,height=1,font=("arial",30),bd=1,fg="white",bg="grey10",command=lambda: Show("0")).place(x=10,y=510)

Button(root,text=".",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="grey10",command=lambda: Show(".")).place(x=290,y=510)
Button(root,text="=",width=5,height=3,font=("arial",30),bd=1,fg="white",bg="dark orange",command=lambda: solve()).place(x=430,y=415)

root.mainloop()