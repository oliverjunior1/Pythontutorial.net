import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askretrycancel, showinfo

#create the root window
root = tk.Tk()
root.title('Tkinter Ok/Retry Dialog')
root.geometry('300x150')

#click event handler
def confirm():
    answer = askretrycancel(
        title='Connection Issue',
        message='The database server is unreachable. Do you want to retry?'
    )
    if answer:
        showinfo(
            title='Information',
            message='Attemp to connect to the database again.'
        )

ttk.Button(
    root,
    text='Connect to the Database Server',
    command=confirm   
).pack(expand=True)

root.mainloop()