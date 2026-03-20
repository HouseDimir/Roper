"""This module serves mostly as a notebook for tkinter gui work"""

from tkinter import *
from tkinter import ttk

scope = (''
        )

class ScrollLabel(ttk.Frame):
	"""Widget which iterates over a data storage file to get
	command line entries in memory saving process; assign
	scrollwheel to scroll_up and scroll_down to enable 
	changing the location of the file that currently has focus,
	displaying lines above/below the focus point into the
	ScrollLabel."""
	def __init__(self):
		"""Initialize ScrollLabel widget"""
		# Initialize reference variables
		self.file_enum = []
		self.filepath = '' # Some code that pulls exact filepath
		self.center = 0
		self.top_bound = center - 20 if center >= 20 else 0 
		self.bottom_bound = center + 20
		self.text_dict = {}
		# Initialize the labels for the displayed lines
		self.label_list = []
		self.gridconfigure(column=0, weight=1)

	def add_line(self, line):
		"""Add passed line to reference file and return it for reference."""
		with open(self.filepath, 'a', encoding='utf-8') as file:
			file.write(line)
			file.flush()
			file.close()
		self.text_update()
		return line

	def _pos_check(self, pos):
		"""Return True when the passed int is inside the bounds."""
		return True if pos >= top_bound and pos <= bottom_bound else False

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
		# Track necessary file data
		text_list = []
		key_list = []
		value_list = []
		# Open the file containing all content printed to the
		# system console
		with open(self.filepath, 'r', encoding='utf-8') as file:
			self.file_enum = []
			num = 0
			# Build the total file to be referenced and have the
			# necessary data selected
			for line in file:
				self.file_enum.append(num)
				line = file.readline()
				text_list.append(line)
			# Build the lists from which to build the text_dict
			for pos in self.file_enum:
				while self._pos_check(pos):
					key_list.append(pos)
					value_list.append(text_list[pos])
			if len(key_list) == len(value_list):
				self.text_dict = dict(zip(key_list, value_list))
			else:
				raise ValueError('Unmatched list length when trying to zip text.')
			# Build the various labels from the available text_dict
			for num in range(0, len(text_dict.values())) and value in text_dict.values():
				self.label_list.append(ttk.Label(self, text=f'{value}'))
			# Set the label positions for the text lines.
			for num in range(0, len(label_list)) and label in self.label_list:
				label.grid(column = 0, row=num)

class CommandLine():
	"""Builds out the gui for the command line portion of the
	Roper application, with scalable drawing."""
	def __init__(self, root, nparse):
		"""Initialize and build a CommandLine() instance
		Ex. cli = CommandLine(Tk(), nParse())"""
		# Initialize reference variables 
		self.exit = False
		self.root = root
		self.parser = nparse
		self.cmd_str = StringVar()
		# Initialize ttk widgets
		self.f_main = ttk.Frame(self.root)
		self.f_sys = ttk.Frame(self.f_main)
		self.bar = ttk.ProgressBar(self.f_main)
		self.f_user = ttk.Frame(self.f_main)
		self.cmd_bt = ttk.Button(self.f_user, text='Run', command=self.parse_cmd)
		self.exit_bt = ttk.Button(self.f_user, text='Exit', command=self.exit)
		self.cmd_entry = ttk.Entry(f_user, width=25)
		# Initalize custom widget
		self.text_field = ScrollLabel(self.f_sys)
		# Grid out the various widgets across the application
		self.root.columnconfigure(0, weight=1)
		self.root.rowconfigure(0, weight=1)
		self.f_main.columnconfigure(0, weight=1)
		self.f_main.rowconfigure(0, weight=1)
		self.f_sys.columnconfigure(0, weight=1)
		self.f_sys.rowconfigure(0, weight=5)
		self.bar.columnconfigure(0, weight=1)
		self.bar.rowconfigure(1, weight=3)
		self.f_user.columnconfigure(0, weight=1)
		self.f_user.rowconfigure(2, weight=2)
		self.cmd_bt.columnconfigure(1, weight=1)
		self.cmd_bt.rowconfigure(0, weight=1)
		self.exit_bt.columnconfigure(2, weight=1)
		self.exit_bt.rowconfigure(0, weight=1)
		self.cmd_entry.columnconfigure(0, weight=8)
		self.cmd_entry.rowconfigure(0, weight=1)
		self.text_field.columnconfigure(0, weight=1)
		self.text_field.rowconfigure(0, weight=1)
		# Grid everything with some padding to prevent crowding.
		for child in f_main.winfo_children(): 
			child.grid_configure(padx=5, pady=5)
		root.bind('<ScrollWheelUp>', self.text_field.scroll_up)
		root.bind('<ScrollWheelDown>', self.text_field.scroll_down)
		root.bind('<Return>', self.parse_cmd)
		# Run the root
		self.root.mainloop()

	def exit(self):
		"""Destroy root object."""
		return self.root.destroy

	def parse_cmd(self):
		"""Set the parser.variable to cmd_str value and call the
		parser.parse_input() method to parse the input value."""
		self.parser.variable_mode = True
		self.parser.variable = self.cmd_str
		self.parser.parse_input()