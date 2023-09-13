from clickDATA import *
from tkinter import *

fill = 0 #check if you already have data saved
reset = 0
cliks = clik

#resets data in clickDATA.py
def DATASAVE():
    f = open("clickDATA.py","w")
    f.write("clik = "+str(cliks))
    f.close()

def DATARESET():
    f = open("clickDATA.py","w")
    f.write("clik = 0")
    f.close()


#set up tkinter
root = Tk()
root.title("clIKER")


e = Entry(root, width=25, borderwidth=5)
e.grid(row=0, column=0, columnspan=1, padx=5, pady=5)

e.insert(0, "Clicks: "+str(cliks))

#ADDS clicks and updates and saves to other file
def clickButton():
    global cliks
    cliks = cliks + 1
    
    e.delete(0,END)
    e.insert(0,"Clicks: "+str(cliks))
    DATASAVE()
    #print(cliks)
    return

#Resets cliks on both this and data save file
def resetButton():
    global cliks
    DATARESET()
    cliks = 0
    e.delete(0,END)
    e.insert(0,"Clicks: "+str(cliks))
    return
#button define
button_1 = Button(root, text="CLICK", padx=30, pady=30, command=clickButton)
button_r = Button(root, text="RESET", padx=20, pady=20, command=resetButton)
#put buttons on screen

button_1.grid(row=1, column=0)
button_r.grid(row=2, column=0)




root.mainloop()
