#!/usr/bin/env python3

import tkinter as tk
import time
def update_time():
    """ A funtion a update time """
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

# Open the window 
root = tk.Tk()
# Title for the app
root.title("Digital Clock")

# Edit some changes   
clock_label = tk.Label(root, font=('Arial', 100), bg='#222c2c', fg='white')
clock_label.pack(fill='both', expand=True)

# Update time accordingly 
update_time()

root.mainloop()

