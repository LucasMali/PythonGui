from tkinter import *
from tkinter import ttk

# create the parent
root = Tk()

# make a button
button = ttk.Button(root, text = 'Click Me')

# Geometry packager.
button.pack()

# sets properties
button.config(text = 'Push Me')

# This will return the dictionary of the config
button.config()

# Set a label
ttk.Label(root, text = "Button").pack()