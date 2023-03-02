
import tkinter as tk
import tkinter.ttk as ttk
from functools import partial
from tkinter import filedialog

def search_menu_add(menu, root):
    menu.add_command(label="Find...")
    menu.add_command(label="Find Next")
    return "Search"

