#!/usr/bin/python

import tkinter as tk
import tkinter.ttk as ttk
from mfile import file_menu_add
from search import search_menu_add

menu_array = [file_menu_add, search_menu_add]
root = tk.Tk(className = " RFC Viewer")

menu = tk.Menu(root)

for menu_add in menu_array:
    m = tk.Menu(menu, tearoff=0)
    name = menu_add(m, root)
    menu.add_cascade(label=name, menu=m)

root.config(menu=menu)

# 运行主循环
root.mainloop()
