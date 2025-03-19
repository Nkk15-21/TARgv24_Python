import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import subprocess
import tkinter as tk
from os import path
from tkinter import ttk


# Avab lisamise faili
def add_data():
    subprocess.run(["python", "01.py"])

# Otsingufunktsioon
def on_search():
    search_query = search_entry.get()
    load_data_from_db(tree, search_query)

# Funktsioon, mis laadib andmed SQLite andmebaasist ja sisestab need Treeview tabelisse
def load_data_from_db(tree, search_query=""):
    # Puhasta Treeview tabel enne uute andmete lisamist
    for item in tree.get_children():
        tree.delete(item)

    # Loo ühendus SQLite andmebaasiga
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    # Tee päring andmebaasist andmete toomiseks, koos ID-ga, kuid ID ei kuvata
    if search_query:
        cursor.execute("""
            SELECT id, title, director, release_year, genre, duration, rating, language, country, description
            FROM movies
            WHERE title LIKE ?
        """, ('%' + search_query + '%',))
    else:
        cursor.execute("""
            SELECT id, title, director, release_year, genre, duration, rating, language, country, description
            FROM movies
        """)

    rows = cursor.fetchall()

    # Lisa andmed tabelisse (Treeview), kuid ID-d ei kuvata
    for row in rows:
        tree.insert("", "end", values=row[1:], iid=row[0])  # iid määratakse ID-ks

    # Sulge ühendus andmebaasiga
    conn.close()

# Funktsioon, mis näitab valitud rea ID-d ja avab muutmise vormi
def on_update():
    selected_item = tree.selection()  # Võta valitud rida
    if selected_item:
        record_id = selected_item[0]  # iid (ID)
        open_update_window(record_id)
    else:
        messagebox.showwarning("Valik puudub", "Palun vali kõigepealt rida!")

# Funktsioon, mis avab uue akna andmete muutmiseks
def open_update_window(record_id):
    # Loo uus aken
    update_window = tk.Toplevel(root)
    update_window.title("Muuda filmi andmeid")

    # Loo andmebaasi ühendus ja toomine olemasolevad andmed
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT title, director, release_year, genre, duration, rating, language, country, description
        FROM movies
        WHERE id=?
    """, (record_id,))
    record = cursor.fetchone()
    conn.close()

    # Veergude nimed ja vastavad sisestusväljad
    labels = ["Pealkiri", "Režissöör", "Aasta", "Žanr", "Kestus", "Reiting", "Keel", "Riik", "Kirjeldus"]
    entries = {}

    for i, label in enumerate(labels):
        tk.Label(update_window, text=label).grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
        entry = tk.Entry(update_window, width=50)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entry.insert(0, record[i])
        entries[label] = entry

    # Salvestamise nupp
    save_button = tk.Button(update_window, text="Salvesta", command=lambda: update_record(record_id, entries, update_window))
    save_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

# Funktsioon, mis uuendab andmed andmebaasis
def update_record(record_id, entries, window):
    # Koguge andmed sisestusväljadest
    title = entries["Pealkiri"].get()
    director = entries["Režissöör"].get()
    release_year = entries["Aasta"].get()
    genre = entries["Žanr"].get()
    duration = entries["Kestus"].get()
    rating = entries["Reiting"].get()
    language = entries["Keel"].get()
    country = entries["Riik"].get()
    description = entries["Kirjeldus"].get()

    # Andmete uuendamine andmebaasis
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE movies
        SET title=?, director=?, release_year=?, genre=?, duration=?, rating=?, language=?, country=?, description=?
        WHERE id=?
    """, (title, director, release_year, genre, duration, rating, language, country, description, record_id))
    conn.commit()
    conn.close()

    # Värskenda Treeview tabelit
    load_data_from_db(tree)

    # Sulge muutmise aken
    window.destroy()

    messagebox.showinfo("Salvestamine", "Andmed on edukalt uuendatud!")

# Ühendatud funktsioon kustutamiseks
def on_delete():
    selected_item = tree.selection()  # Võta valitud rida
    if selected_item:
        record_id = selected_item[0]  # iid (ID)
        confirm = messagebox.askyesno("Kinnita kustutamine", "Kas oled kindel, et soovid selle rea kustutada?")
        if confirm:
            try:
                # Loo andmebaasi ühendus
                conn = sqlite3.connect('movies.db')
                cursor = conn.cursor()
               
                # Kustuta kirje
                cursor.execute("DELETE FROM movies WHERE id=?", (record_id,))
                conn.commit()
                conn.close()
               
                # Värskenda Treeview tabelit
                load_data_from_db(tree)
               
                messagebox.showinfo("Edukalt kustutatud", "Rida on edukalt kustutatud!")
            except sqlite3.Error as e:
                messagebox.showerror("Viga", f"Andmebaasi viga: {e}")
    else:
        messagebox.showwarning("Valik puudub", "Palun vali kõigepealt rida!")

