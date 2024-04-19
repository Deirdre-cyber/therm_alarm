from microbit import *
import utime

SENSOR_ID = "SENSE001"
LOCATION_ID = "S300"
HIGH_THRESHOLD = 23
LOW_THRESHOLD = 19


with open("temperature_log.txt", "w") as log_file:

    while True:
        curr_temp = temperature()
        is_exceeded = False


        if curr_temp > HIGH_THRESHOLD or curr_temp < LOW_THRESHOLD:
            is_exceeded = True
            display.show(Image.SAD)

        else:
            display.show(Image.HAPPY)

        log_data = "{}, {}, {}, {}, {}, {}".format(
            SENSOR_ID, HIGH_THRESHOLD, LOW_THRESHOLD, LOCATION_ID, curr_temp, is_exceeded)

        sleep(2000)

        print(log_data)
        log_file.write(log_data)

        sleep(5000)
