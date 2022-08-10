from tkinter import *
from functools import partial
from itertools import product

import main

class self:
	frame = None
	backBtn = None
	# labels
	labelTitle = None
	labelHelp = None

def reinit():
	clear()
	create()

def clear():
	if self.frame != None:
		for item in self.frame.winfo_children():
			item.destroy()

def create():
	self.labelTitle = Label(self.frame, text="HELP", font=("Arial", 20))
	self.labelTitle.pack(expand="True")
	self.labelHelp = Label(self.frame, text="1. To win the game, find the piggy hiding in muds\n\n2. There are three types of muds:\n- trap muds(1/2 possibility being tarpped)\n- empty muds(1/2 possibility showing around trap count)\n- a piggy mud(the target)\n\n3. Once getting traped, you lose\n\n4. The spell helps to figure out\nwhether two blocks are the same type")
	self.labelHelp.pack(expand="True")
	self.backBtn = Button(self.frame, command=partial(back), text="back")
	self.backBtn.place(x=20, y=405, width=50, height=25)

def back():
	main.reinit()
	self.frame.pack_forget()
	main.self.frame.pack(expand='True')