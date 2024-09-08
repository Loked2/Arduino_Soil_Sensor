import tkinter as tk
from tkinter import ttk
import sqlite3

def fetch_moisture_data():
    conn = sqlite3.connect('soil_moisture.db')
    cursor = conn.cursor()
    cursor.execute("SELECT moisture_level FROM moisture_data ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def update_display():
    moisture_value = fetch_moisture_data()

    if moisture_value is not None:
        moisture_label.config(text=f"Moisture Level: {moisture_value}")

        # Change background color based on moisture value
        if moisture_value < 500:
            root.config(bg="green")
        else:
            root.config(bg="red")
    else:
        moisture_label.config(text="Moisture Level: No Data")
        root.config(bg="white")  # Default background color if no data

    root.after(5000, update_display)  # Schedule to call `update_display` again after 5000 milliseconds (5 seconds)

# Initialize the main window
root = tk.Tk()
root.title("Moisture Meter")

# Create and pack the moisture level label
moisture_label = ttk.Label(root, text="Moisture Level: Not Available", font=("Arial", 16))
moisture_label.pack(padx=20, pady=20)

# Start updating the display
update_display()

# Start the Tkinter event loop
root.mainloop()