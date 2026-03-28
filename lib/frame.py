"""This module defines the ScrollLabel() class and how it functions
as well as initializes and organized the GUI interface run by __main__"""

import os
import sys
from time import *
from tkinter import *
from pathlib import Path
from tkinter import ttk

scope = (''
        )
# Absolute pathing variables
_current_file = Path(__file__).resolve()
_module_dir = _current_file.parent
_root_dir = _module_dir.parent

# Implement inherited class methods

class ScrollLabel(ttk.Frame):
	"""Widget which iterates over a data storage file to get
	command line entries in memory saving process; assign
	scrollwheel to scroll_up and scroll_down to enable 
	changing the location of the file that currently has focus,
	displaying lines above/below the focus point into the
	ScrollLabel."""
	def __init__(self, parent, debug=False):
		"""Initialize ScrollLabel widget."""
		# Initialize reference variables
		super().__init__(parent)
		self.debug = debug
		self.file_enum = []
		self.filepath = str(_root_dir) + '/bin/ref/scrollable.txt'
		try:
			open(self.filepath, 'x', encoding='utf-8')
		except FileExistsError:
			os.remove(self.filepath)
			open(self.filepath, 'x', encoding='utf-8')
		self.center_line = 0
		self.top_bound = self.center_line - 20 if self.center_line >= 20 else 0 
		self.bottom_bound = self.center_line + 20
		# Initialize the label for the displayed lines
		self.str_label = ''
		self.sys_txt = ttk.Label(self, text=f'{self.str_label}')
		self.sys_txt.grid(column=0, row=0, sticky=(W, E))
		self.widgets = self.grid_slaves()
		self.grid_configure(column=0, sticky=(N, W, E))
		self.grid(column=0, row=0)
		if self.debug:
			print('Finished initializing ScrollLabel()')

	def add_line(self, line):
		"""Add passed line to reference file and return it for reference."""
		if self.debug:
			print(f'Writing line to {self.filepath}:\n{line}')
		with open(self.filepath, 'a', encoding='utf-8') as file:
			file.write(line+'\n')
			file.flush()
			file.close()
		return

	def destroy_file(self):
		"""Delete the command data storage file."""
		try:
			if self.debug:
				print(f'Destroying {self.filepath}')
			os.remove(self.filepath)
		except FileNotFoundError:
			pass

	def clear_labels(self):
		"""Empty the label_list before running self.text_update."""
		# Empty the current label_list in mem-conserving manner.
		if self.debug:
			print('Emptying ScrollLabel().label_list.')
		for child in self.winfo_children():
			child.destroy()

	def pos_check(self, pos):
		"""Return True when the passed int is inside the bounds."""
		bool_ = True if pos >= self.top_bound and pos <= self.bottom_bound else False
		if self.debug:
			print(f'Checking file position {pos} is valid: {bool_}')
		return True if bool_ else False

	def on_scroll(self, event=None):
		"""Shift the ScrollLabel center upwards or downwards one
		based on the event().delta return value"""
		if event.delta > 0:
			if len(self.file_enum) <= 41:
				if self.debug:
					print('Too few commands to scroll.')
				pass
			else:
				if self.debug:
					print('Scrolling command field up once.')
				for pos in self.file_enum:
					if pos == (self.center_line - 1):
						self.center_line -= 1
		else:
			if self.center_line < len (self.file_enum):
				if self.debug:
					print('Scrolling command field down once.')
				for pos in self.file_enum:
					if pos == (self.center_line + 1):
						self.center_line += 1
			elif self.center_line == len(self.file_enum):
				pass
			else:
				raise ValueError(f'{self}.focus escaped upper bounds.')
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
			# Build the total file to be referenced and have the
			# necessary data selected
			if self.debug:
				print('Storing all text, one moment please.')
			for line in file:
				if self.debug:
					print(f'{line}')
				text_list.append(line)
				if self.debug:
					print(f'text_list: {text_list}\n')
			for index, str_ in enumerate(text_list):
				if self.pos_check(index):
					if self.debug:
						print(f'{self.str_label}\n'
							f'{index}\n'
							f'{str_}\n')
					self.str_label = self.str_label + f'{str_}\n'
					if self.debug:
						print(f'{self.str_label}')
			self.sys_txt.configure(text=f'{self.str_label}')

