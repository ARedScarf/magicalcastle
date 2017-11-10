from tkinter import *
from tkinter import ttk

def calculate(*args):
   s=inputtext.get()
   output.delete(0, 30)
   output.insert(END, s)

def pressme(Event):
  
   output.delete(0, 130)
   s=inputtext.get()
   output.insert(END, s)
   f = open('hughfile.txt','w')
   f.write(s)
   f.close()


    
root = Tk()
root.title("Magical Castle")


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)




inputtext = StringVar()
enteredtext = ttk.Entry(mainframe, width=30, textvariable=inputtext)
enteredtext.grid(column=2, row=1, sticky=(W, E))

reply= StringVar()
output = ttk.Entry(mainframe, width=30, textvariable=reply)
output.grid(column=2, row=2, sticky=(W, E))


ttk.Button(mainframe, text="Reply", command=calculate).grid(column=3, row=3, sticky=W)


enteredtext.focus()
root.bind('<Return>', calculate)
root.bind('p', pressme)
root.mainloop()
