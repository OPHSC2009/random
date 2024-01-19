import random
from tkinter import*
root=Tk()
root.geometry("500x500")
root.title("list")

lbl_1=Label(root)
lbl_1.place(relx=0.5,rely=0.3,anchor=CENTER)



lbl_2=Label(root)
lbl_2.place(relx=0.5,rely=0.6,anchor=CENTER)

def create():
    rl=random.sample(range(1,100),10)
    lbl_1["text"]="Random list = "+str(rl)
    
    rl.sort()
    lbl_2["text"]="List in ascending order = "+str(rl)
        
        
        
        

btn=Button(root,text="Generate Random List",command=create)
btn.place(relx=0.5,rely=0.8,anchor=CENTER)

root.mainloop()


