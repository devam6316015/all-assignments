# print("Q1. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.")
# import tkinter
# from tkinter import *
# import sys

# def exit():
	# print("Hello World")
	# sys.exit()
# root=Tk()
# b=Button(root,text="EXIT",width=20 ,command=exit)
# b.pack()
# root.mainloop()






# print("\nQ2. Write a python program to in the same interface as above and create a action when the button is click it will display some text.")
# import tkinter
# from tkinter import *
# import sys
# def prnt():
	# print("YoYo")
# root=Tk()
# b=Button(root,text="click!!!" ,width=10,height=2,bg="#111",fg="#777",command=prnt)
# b.pack()
# root.mainloop()






# print("\nQ3. Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.")
# import tkinter
# from tkinter import *
# import sys

# def exit():
	# sys.exit()
	
# def change():
	# label.config(text='chai pilo')
	
# root=Tk()
# root.title("window")
# root.geometry("300x300")

# label=Label(root,text='hello fraands')
# label.pack()


# f1=Frame(root)
# f1.pack()

# b1=Button(f1,text="exit",width=10,height=2,bg="#777",fg="#111",command=exit)
# b1.grid(row=0,column=0)
# b2=Button(f1,text="change",width=10,height=2,bg="#AAA",fg="#DDD",command=change)
# b2.grid(row=1,column=0)

# root.mainloop()





# print("\nQ4. Write a python program using tkinter interface to take an input in the GUI program and print it.")
# import tkinter
# from tkinter import *
# import sys
	
# def show():
	# print(listbox.get(ACTIVE))
# root=Tk()
# def exit():
	# sys.exit()
	
# listbox=Listbox(root)
# listbox.insert(1,'delhi')
# listbox.insert(2,'chandigarh')
# listbox.insert(3,'goa')
# listbox.insert(4,'mumbai')
# listbox.pack()

	
	
# b1=Button(root,text="enter",width=10,height=2,bg="#AAA", fg="#EEE",command=show)
# b1.pack()
# b2=Button(root,text="exit",width=10,height=2,bg="#AAA", fg="#EEE",command=exit)
# b2.pack()

# root.mainloop()