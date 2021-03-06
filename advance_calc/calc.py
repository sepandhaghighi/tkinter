from tkinter import *
import math
def frame_maker(root,side):
    temp=Frame(root)
    temp.pack(side=side,expand=YES,fill=BOTH)
    return temp
def button_maker(root,text,side,command):
    temp=Button(root,text=text,command=command,bg="gray40",fg="steelblue",font=("arial",10,"bold"))
    temp.pack(side=side,expand=YES,fill=BOTH)
    return temp
def calc(w):
    try:
        w.set(eval(w.get()))
    except:
        w.set("Error")
def tri_func(w,part="sin"):
    try:
        if radio.get()==2:
            temp= (float(w.get())*math.pi)/180
        else:
            temp=float(w.get())
        if part=="sin": 
            w.set(math.sin(temp))
        elif part=="cos":
            w.set(math.cos(temp))
        elif part=="tan":
            w.set(math.tan(temp))
        elif part=="fact":
            w.set(math.factorial(temp))
    except:
        w.set("Error")
def radio_change(v):
    if v==2:
        label_rad.config(text="DEG")
    else:
        label_rad.config(text="RAD")

object_list=["123","456","789"]
if __name__=="__main__":
    flag=0
    s=Frame(bg="gray40")
    s.pack(expand=YES,fill=BOTH)
    display=StringVar()
    radio=IntVar()
    disp=Entry(s,textvariable=display)
    disp.pack(side=TOP,expand=YES,fill=BOTH)
    frame_0=frame_maker(s,TOP)
    frame_1=frame_maker(s,TOP)
    frame_2=frame_maker(s,TOP)
    frame_3=frame_maker(s,TOP)
    frame_4=frame_maker(s,TOP)
    frame_5=frame_maker(s,TOP)
    frame_7=frame_maker(s,TOP)
    frame_6=frame_maker(s,TOP)
    radio_1=Radiobutton(frame_0,variable=radio,text="RAD",value=1,command=lambda :radio_change(1))
    radio_1.pack(anchor=W)
    radio_1.select()
    radio_2=Radiobutton(frame_0,variable=radio,text="DEG",value=2,command=lambda : radio_change(2))
    radio_2.pack(anchor=W)
    label_rad=Label(frame_0,text="RAD",fg="red")
    label_rad.pack(anchor=W)
    button_1=button_maker(frame_1,"1",LEFT,lambda w=display:w.set(w.get()+"1"))
    button_2=button_maker(frame_1,"2",LEFT,lambda w=display:w.set(w.get()+"2"))
    button_3=button_maker(frame_1,"3",LEFT,lambda w=display:w.set(w.get()+"3"))
    button_pi=button_maker(frame_1,"pi",LEFT,lambda w=display:w.set(w.get()+str(math.pi)))
    button_4=button_maker(frame_2,"4",LEFT,lambda w=display:w.set(w.get()+"4"))
    button_5=button_maker(frame_2,"5",LEFT,lambda w=display:w.set(w.get()+"5"))
    button_6=button_maker(frame_2,"6",LEFT,lambda w=display:w.set(w.get()+"6"))
    button_e=button_maker(frame_2,"e",LEFT,lambda w=display:w.set(w.get()+str(math.e)))
    button_7=button_maker(frame_3,"7",LEFT,lambda w=display:w.set(w.get()+"7"))
    button_8=button_maker(frame_3,"8",LEFT,lambda w=display:w.set(w.get()+"8"))
    button_9=button_maker(frame_3,"9",LEFT,lambda w=display:w.set(w.get()+"9"))
    button_dot=button_maker(frame_3,".",LEFT,lambda w=display:w.set(w.get()+"."))
    button_10=button_maker(frame_4,"+",LEFT,lambda w=display:w.set(w.get()+"+"))
    button_11=button_maker(frame_4,"-",LEFT,lambda w=display:w.set(w.get()+"-"))
    button_12=button_maker(frame_4,"/",LEFT,lambda w=display:w.set(w.get()+"/"))
    button_pow=button_maker(frame_4,"^",LEFT,lambda w=display:w.set(w.get()+"**"))
    button_13=button_maker(frame_5,"*",LEFT,lambda w=display:w.set(w.get()+"*"))
    button_14=button_maker(frame_5,"0",LEFT,lambda w=display:w.set(w.get()+"0"))
    button_15=button_maker(frame_5,"=",LEFT,lambda w=display:calc(w))
    button_sin=button_maker(frame_7,"Sin",LEFT,lambda w=display:tri_func(w,"sin"))
    button_cos=button_maker(frame_7,"Cos",LEFT,lambda w=display:tri_func(w,"cos"))
    button_tan=button_maker(frame_7,"Tan",LEFT,lambda w=display:tri_func(w,"tan"))
    button_fact=button_maker(frame_7,"fact",LEFT,lambda w=display:tri_func(w,"fact"))
    button_16=button_maker(frame_6,"Clear",LEFT,lambda w=display:w.set(""))
    label_1=Label(s,text="By Sepand Haghighi")
    label_1.pack(side=TOP,expand=YES,fill=BOTH)
    s.mainloop()
