#!/usr/bin/env python

"""
Provides the following functions:
 - popupmsg: Creates a popup message with an "Okay" button
 - select_folder: Pops up a message prompting to select a folder, then opens a window to select a directory
 - select_file: Pops up a message prompting to select a file, then opens a window to select a file
"""

import tkinter as tk
import tkinter.filedialog as tkf


# Create a popup dialog window with a confirmation button
def popupmsg(window_title, msg):
    popup = tk.Tk()
    popup.wm_title(window_title)
    label = tk.Label(popup, text=msg)
    label.pack(side="top", fill="x", padx=25, pady=25)
    ok_button = tk.Button(popup, text="Okay", command=popup.destroy)
    ok_button.pack()
    popup.mainloop()


# Prompt the user to select a folder
def select_folder(window_title, msg):
    popupmsg(window_title, msg)
    dialog = tk.Tk()
    dialog.withdraw()
    dialog.update()
    selected = tkf.askdirectory(title=window_title)
    dialog.destroy()
    return selected


# Prompt the user to select a file
def select_file(window_title, msg):
    popupmsg(window_title, msg)
    dialog = tk.Tk()
    dialog.withdraw()
    dialog.update()
    selected = tkf.askopenfilename(title=window_title)
    dialog.destroy()
    return selected


