import serial
import sys
import os

from datetime import datetime
import requests
import json
import boto3
import time
from decimal import Decimal

# https://stackoverflow.com/questions/1960516/python-json-serialize-a-decimal-object
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return str(o)
        return super().default(o)

COM_PORT = 'COM3'
BAUD_RATE = 115200
#API_ENDPOINT = 'https://woqi43dh1h.execute-api.eu-north-1.amazonaws.com/test'
RUN_TIME = 20

lambda_client = boto3.client('lambda', region_name='eu-north-1')

try:
    ser = serial.Serial(COM_PORT, BAUD_RATE)

    if ser.is_open:
        print("Serial port opened")
    else:
        print("Could not open serial port.")
        sys.exit()

    start_time = time.time()

    with open('temperature_data.txt', 'w', encoding='utf-8') as log_file:
        while True:
            if time.time() - start_time >= RUN_TIME:
                print("Program finished running for 20 seconds")
                break
            
            try:
                temperature_data = ser.readline().decode('utf-8').rstrip()
            
                variables = temperature_data.split(',')

                current_time = datetime.now().isoformat()

                sensor_id = variables[0]
                date_time = current_time
                max_threshold = int(variables[1].strip())
                min_threshold = int(variables[2].strip())
                location_id = variables[3].strip()
                curr_temp = float(variables[4].strip())
                is_exceeded = variables[5].strip().lower() == "true"

                data = {
                    'sensor_id': sensor_id,
                    'date_time': date_time,
                    'max_threshold': Decimal(max_threshold),
                    'min_threshold': Decimal(min_threshold),
                    'location_id': location_id,
                    'curr_temp': Decimal(curr_temp),
                    'is_exceeded': is_exceeded
                }

                #print("JSON Object:", json.dumps(data))

                json_data = json.dumps(data, cls=DecimalEncoder)

                try:
                    #response = requests.post(API_ENDPOINT, json=json_data, timeout=5)
                    response = lambda_client.invoke(
                    FunctionName='HttpRequestHandlerLambda',
                    InvocationType='RequestResponse',
                    Payload=json_data
                    )

                    print("Data sent to the database")
                except requests.exceptions.RequestException as e:
                    print("Error sending data to the database:", e)

            except KeyboardInterrupt as e:
                print("Keyboard interrupt. Exiting program")
                ser.close()
                sys.exit()

except serial.SerialException as e:
    print("Serial port error. Exiting program")
    sys.exit()
