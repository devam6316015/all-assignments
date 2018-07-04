# Q1. Create a dict with name and mobile number.Define a GUI interface using tkinter and pack the label and create a scrollbar 
# to scroll the list of keys in the dictionary.

import tkinter
from tkinter import *
import sys


dic={"devam":9594305348,"aman":84593745722,"shubham":94524592345,"satyam":87654322678,"tiwari":7564565503,"dheeraj":856453545343,"varinder":8435340034554,"rohit":9845384754,"tushar":94954378758,"rishab":83458439877,"nishant":6345666764,"mukesh":85422422455,"sartthak":84735822}
root=Tk()
root.title("window")
root.geometry("250x250")
root.resizable(True,True)
root.minsize(200,200)
root.maxsize(300,300)
root.configure(background="Beige")

f=Frame()
f.pack(side=RIGHT)
label=Label(f,text="MY LIST")
label.pack()

s=Scrollbar(f)
s.pack(side=RIGHT,fill=Y)
l=Listbox(f,yscrollcommand=s.set)
for x in dic:
	l.insert(END,x)
l.pack(side=LEFT,fill=BOTH)
s.config(command=l.yview())

root.mainloop()





#Q2. In the same tkinter file as created above, create a function to insert items into the dictionary.

# import tkinter
# from tkinter import *
# import sys


# dic={"devam":9594305348,"aman":84593745722,"shubham":94524592345,"satyam":87654322678,"tiwari":7564565503,"dheeraj":856453545343,"varinder":8435340034554,"rohit":9845384754,"tushar":94954378758,"rishab":83458439877,"nishant":6345666764,"mukesh":85422422455,"sartthak":84735822}
# def insert():
	# dic[entry1.get()]=int(entry2.get())
	# l.insert(END, '{}: {}'.format(entry1.get(), entry2.get()))
	# print(dic)
	
# root=Tk()
# root.title("window")
# root.geometry("250x250")
# root.resizable(True,True)
# root.minsize(200,200)
# root.maxsize(300,300)
# root.configure(background="Beige")

# entry1=Entry(root,width=20)
# entry1.pack()

# entry2=Entry(root,width=20)
# entry2.pack()

# b=Button(root,text='submit',width=5,command=insert)
# b.pack()

# f=Frame()
# f.pack(side=BOTTOM)

# s=Scrollbar(f)
# s.pack(side=RIGHT,fill=Y)
# l=Listbox(f,yscrollcommand=s.set)

# for key in dic:
    # l.insert(END, '{}: {}'.format(key, dic[key]))
	
# l.pack(side=LEFT,fill=BOTH)
# s.config(command=l.yview())

# root.mainloop()