class CommandLine():
	"""Builds out the gui for the command line portion of the
	Roper application, with scalable drawing."""
	def __init__(self, root, nparse, debug=False):
		"""Initialize and build a CommandLine() instance
		Ex. cli = CommandLine(Tk(), nParse())"""
		# Initialize reference variables 
		self.exit = False
		self.debug = debug
		self.root = root
		self.parser = nparse
		self.cmd_str = StringVar()
		# Initialize ttk widgets
		self.f_main = ttk.Frame(self.root)
		self.f_sys = ttk.Frame(self.f_main)
		self.bar = ttk.Progressbar(self.f_main)
		self.f_user = ttk.Frame(self.f_main)
		self.cmd_bt = ttk.Button(self.f_user, text='Run', command=self.parse_cmd)
		self.exit_bt = ttk.Button(self.f_user, text='Exit', command=self.close)
		self.cmd_entry = ttk.Entry(self.f_user, width=75, textvariable=self.cmd_str)
		# Initalize custom widget
		self.text_field = ScrollLabel(self.f_sys, self.debug)
		if self.debug:
			print('Finished initializing CommandLine().')

	def draw_fields(self):
		"""Grid out the various widgets across the application."""
		if self.debug:
			print('Plotting objects to grids.')
		self.root.columnconfigure(0, weight=1)
		self.root.rowconfigure(0, weight=1)
		self.f_main.columnconfigure(0, weight=1)
		self.f_main.rowconfigure(0, weight=1)
		self.f_main.grid(column=0, row=0, sticky=(N, W, E, S))
		self.f_sys.columnconfigure(0, weight=1)
		self.f_sys.rowconfigure(0, weight=5)
		self.f_sys.grid(column=0, row=0, sticky=(N, W, E))
		self.bar.columnconfigure(0, weight=1)
		self.bar.rowconfigure(1, weight=3)
		self.bar.grid(column=0, row=1, sticky=(W, E))
		self.f_user.columnconfigure(0, weight=1)
		self.f_user.rowconfigure(2, weight=2)
		self.f_user.grid(column=0, row=2, sticky=(W, E, S))
		self.cmd_bt.columnconfigure(1, weight=1)
		self.cmd_bt.rowconfigure(0, weight=1)
		self.cmd_bt.grid(column=1, row=0, sticky=(E, S))
		self.exit_bt.columnconfigure(2, weight=1)
		self.exit_bt.rowconfigure(0, weight=1)
		self.exit_bt.grid(column=2, row=0, sticky=(E, S))
		self.cmd_entry.columnconfigure(0, weight=8)
		self.cmd_entry.rowconfigure(0, weight=8)
		self.cmd_entry.grid(column=0, row=0, sticky=(W, S))
		self.text_field.columnconfigure(0, weight=1)
		self.text_field.rowconfigure(0, weight=1)
		self.text_field.grid(column=0, row=0, sticky=(N, W, E, S))
		# Grid everything with some padding to prevent crowding.
		if self.debug:

			print('Padding all objects in grid.\n'
				f'{self.f_main.winfo_children()}')
		for child in self.f_main.winfo_children():
			# if child == self.text_field:
			# 	child.grid_configure(padx=1, pady=5)
			# else:
			# 	child.grid_configure(padx=5, pady=5)
			child.grid_configure(padx=5, pady=5)
		if self.debug:
			print('Assigning hotkeys.')
		self.root.protocol('WM_DELETE_WINDOW', self.close)
		self.root.bind('<MouseWheel>', self.text_field.on_scroll)
		self.root.bind('<Return>', self.parse_cmd)
		self.root.bind('<Escape>', self.close)
		self.cmd_entry.focus_set()
		if self.debug:
			print('Finished plotting objects to grids.')

	def close(self, event=None):
		if self.debug:
			print('Quitting root software.')
		self.text_field.destroy_file()
		self.root.quit()
		sleep(1)

	def parse_cmd(self, event=None):
		"""Set the parser.variable to cmd_str value and call the
		parser.parse_input() method to parse the input value."""
		if self.debug:
			print('Transforming input, then parsing to <{command:{*args}}> format.')
		self.text_field.add_line(self.cmd_str.get())
		self.text_field.clear_labels()
		self.text_field.text_update()
		self.parser.variable_mode = True
		self.parser.variable = self.cmd_str.get()
		self.parser.parse_input()

	def run_loop(self):
		"""Run the mainloop."""
		if self.debug:
			print('Starting GUI framework, self-destructing upon quit().')
		self.root.mainloop()
		self.root.destroy()
		sys.exit(1)