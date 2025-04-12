# b_with_database.py

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

def main():
    username = input("Enter your name: ")
    specimen = input("Enter specimen name: ")
    microscope_size = float(input("Enter microscope size (μm): "))
    magnification = float(input("Enter magnification level: "))
    actual_size = calculate_real_size(microscope_size, magnification)
    store_data(username, specimen, microscope_size, actual_size)
    print(f"Stored: {specimen} | Actual Size: {actual_size:.2f} μm")

if __name__ == "__main__":
    main()
