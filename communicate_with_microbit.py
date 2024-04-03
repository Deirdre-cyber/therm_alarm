import serial
import sys

BAUD_RATE = 115200

ser = serial.Serial('COM3', BAUD_RATE)

if ser.is_open:
    print("Serial port opened")
else:
    print("Could not open serial port.")
    sys.exit()

while True:
    temperature_data = ser.readline().decode('utf-8').rstrip()
    print("Data received:", temperature_data)
