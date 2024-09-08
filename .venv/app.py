# import PySerial and time
import serial
import time

# Initialize port, rate, and timeout duration
port = "COM3"
rate = 9600
timeout = 0.5

# Connects to Arduino via Serial
ser = serial.Serial(port, rate, timeout)

# Gives time for connection to establish
time.sleep(2)


while True:
    try:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()  # Read, decode, and strip newlines
            print("Soil Moisture Level: ", line)  # Print the data

    except KeyboardInterrupt:
        print("Closing connection...")
        ser.close()
        break