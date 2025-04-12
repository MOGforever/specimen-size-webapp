# c_gui_app.py

import tkinter as tk
from tkinter import messagebox
import sqlite3

def calculate_real_size(microscope_size, magnification):
    return microscope_size / magnification

def store_data(username, specimen, microscope_size, actual_size):
    conn = sqlite3.connect("specimens.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS records
                 (username TEXT, specimen TEXT, microscope_size REAL, actual_size REAL)''')
    c.execute("INSERT INTO records VALUES (?, ?, ?, ?)",
              (username, specimen, microscope_size, actual_size))
    conn.commit()
    conn.close()

def submit():
    try:
        username = entry_username.get()
        specimen = entry_specimen.get()
        microscope_size = float(entry_microscope_size.get())
        magnification = float(entry_magnification.get())
        actual_size = calculate_real_size(microscope_size, magnification)
        store_data(username, specimen, microscope_size, actual_size)
        messagebox.showinfo("Result", f"Actual Size: {actual_size:.2f} μm saved successfully.")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# GUI setup
root = tk.Tk()
root.title("Specimen Size Calculator")

tk.Label(root, text="Username:").grid(row=0)
tk.Label(root, text="Specimen:").grid(row=1)
tk.Label(root, text="Microscope Size (μm):").grid(row=2)
tk.Label(root, text="Magnification:").grid(row=3)

entry_username = tk.Entry(root)
entry_specimen = tk.Entry(root)
entry_microscope_size = tk.Entry(root)
entry_magnification = tk.Entry(root)

entry_username.grid(row=0, column=1)
entry_specimen.grid(row=1, column=1)
entry_microscope_size.grid(row=2, column=1)
entry_magnification.grid(row=3, column=1)

tk.Button(root, text="Calculate & Save", command=submit).grid(row=4, columnspan=2, pady=10)

root.mainloop()
