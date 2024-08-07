import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Slider Demo')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

current_value = tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())

slider_label = ttk.Label(
    root,
    text='Slider:'
)
slider_label.grid(
    column=0,
    row=0,
    sticky='w'
)
slider = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',
    command=slider_changed,
    variable=current_value
)
slider.grid(
    column=1,
    row=0,
    sticky='we'
)
current_value_label = ttk.Label(
    root,
    text='Current Value:'
)
current_value_label.grid(
    row=1,
    column=2,
    sticky='n',
    ipadx=10,
    ipady=10
)
value_label = ttk.Label(
    root,
    text=get_current_value()
)
value_label.grid(
    row=2,
    columnspan=2,
    sticky='n'
)
root.mainloop()