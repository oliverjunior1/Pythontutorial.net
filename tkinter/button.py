# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Button Demo')

# exit_button = ttk.Button(
#     root,
#     text='Exit',
#     command=lambda:root.quit()
# )
# exit_button.pack(
#     ipadx=5,
#     ipady=5,
#     expand=True
# )
# root.mainloop()
###################################
# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo

# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Image Button Demo')

# def download_clicked():
#     showinfo(
#         title='Information',
#         message='Download button clicked!'
#     )

# download_icon = tk.PhotoImage(file='C:\\Users\\Olive\\Downloads\\Visual Studio Code\\Pythontutorial.net\\tkinter\\python-logo.png')
# download_button = ttk.Button(
#     root,
#     image=download_icon,
#     command=download_clicked
# )

# download_button.pack(
#     ipadx=5,
#     ipad=5,
#     expand=True
# )

# root.mainloop()

###################################

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Image Button Demo')

def download_clicked():
    showinfo(
        title = 'Information',
        message='Download button clicked!'
    )

download_icon = tk.PhotoImage(file='')

download_button = ttk.Button(
    root,
    image=download_icon,
    text='Download',
    compound=tk.LEFT,
    command=download_clicked
)
download_button.pack(
    ipadx= 5,
    ipady=5,
    expand=True
)
root.mainloop()
