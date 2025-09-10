
import os
import sqlite3
import hashlib
import csv
from datetime import datetime, date
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

APP_TITLE = "GSEHS — School Manager"
SCHOOL_NAME = "Good Shepherd English High School"
DB_FILE = "school.db"
ASSETS_DIR = os.path.join("assets")
LOGO_FILE = os.path.join(ASSETS_DIR, "logo.png")
PHOTOS_DIR = os.path.join(ASSETS_DIR, "photos")

def sha(text:str)->str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def ensure_db():
    if not os.path.exists("starter_db.sqlite3"):
        # create empty DB if no starter provided
        con = sqlite3.connect(DB_FILE); con.close()
        return
    if not os.path.exists(DB_FILE):
        shutil.copy("starter_db.sqlite3", DB_FILE)

# For brevity in this packaged version, on first run copy starter_db
import shutil
if not os.path.exists(DB_FILE) and os.path.exists("starter_db.sqlite3"):
    shutil.copy("starter_db.sqlite3", DB_FILE)

def load_logo(size=(48,48)):
    try:
        img = Image.open(LOGO_FILE).convert("RGBA")
        img.thumbnail(size, Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception:
        return None

# Minimal GUI launcher that notifies if DB present and opens a simple window.
def main():
    root = tk.Tk()
    root.title(APP_TITLE)
    root.geometry("800x600")
    top = ttk.Frame(root, padding=8); top.pack(fill="x")
    logo = load_logo((48,48))
    if logo:
        ttk.Label(top, image=logo).pack(side="left")
    ttk.Label(top, text=SCHOOL_NAME, font=("Segoe UI", 14, "bold")).pack(side="left", padx=8)
    ttk.Label(top, text="Starter GUI packaged. Replace with full app.py for more features.", foreground="gray").pack(pady=20)
    ttk.Button(root, text="Open Data Folder", command=lambda: os.startfile(os.getcwd())).pack(pady=6)
    root.mainloop()

if __name__ == "__main__":
    main()
