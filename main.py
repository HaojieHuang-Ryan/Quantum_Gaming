from tkinter import *
from functools import partial
from itertools import product

import game
import credits
import help

class self:
	frame = None
	title = None
	startBtn = None
	helpBtn = None
	creditsBtn = None

def reinit():
	clear()
	create()

def clear():
	if self.frame != None:
		for item in self.frame.winfo_children():
			item.destroy()

def create():
	self.labelTitle = Label(self.frame, text="Find the Piggy hiding in Mud", font=("Arial", 20))
	self.labelTitle.pack(side='top')
	self.creditsBtn = Button(self.frame, command=partial(show, credits), text="credits")
	self.creditsBtn.pack(side='bottom')
	self.helpBtn = Button(self.frame, command=partial(show, help), text="help")
	self.helpBtn.pack(side='bottom')
	self.startBtn = Button(self.frame, command=partial(show, game), text="start")
	self.startBtn.pack(side='bottom')

def show(element):
	element.reinit()
	self.frame.pack_forget()
	element.self.frame.pack(fill='both', expand='True')