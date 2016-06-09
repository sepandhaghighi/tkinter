from tkinter import *
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
    root.mainloop()
        
            
    
