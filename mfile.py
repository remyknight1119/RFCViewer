
import tkinter as tk
import tkinter.ttk as ttk
from functools import partial
from tkinter import filedialog

def add_tab(file_path, notebook, blank_text_box):
    # 打开文件并读取内容
    with open(file_path, "r") as file:
        content = file.read()

    notebook.pack()

    #sidebar = ttk.Frame(notebook, width=200)
    #sidebar.pack(side=tk.LEFT, fill=tk.Y)

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


def open_file(notebook, blank_text_box):
    file_path = filedialog.askopenfilename()
    if file_path:
        add_tab(file_path, notebook, blank_text_box)

def close_file(notebook, blank_text_box):
    current_tab_index = notebook.index(notebook.select())
    notebook.forget(current_tab_index)
    blank_text_box.pack(expand=True, fill=tk.BOTH)


def file_menu_add(menu, root):
    blank_text_box = tk.Text(root)
    blank_text_box.pack(expand=True, fill=tk.BOTH)
    notebook = ttk.Notebook(root)
    menu.add_command(label="Open", command=partial(open_file, notebook, blank_text_box))
    menu.add_command(label="Close", command=partial(close_file, notebook, blank_text_box))
    menu.add_separator()
    menu.add_command(label="Exit", command=root.quit)
    return "File"

