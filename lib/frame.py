"""This module serves mostly as a notebook for tkinter gui work"""

import os
from tkinter import *
from tkinter import ttk

meters: float = 0.0

def do_math(feet):
	"""Take an input of feet and convert it to the meter
	measurement down to the nearest hundredths position."""
	try:
		feet = float(feet)
		globals()[meters] = float(feet * 0.3048)
		return meters
	except TypeError:
		print('Wrong object type passed to <\'feet\'>')
		pass

def set_exit(exit, root):
	"""Set exit to True"""
	exit = True
	root.destroy
	return exit

exit= False
while not exit:
	root = Tk()
	frame = ttk.Frame(root, padding=5)
	feet: float = 0.0
	# Grid uses relative widget position requiring whitespace
	# declaration with manual position spacing, width calculation,
	# and space management based off of declared grid blocking.
	frame.grid(column=0, row=0, sticky=(N, W, E, S))
	ttk.Label(frame, text='').grid(column=1, row=1, columnspan=7, rowspan=2)
	ttk.Label(frame, text='').grid(column=1, row=3, columnspan=3, rowspan=3)
	ttk.Entry(frame, width=3, textvariable=feet).grid(column=4, row=3, columnspan=1, rowspan=3)
	ttk.Label(frame, text='Feet').grid(column=5, row=3, columnspan=1, rowspan=3)
	ttk.Label(frame, text='').grid(column=6, row=3, columnspan=2, rowspan=3)
	ttk.Button(frame, text='Exit', command=set_exit(exit, root)).grid(column=1, row=6, columnspan=1, rowspan=2)
	ttk.Label(frame, text='').grid(column=1, row=8, columnspan=1, rowspan=2)
	ttk.Label(frame, text='').grid(column=2, row=6, columnspan=1, rowspan=4)
	ttk.Label(frame, text='is equivalent to: ').grid(column=3, row=6, columnspan=2, rowspan=4)
	ttk.Label(frame, text=f'{meters}').grid(column=5, row=6, columnspan=1, rowspan=4)
	ttk.Label(frame, text='Meters.').grid(column=6, row=6, columnspan=1, rowspan=4)
	ttk.Button(frame, text='Calculate', command=do_math(feet)).grid(column=7, row=6, columnspan=1, rowspan=2)
	ttk.Label(frame, text='').grid(column=7, row=8, columnspan=1, rowspan=2)
	ttk.Label(frame, text='').grid(column=1, row=10, columnspan=7, rowspan=2)