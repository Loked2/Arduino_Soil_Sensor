# import PySerial and time
import serial
import time
import pandas as pd
current_time = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
moist = []
# Initialize port, rate, and timeout duration
port = "COM3"
rate = 9600
timeoutTime = 1

# Connects to Arduino via Serial
ser = serial.Serial(port, rate, timeout = timeoutTime)

# Gives time for connection to establish
time.sleep(2)


while True:
    try:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()  # Read, decode, and strip newlines
            moist.append(line)
            df = pd.DataFrame({'Time': formatted_time, 'Moisture': moist})
            print("Soil Moisture Level: ", line)  # Print the data

    except KeyboardInterrupt:
        print("Closing connection...")
        ser.close()
        df.to_excel('sensor_data.xlsx', index=False, engine='openpyxl')
        break
