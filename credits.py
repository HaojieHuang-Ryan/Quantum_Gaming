from tkinter import *
from functools import partial
from itertools import product

import main

class self:
	frame = None
	backBtn = None
	# labels
	labelTitle = None
	labelName = None

def reinit():
	clear()
	create()

def clear():
	if self.frame != None:
		for item in self.frame.winfo_children():
			item.destroy()

def create():
	self.labelTitle = Label(self.frame, text="CREDITS", font=("Arial", 20))
	self.labelTitle.pack(expand="True")
	self.labelName = Label(self.frame, text="Woo Hoo 2")
	self.labelName.pack(expand="True")
	self.backBtn = Button(self.frame, command=partial(back), text="back")
	self.backBtn.place(x=20, y=405, width=50, height=25)

def back():
	main.reinit()
	self.frame.pack_forget()
	main.self.frame.pack(expand='True')