# Loo põhivorm
root = tk.Tk()
root.title("Filmid")
root.geometry("1000x600")  # Soovitatav lisada akna suurus

# Loo ülemine raam, mis sisaldab otsingut ja nuppe
top_frame = tk.Frame(root)
top_frame.pack(pady=10, fill=tk.X, padx=10)

# Loo otsinguväli ja nupp vasakule
search_frame = tk.Frame(top_frame)
search_frame.pack(side=tk.LEFT, anchor="w")

search_label = tk.Label(search_frame, text="Otsi filmi pealkirja järgi:")
search_label.pack(side=tk.LEFT)

search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT, padx=10)

search_button = tk.Button(search_frame, text="Otsi", command=on_search)
search_button.pack(side=tk.LEFT)

# Loo nupud paremale
buttons_frame = tk.Frame(top_frame)
buttons_frame.pack(side=tk.RIGHT, anchor="e")

# Lisa andmete lisamise nupp
open_button = tk.Button(buttons_frame, text="Lisa andmeid", command=add_data)
open_button.pack(side=tk.LEFT, padx=5)

# Uuenda nupp
update_button = tk.Button(buttons_frame, text="Uuenda", command=on_update)
update_button.pack(side=tk.LEFT, padx=5)

# Kustuta nupp
delete_button = tk.Button(buttons_frame, text="Kustuta", command=on_delete)
delete_button.pack(side=tk.LEFT, padx=5)

# Loo raam kerimisribaga
frame = tk.Frame(root)
frame.pack(pady=20, fill=tk.BOTH, expand=True, padx=10)
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Loo tabel (Treeview) andmete kuvamiseks, ilma ID veeruta
tree = ttk.Treeview(frame, yscrollcommand=scrollbar.set, columns=(
    "title", "director", "year", "genre", "duration", "rating", "language", "country", "description"), show="headings")
tree.pack(fill=tk.BOTH, expand=True)

# Seosta kerimisriba tabeliga
scrollbar.config(command=tree.yview)

# Määra veergude pealkirjad ja laius
tree.heading("title", text="Pealkiri")
tree.heading("director", text="Režissöör")
tree.heading("year", text="Aasta")
tree.heading("genre", text="Žanr")
tree.heading("duration", text="Kestus")
tree.heading("rating", text="Reiting")
tree.heading("language", text="Keel")
tree.heading("country", text="Riik")
tree.heading("description", text="Kirjeldus")

tree.column("title", width=150)
tree.column("director", width=100)
tree.column("year", width=60)
tree.column("genre", width=100)
tree.column("duration", width=60)
tree.column("rating", width=60)
tree.column("language", width=80)
tree.column("country", width=80)
tree.column("description", width=200)

# Laadi andmed tabelisse
load_data_from_db(tree)

# Käivita põhiloogika
root.mainloop()


# Lisa Kustuta nupp, mis kustutab selekteeritud rea
delete_button = tk.Button(root, text="Kustuta", command=on_delete)
delete_button.pack(pady=10)

# Ühendatud funktsioon kustutamiseks
def on_delete():
    selected_item = tree.selection()  # Võta valitud rida
    if selected_item:
        record_id = selected_item[0]  # iid (ID)
        confirm = messagebox.askyesno("Kinnita kustutamine", "Kas oled kindel, et soovid selle rea kustutada?")
        if confirm:
            try:
                # Loo andmebaasi ühendus
                conn = sqlite3.connect('movies.db')
                cursor = conn.cursor()
               
                # Kustuta kirje
                cursor.execute("DELETE FROM movies WHERE id=?", (record_id,))
                conn.commit()
                conn.close()
               
                # Värskenda Treeview tabelit
                load_data_from_db(tree)
               
                messagebox.showinfo("Edukalt kustutatud", "Rida on edukalt kustutatud!")
            except sqlite3.Error as e:
                messagebox.showerror("Viga", f"Andmebaasi viga: {e}")
    else:
        messagebox.showwarning("Valik puudub", "Palun vali kõigepealt rida!")