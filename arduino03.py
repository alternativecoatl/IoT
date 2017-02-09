import serial
import time
from ISStreamer.Streamer import Streamer

arduinoSerialData = serial.Serial("/dev/ttyACM0" ,9600)

streamer = Streamer(bucket_name="Motion Sensor", bucket_key="BUCKETKEY", access_key="diDVEooR0jivG0PgipJITmhCkfj58k8R")

try:
        while True:
                myData = arduinoSerialData.readline()
                print myData
                streamer.log("Message: ", myData)
except KeyboardInterrupt:
	streamer.close()
