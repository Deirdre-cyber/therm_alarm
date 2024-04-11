import serial
import sys
from datetime import datetime
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

COM_PORT = 'COM3'
BAUD_RATE = 115200
LAMBDA_ENDPOINT = os.getenv('LAMBDA_ENDPOINT')

try:
    ser = serial.Serial(COM_PORT, BAUD_RATE)

    if ser.is_open:
        print("Serial port opened")
    else:
        print("Could not open serial port.")
        sys.exit()

    with open('temperature_data.txt', 'w', encoding='utf-8') as log_file:
        while True:
            try:
                temperature_data = ser.readline().decode('utf-8').rstrip()
            
                variables = temperature_data.split(',')

                current_time = datetime.now().isoformat()

                # dictionary for the date for ease in uploading to the database
                # trhresholds will need to be set from app...
                data = {
                    'sensor_id' : variables[0],
                    'date_time' : current_time,
                    'max_threshold' : variables[1],
                    'min_threshold' : variables[2],
                    'location_id' : variables[3],
                    'curr_temp' : variables[4],
                    'is_exceeded' : variables[5]
                }

                json_data = json.dumps(data)


                try:
                    response = requests.post(LAMBDA_ENDPOINT, json=json_data, timeout=5)

                    if response.status_code == 200:
                        print("Data sent to the database")
                    else:
                        print("Error sending data to the database")
                except requests.exceptions.RequestException as e:
                    print("Error sending data to the database:", e)

                # log file is for debugging
                log_file.write(data['sensor_id'] + ',' + str(data['date_time']) + ',' + data['max_threshold'] + ',' + data['min_threshold'] + ',' + data['location_id'] + ',' + data['curr_temp'] + ',' + data['is_exceeded'] + '\n')

            except KeyboardInterrupt as e:
                print("Keyboard interrupt. Exiting program")
                ser.close()
                sys.exit()

except serial.SerialException as e:
    print("Serial port error. Exiting program")
    sys.exit()
