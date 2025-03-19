import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# validate_data funktsioon, mis kontrollib kas sisestatud andmed on korrektsed
def validate_data():
    title = entries["Pealkiri"].get()
    release_year = entries["Aasta"].get()
    rating = entries["Reiting"].get()

    if not title:
        messagebox.showerror("Viga", "Pealkiri on kohustuslik!")
        return False
    if not release_year.isdigit():
        messagebox.showerror("Viga", "Aasta peab olema arv!")
        return False
    if rating and (not rating.replace('.', '', 1).isdigit() or not (0 <= float(rating) <= 10)):
        messagebox.showerror("Viga", "Reiting peab olema vahemikus 0 kuni 10!")
        return False

    return True

# valideerib andmed ja lisab need andmebaasi
def insert_data():
    if validate_data():
        connection = sqlite3.connect("movies.db")
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO movies (title, director, release_year, genre, duration, rating, language, country, description)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            entries["Pealkiri"].get(),
            entries["Režissöör"].get(),
            entries["Aasta"].get(),
            entries["Žanr"].get(),
            entries["Kestus"].get(),
            entries["Reiting"].get(),
            entries["Keel"].get(),
            entries["Riik"].get(),
            entries["Kirjeldus"].get()
        ))

        connection.commit()
        connection.close()

        messagebox.showinfo("Edu", "Andmed sisestati edukalt!")
        clear_entries()  # Puhastame sisestusväljad pärast sisestamist

        # Now we update the Treeview in the second window to reflect the new data
        if second_window:
            load_data_from_db(second_window.tree)

# Puhastab kõik sisestusväljad
def clear_entries():
    for entry in entries.values():
        entry.delete(0, tk.END)

# Create a new instance of the second window
second_window = None

def open_second_window():
    global second_window
    second_window = SecondWindow()

# The second window (where data is displayed)
class SecondWindow:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Filmid")
        self.tree = ttk.Treeview(self.window, columns=("title", "director", "year", "genre", "duration", "rating", "language", "country", "description"), show="headings")
        
        # Set up the columns
        self.tree.heading("title", text="Pealkiri")
        self.tree.heading("director", text="Režissöör")
        self.tree.heading("year", text="Aasta")
        self.tree.heading("genre", text="Žanr")
        self.tree.heading("duration", text="Kestus")
        self.tree.heading("rating", text="Reiting")
        self.tree.heading("language", text="Keel")
        self.tree.heading("country", text="Riik")
        self.tree.heading("description", text="Kirjeldus")

        self.tree.pack(fill=tk.BOTH, expand=True)
        self.load_data_from_db()

    def load_data_from_db(self):
        # Clear existing data in Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Connect to the database and fetch data
        conn = sqlite3.connect('movies.db')
        cursor = conn.cursor()
        cursor.execute("SELECT title, director, release_year, genre, duration, rating, language, country, description FROM movies")
        rows = cursor.fetchall()

        # Insert data into the Treeview
        for row in rows:
            self.tree.insert("", "end", values=row)

        conn.close()

# Loo Tkinteri aken
root = tk.Tk()
root.title("Filmi andmete sisestamine")

# Loo sildid ja sisestusväljad
labels = ["Pealkiri", "Režissöör", "Aasta", "Žanr", "Kestus", "Reiting", "Keel", "Riik", "Kirjeldus"]
entries = {}

for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5)
    entry = tk.Entry(root, width=40)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries[label] = entry

# Loo nupp andmete sisestamiseks
submit_button = tk.Button(root, text="Sisesta andmed", command=insert_data)
submit_button.grid(row=len(labels), column=0, columnspan=2, pady=20)

# Nuputa aken, mis avab teise akna
open_second_button = tk.Button(root, text="Ava teise akna", command=open_second_window)
open_second_button.grid(row=len(labels)+1, column=0, columnspan=2, pady=20)

# Näita Tkinteri akent
root.mainloop()
