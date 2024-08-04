# import tkinter as tk

# root = tk.Tk()

# root.mainloop()

###################################

# import tkinter as tk

# root = tk.Tk()
# root.title('Tkinter Window Demo ')
# root.geometry('600x400+50+50')

# root.mainloop()
###################################

# import tkinter as tk

# root = tk.Tk()
# root.title('Tkinter Window - Center')

# window_width = 300
# window_height = 200

# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()

# center_x = int(screen_height/2 - window_width/2)
# center_y = int(screen_height/2 - window_width/2)

# root.geometry(f'{window_width}x{window_height}+ {center_x} + {center_y}')

# root.mainloop()

###################################

# import tkinter as tk

# root = tk.Tk()
# root.title('Tkinter Window Demo')
# root.geometry('600x400+50+50')
# root.resizable(False, False)
# root.attributes('-alpha', 0.5)

# root.mainloop()
###################################

# import tkinter as tk

# root = tk.Tk()
# root.title('Tkinter Window Demo')
# root.geometry('300x200+50+50')
# root.resizable(0,0)
# root.attributes('-topmost', 1)

# root.mainloop()
###################################

import tkinter as tk

root = tk.Tk()
root.title('Tkinter Window Demo')
root.geometry('300x200+50+50')
root.resizable(False, False)
root.iconbitmap('/assets/pythontutorial.ico')

root.mainloop()
