# March 23, 2020
# from Udemy Tkinter Course amd Teclado and Tecladocode(github)
# Followed along, and practice, tried different items.
# Tried to use constructive notes.
#
# Needs Python3.8.+


import tkinter as tk

from tkinter import ttk

# ****************************************************************************
def greet():
    # Use get() method to retrieve StringVar() instance
    # If No user_name, then print Hello
    # user_name.get() retrives the variable from "textvariable=user_name"
    print(f"Hello, {user_name.get() or 'World'}!")

# ****************************************************************************

# Our Main or Parent Window
root = tk.Tk()
root.title("My Greeter")

# Create an Instance of StringVar() class
user_name = tk.StringVar() 

# Add a Label
name_Label = ttk.Label(root, text="Name:  ")
name_Label.pack(side="left", padx=(0, 10))

# Add a Label to get user_name
# width is used for the text entry box for number of characters
name_entry = ttk.Entry(root, width=20, textvariable=user_name) 
name_entry.pack(side="left")

name_entry.focus() 

# The Greet Button i.e. a Widget
greet_button = ttk.Button(root, text="Greet", command=greet)  
greet_button.pack(side="left", fill="x", expand=True)

# The Quit Button
quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="left", fill="x", expand=True)

# Call our Tkinterface to Start/Run
root.mainloop()

# Nothing below "root.mainloop" here runs until the tkinterface Exits


# Just a Debug itm to let me know that my code reached this point!
# When the tkinterface closes/Exits it returns top Python
print("Hey Robert --->>> Tkinter has Closed and returned to Python!")


