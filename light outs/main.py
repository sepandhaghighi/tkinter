from tkinter import *
from random import *
import sys
def win_check():
    for i in range(5):
        for j in range(5):
            if list(but_array[i][j].config()["background"])[-1]=="white":
                return False
    return True
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
    if win_check()==True:
        label_1.config(text="You Win The Game")
    label_turn.config(text=str(int(list(label_turn.config()["text"])[-1])+1))        
    
def rand_gen():
    rand_col=[]
    rand_row=[]
    for i in range(3):
        rand_col.append(randint(0,4))
        rand_row.append(randint(0,4))
    but_array[rand_row[0]][rand_col[0]].config(bg="white")
    but_array[rand_row[1]][rand_col[1]].config(bg="white")
    but_array[rand_row[2]][rand_col[2]].config(bg="white")
def reset():
    for i in range(5):
        for j in range(5):
            but_array[i][j].config(bg="black")
    rand_gen()   
if __name__=="__main__":
    but_array=[]
    program=Tk()
    program.title("Lights Out")
    root=Frame(program)
    root.pack(expand=YES,fill=BOTH)
    label_1=Label(root,text="Play . . .")
    label_1.pack()
    label_frame=Frame(root)
    label_frame.pack(expand=YES,fill=BOTH,side=TOP)
    label_show=Label(label_frame,text="Click : ")
    label_show.pack(side=LEFT)
    label_turn=Label(label_frame,text="0")
    label_turn.pack(side=RIGHT)
    
    val=IntVar()
    for i in range(5):
        but_temp=[]
        frame=Frame(root)
        frame.pack(expand=YES,fill=BOTH)
        for j in range(5):
            but_temp.append(Button(frame,text="",command=lambda k=i, w=j:but_func(k,w),bg="black"))
            but_temp[j].pack(side=LEFT,expand=YES,fill=BOTH)
        but_array.append(but_temp)
    frame_exit=Frame(root)
    frame_exit.pack(expand=YES,fill=BOTH,side=TOP)
    frame_reset=Frame(root)
    frame_reset.pack(expand=YES,fill=BOTH,side=TOP)
    but_exit=Button(frame_exit,text="Exit",command= lambda : program.destroy())
    but_exit.pack(expand=YES,side=TOP,fill=BOTH)
    but_reset=Button(frame_reset,text="Reset",command=lambda : reset())
    but_reset.pack(expand=YES,fill=BOTH,side=TOP)
    rand_gen()
    root.mainloop()
        
            
    
