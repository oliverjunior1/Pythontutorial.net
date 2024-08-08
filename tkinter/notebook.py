import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('400x300')
root.title('Notebook Demo')

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

frame1 = ttk.Frame(notebook, width=400, height=200)
frame2 = ttk.Frame(notebook, width=400, height=200)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

notebook.add(frame1, text='General Information')
notebook.add(frame2, text='Profile')

root.mainloop()
