"""Store and execute the variables and functions that define how
the accompanying modules are utilized. It also serves to initialize,
describe, and build the interface users will be interacting with."""

import os
import re
import platform
import subprocess
from nput import *
from frame import *
from roper import *
from tkinter import *
from smartjack import *
from pathlib import Path
from tkinter import ttk

scope = (''
        )
debug = True

# Absolute pathing variables
_current_file = Path(__file__).resolve()
_module_dir = _current_file.parent
_root_dir = _module_dir.parent

# Creates a basic cli with text-wrapping, a non-
# standard font, and customizable coloration options (3 themes).
# The cli should display printed text to the user, distinguish
# between file upload modes and text input modes, and allow for
# the input of a large number of words/characters without slowing
# down.
var_track = ''
root = Tk()
smartjack = SmartJack(debug)
nput = nParse(variable_mode=True, variable=var_track, debug=debug)
frame = CommandLine(root, nput, debug)
commands = {}
for command in commands:
        frame.parser.add_command(command)
var_track = frame.cmd_str
roper_cube_list = []
roper_pack_list = []
frame.draw_fields()
frame.run_loop()