from tkinter import *

if __name__=="__main__":
    but_array=[]
    root=Frame()
    root.pack(expand=YES,fill=BOTH)
    for i in range(5):
        but_temp=[]
        frame=Frame(root)
        frame.pack(expand=YES,fill=BOTH)
        for i in range(5):
            but_temp.append(Button(frame,text="",command=None,bg="blackss"))
            but_temp[i].pack(side=LEFT,expand=YES,fill=BOTH)
        but_array.append(but_temp)
    root.mainloop()
        
            
    
