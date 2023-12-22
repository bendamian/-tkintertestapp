import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Demo')
window.geometry('300x200')

# (Label)/title
title_label = ttk.Label(master=window, text="Miles to Kilometer",font='sans-serif  18 bold')
title_label.pack()



window.mainloop()
