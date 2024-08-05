# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Label Widget Demo')

# root.mainloop()

###################################

# import tkinter as tk
# from tkinter.ttk import Label

# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Label Widget Demo')

# label = Label(root, text='This is a label')
# label.pack(ipadx=10, ipady=10)

# root.mainloop()

###################################

# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Label Widget Demo')

# label = ttk.Label(
#     root,
#     text='A Label with the Helvetica font',
#     font=('Helvetica', 14)
# )
# label.pack(ipadx=10, ipady=10)

# root.mainloop()

###################################
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Label Widget Image')

photo = tk.PhotoImage(file='C:\\Users\\Olive\\Downloads\\Visual Studio Code\\Pythontutorial.net\\tkinter\\python-logo.png')
image_label=ttk.pack(
    root,
    image=photo,
    padding = 5
)
image_label.pack()
root.mainloop()