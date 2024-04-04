import serial
import sys

COM_PORT = 'COM3'
BAUD_RATE = 115200



try:
    ser = serial.Serial(COM_PORT, BAUD_RATE)

    if ser.is_open:
        print("Serial port opened")
    else:
        print("Could not open serial port.")
        sys.exit()

    while True:
        try:
            temperature_data = ser.readline().decode('utf-8').rstrip()
            print("Data received:", temperature_data)
        except KeyboardInterrupt as e:
            print("Keyboard interrupt. Exiting program")
            ser.close()
            sys.exit()

except serial.SerialException as e:
    print("Serial port error. Exiting program")
    sys.exit()
