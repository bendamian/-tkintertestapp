import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Demo')
window.geometry('300x200')

# (Label)/title
title_label = ttk.Label(master=window, text="Miles to Kilometer", font='sans-serif  18 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master=window, padding=0.5)
entry = ttk.Entry(master=input_frame)
button = ttk.Button(master=input_frame, text="Convert")
entry.pack(side="left", padx=10)
button.pack(side="left")
input_frame.pack(pady= 10)

output_label = ttk.Label(master=window,text=f"output")
output_label.pack()

window.mainloop()
