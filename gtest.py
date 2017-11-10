from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkinter import filedialog

def saveit(*args):
   s=inputtext.get()
   output.delete(0, 30)
   output.insert(END, s)

   g = str(datetime.now())
   filename = g + ".txt"
   f = open(filename,'w')
   f.write(s)
   f.close()

def pressme(Event):
  
   output.delete(0, 130)
   s=inputtext.get()
   output.insert(END, s)

   g = str(datetime.now())
   filename = g + ".txt"
   f = open(filename,'w')
   f.write(s)
   f.close()

def fetchit():
   root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    
root = Tk()
root.title("Magical Castle")
# create a toplevel menu
menubar = Menu(root)

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Hughs secret command", command=fetchit)
filemenu.add_command(label="Save", command=saveit)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# display the menu
root.config(menu=menubar)

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


ttk.Button(mainframe, text="Reply", command=saveit).grid(column=3, row=3, sticky=W)


enteredtext.focus()
root.bind('<Return>', saveit)
root.bind('s', pressme)


w = Canvas(root, width=200, height=200)
w.create_oval(50,50,100,100)
w.grid(column=2, row=3, sticky=(W, E))

root.mainloop()
