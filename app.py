import sqlite3
from datetime import datetime
import serial
import time

# SQLite setup
with sqlite3.connect('soil_moisture.db') as conn:
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS moisture_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT NOT NULL,
        moisture_level INTEGER NOT NULL
    )
    ''')
    conn.commit()

# Moisture data update function
    def insert_moisture_data(moisture_value):
# Get current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Insert data into table
        cursor.execute("INSERT INTO moisture_data (timestamp, moisture_level) VALUES (?, ?)",
                       (timestamp, moisture_value))

# Commit every insert
        conn.commit()

# Fetch last inserted row and print
        cursor.execute("SELECT * FROM moisture_data ORDER BY id DESC LIMIT 1")
        last_row = cursor.fetchone()
        print(last_row)

# Initialize port, rate, and timeout duration
    port = 'COM3'
    rate = 9600
    timeoutTime = 1
    with serial.Serial(port, rate, timeout=timeoutTime) as ser:

# Give time for connection to establish
        time.sleep(2)

        while True:
            try:
                if ser.in_waiting > 0:
# Read line from the serial port
                    line = ser.readline().decode('utf-8').strip()
                    insert_moisture_data(line)
            except KeyboardInterrupt:
# Close connection on interrupt
                print("Closing connection...")
                break
