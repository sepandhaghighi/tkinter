from tkinter import *
from random import *

def but_func(x,y):
    if list(but_array[x][y].config()["background"])[-1]=="black":
        but_array[x][y].config(bg="white")
    else:
        but_array[x][y].config(bg="black")
    if x+1<5:
        if list(but_array[x+1][y].config()["background"])[-1]=="black":
            but_array[x+1][y].config(bg="white")
        else:
            but_array[x+1][y].config(bg="black")
    if y+1<5:
        if list(but_array[x][y+1].config()["background"])[-1]=="black":
            but_array[x][y+1].config(bg="white")
        else:
            but_array[x][y+1].config(bg="black")
        
    if x-1>-1:
        if list(but_array[x-1][y].config()["background"])[-1]=="black":
            but_array[x-1][y].config(bg="white")
        else:
            but_array[x-1][y].config(bg="black")
        
    if y-1>-1:
        if list(but_array[x][y-1].config()["background"])[-1]=="black":
            but_array[x][y-1].config(bg="white")
        else:
            but_array[x][y-1].config(bg="black")
def rand_gen():
    rand_col=[]
    rand_row=[]
    for i in range(3):
        rand_col.append(randint(0,4))
        rand_row.append(randint(0,4))
    but_array[rand_row[0]][rand_col[0]].config(bg="white")
    but_array[rand_row[1]][rand_col[1]].config(bg="white")
    but_array[rand_row[2]][rand_col[2]].config(bg="white")
if __name__=="__main__":
    but_array=[]
    root=Frame()
    root.pack(expand=YES,fill=BOTH)
    #label_1=Label(root,text="salam")
    #label_1.pack()
    val=IntVar()
    for i in range(5):
        but_temp=[]
        frame=Frame(root)
        frame.pack(expand=YES,fill=BOTH)
        for j in range(5):
            but_temp.append(Button(frame,text="",command=lambda k=i, w=j:but_func(k,w),bg="black"))
            but_temp[j].pack(side=LEFT,expand=YES,fill=BOTH)
        but_array.append(but_temp)
    rand_gen()
    root.mainloop()
        
            
    
