import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk


def convert():
    mile = entry_int.get()
    km = mile * 1.61
    output_string.set(f"{km} km")


# window
window = tk.Tk()
window.title('Demo')
window.geometry('300x200')

# (Label)/title
title_label = ttk.Label(master=window, text="Miles to Kilometer", font='sans-serif  18 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master=window, padding=0.5)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text="Convert", command=convert)
entry.pack(side="left", padx=10)
button.pack(side="left")
input_frame.pack(pady=10)
output_string = tk.StringVar()
output_label = ttk.Label(master=window, text=f"output", font='sans-serif  12 bold', textvariable=output_string)
output_label.pack(pady=5)

window.mainloop()
