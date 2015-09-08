import httplib, urllib
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(22,GPIO.IN)
GPIO.setup(25,GPIO.IN)

while True:
        while GPIO.input(22):
                conn = httplib.HTTPSConnection("api.pushover.net:443")
                conn.request("POST", "/1/messages.json",
                        urllib.urlencode({
                                "token": "auRmuk8k3RMwMvBsUWHd32HiFKA1q1",
                                "user": "uhXNJNNZ2vXGoLvuHRipD6RbPVpGQR",
                                "message": "Door Bell",
                                "sound": "persistent",
                                "priority": "1",
                        }), { "Content-type": "application/x-www-form-urlencoded" })
                conn.getresponse()
                time.sleep(5)
