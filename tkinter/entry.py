import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('300x150')
root.resizable(False, False)
root.title('Sign in')

email = tk.StringVar()
password = tk.StringVar()

def loging_clicked():
    '''
    callback when the login button clicked
    '''
msg = f'You entered email: {email.get()} and password: {password.get()}'
showinfo(
    title='Information',
    message=msg
)

signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)

email_label = ttk.Label(signin, text='Email Address:')
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

password_label = ttk.Label(signin, text='Password:')
password_label.pack(fill='x', expand=True)

password_entry = ttk.Label(signin, textvariable=password, show='*')
password_entry.pack(fill='x', expand=True)

login_button = ttk.Button(signin, text='Login', command=loging_clicked)
login_button.pack(fill='x', expand=True, pady=10)

root.mainloop()