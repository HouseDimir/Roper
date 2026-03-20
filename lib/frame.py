"""This module serves mostly as a notebook for tkinter gui work"""

from tkinter import *
from tkinter import ttk

class ScrollLabel(ttk.Frame):
	# Some code that iterates over a data storage file to get
	# command line entries in memory saving process; assign
	# scrollwheel to changing the location of the file that
	# currently has focus, displaying lines above/below the
	# focus point into the ScrollLabel. 
	def __init__(self):
		"""Initialize ScrollLabel widet"""
		# Initialize reference variables
		self.file_enum = []
		self.filepath = '' # Some code that pulls exact filepath
		self.center = 0
		self.top_bound = center - 20 if center >= 20 else 0 
		self.bottom_bound = center + 20
		self.text_dict = {}

	def scroll_down(self):
		"""Shift the ScrollLabel center downwards one."""
		if center < len(file_enum):
			for pos in file_enum:
				if pos == self.center + 1:
					self.center = pos
		elif center == len(file_enum):
			pass
		else:
			raise ValueError(f'{self}.focus escaped upper bounds.')
		self.text_update()

	def scroll_up(self):
		"""Shift the ScrollLabel center upwards one."""
		if len(self.file_enum) == 0:
			pass
		else:
			for pos in range(0, len(self.file_enum)):
				if pos == self.focus - 1:
					self.center = pos
		self.text_update()

	def text_update(self):
		"""Update the text variables to refelct the lines shown
		by self.top_bound and self.bottom_bound."""
		# Track key names from file_enum
		text_list = []
		key_list = []
		value_list = []
		with open(self.filepath, 'r', encoding='utf-8') as file:
			self.file_enum = []
			num = 0
			for line in file:
				self.file_enum.append(num)
				line = file.readline()
				text_list.append(line)
			for pos in self.file_enum:
				while pos >= self.top_bound and pos <= self.bottom_bound:
					key_list.append(pos)
					value_list.append(text_list[pos])
			while len(key_list) == len(value_list)
			self.text_dict = dict(zip(key_list, value_list))

class CommandLine():
	# Some code holds the various hierarchy to build a
	# command-line interface with basic indeterminate progress
	# bar.
	def __init__(self, root, nparse):
		"""Initialize and build a CommandLine() instance
		Ex. cli = CommandLine(Tk(), nParse())"""
		# Initialize reference variables 
		self.exit = False
		self.root = root
		self.parser = nparse
		self.cmd_str = StringVar()
		# Initialize ttk widgets
		self.cmd_entry = ttk.Entry(width=(self.window_width-self.p_bt))
		# Initalize TK widgets

	def exit(self):
		"""Destroy root object"""
		return self.root.destroy

	def parse_cmd(self):
		# Some code that calls the nParse func on call
		self.parser.variable_mode = True
		self.parser.variable = self.cmd_str
		self.parser.parse_input()

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(round(0.3048 * value, 4))
    except ValueError:
        pass

root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
ttk.Button(mainframe, text="Quit", command=root.destroy).grid(column=3, row=4, sticky=(W, S))

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()