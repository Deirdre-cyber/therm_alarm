import serial
import sys
from datetime import datetime

COM_PORT = 'COM3'
BAUD_RATE = 115200

try:
    ser = serial.Serial(COM_PORT, BAUD_RATE)

    if ser.is_open:
        print("Serial port opened")
    else:
        print("Could not open serial port.")
        sys.exit()

    # log file is also for debugging
    with open('temperature_data.txt', 'w') as log_file:
        while True:
            try:
                temperature_data = ser.readline().decode('utf-8').rstrip()
                print("Data received:", temperature_data)

                variables = temperature_data.split(',')

                current_time = datetime.now()

                # dictionary for the date for ease in uploading to the database
                data = {
                    'sensor_id' : variables[0],
                    'date_time' : current_time,
                    'max_threshold' : variables[1],
                    'min_threshold' : variables[2],
                    'location_id' : variables[3],
                    'curr_temp' : variables[4],
                    'is_exceeded' : variables[5]
                }

                print("Number of variables:", len(variables)) # debug

                # following print statements all for debugging purposes
                print("sensor_id:", data['sensor_id'])
                print("date_time:", data['date'])
                print("max_threshold:", data['max_threshold'])
                print("min_threshold:", data['min_threshold'])
                print("location_id:", data['location_id'])
                print("curr_temp:", data['curr_temp'])
                print("is_exceeded:", data['is_exceeded'])

                # log file is also for debugging
                log_file.write(temperature_data + '\n')

            except KeyboardInterrupt as e:
                print("Keyboard interrupt. Exiting program")
                ser.close()
                sys.exit()

except serial.SerialException as e:
    print("Serial port error. Exiting program")
    sys.exit()
