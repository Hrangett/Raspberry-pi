import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin=21

try:
        while True:
                h,t = Adafruit_DHT.read_retry(sensor,pin)
                if h is not None and t is not None:
                        print("Temp = {0:0.1f}*C Humi = {1:0.1f}%".format(t,h))
                else:
                        print("Failed to get reading")
except KeyboardInterrupt:
       GPIO.clearup()

