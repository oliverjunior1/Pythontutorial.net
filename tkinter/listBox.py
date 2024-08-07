# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo

# root = tk.Tk()
# root.title('Listbox')

# langs = ('Java', 'C#', 'C', 'C++', 'Python',
#          'Go', 'Javascript', 'PHP', 'Swift')

# var = tk.Variable(value=langs)

# listbox = tk.Listbox(
#     root,
#     listvariable=var,
#     height=6,
#     selectmode=tk.EXTENDED
# )
# listbox.pack(expand=True, fill=tk.BOTH)

# def items_selected(event):
#     selected_indices = listbox.curselection()
#     selected_langs = ','.join([listbox.get(i) for i in selected_indices])
#     msg = f'You selected: {selected_langs}'
#     showinfo(title='Information', message=msg)
    
# listbox.bind('<<ListboxSelect>>', items_selected)

# root.mainloop()
#####################################
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Listbox')

langs = ('Java', 'C#', 'C', 'C++', 'Python',
         'Go', 'Javasctipt', 'PHP', 'Swift')

var = tk.Variable(value=langs)

listbox = tk.Listbox(
    root,
    listvariable=var,
    height=6,
    selectmode=tk.EXTENDED
)
listbox.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

scrollbar = ttk.Scrollbar(
    root,
    orient=tk.VERTICAL,
    command=listbox.yview
)
listbox['yscrollcommand'] = scrollbar.set

scrollbar.pack(side=tk.LEFT, expand=True, fill=tk.Y)

def items_selected(event):
    selected_indices = listbox.curselection()
    selected_langs = ','.join([listbox.get(i) for i in selected_indices])
    msg = f'You selected: {selected_langs}'
    showinfo(title='Information', message=msg)

listbox.bind('<<LIstboxSelect>>', items_selected)

root.mainloop()