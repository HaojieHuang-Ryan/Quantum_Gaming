import game
import main
import credits
import help
from tkinter import *

root = Tk()
root.geometry('400x430')
root.title('Find the Piggy hiding in Muds')

main.self.frame = Frame(root, width=400, height=200)
main.self.frame.pack_propagate(0)
credits.self.frame = Frame(root)
help.self.frame = Frame(root)
main.create()
game.self.frame = Frame(root)
main.self.frame.pack(expand='True')

root.mainloop()