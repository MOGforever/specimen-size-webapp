# d_flask_web_app/app.py

from flask import Flask, render_template, request, redirect, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for flashing messages

DB_PATH = os.path.join(os.path.dirname(__file__), 'specimens.db')

def calculate_real_size(microscope_size, magnification):
    return microscope_size / magnification

def store_data(username, specimen, microscope_size, actual_size):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS records
                 (username TEXT, specimen TEXT, microscope_size REAL, actual_size REAL)''')
    c.execute("INSERT INTO records VALUES (?, ?, ?, ?)",
              (username, specimen, microscope_size, actual_size))
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            username = request.form['username']
            specimen = request.form['specimen']
            microscope_size = float(request.form['microscope_size'])
            magnification = float(request.form['magnification'])
            actual_size = calculate_real_size(microscope_size, magnification)
            store_data(username, specimen, microscope_size, actual_size)
            flash(f"Success! Actual size: {actual_size:.2f} μm")
        except ValueError:
            flash("Please enter valid numbers.")
        return redirect('/')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
