from tkinter import *


tk = Tk()

l = []


def reset():
    l = []
    label2.config(text=l)
    
def stop():
    somma = 0
    print("u stopped the program")
    
    for i in l:
        try:
            somma += float(i)
        except:
            print("could not parse", i)
    label.config(text="sum: {0}".format(somma))
    

def add(event):
    l.append(e.get())
    e.delete(0, END)
    label2.config(text=l)





b2 = Button(tk, text="reset", command=reset)
b2.pack()

b = Button(tk, text="click for end", command=stop)
b.pack()

label2 = Label(tk, text=l)
label2.pack()

e = Entry(tk)
e.pack()

label = Label(tk, text="sum: 0")
label.pack()

e.bind("<Return>", add)




tk.mainloop()
