#!/usr/bin/python

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog

root = tk.Tk(className = " RFC Viewer")

blank_text_box = tk.Text(root)
blank_text_box.pack(expand=True, fill=tk.BOTH)

notebook = ttk.Notebook(root)
notebook.pack()

def add_tab(file_path):
    # 打开文件并读取内容
    with open(file_path, "r") as file:
        content = file.read()

    frame = ttk.Frame(notebook)

    blank_text_box.pack_forget()
    notebook.pack_forget()

    # 创建文本框对象
    text_box = tk.Text(frame)
    text_box.insert(tk.END, content)
    text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # 创建滚动条对象
    scroll_bar = ttk.Scrollbar(frame, command=text_box.yview)
    text_box.config(yscrollcommand=scroll_bar.set)
    scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

    # 添加子页到 Notebook 中
    notebook.add(frame, text=file_path)
    notebook.pack(expand=True, fill=tk.BOTH)

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        add_tab(file_path)

menu = tk.Menu(root)

# 添加一个下拉菜单
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Close")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=file_menu)

search_menu = tk.Menu(menu, tearoff=0)
search_menu.add_command(label="Find...")
search_menu.add_command(label="Find Next")
menu.add_cascade(label="Search", menu=search_menu)

root.config(menu=menu)

# 运行主循环
root.mainloop()
