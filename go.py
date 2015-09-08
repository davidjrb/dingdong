import httplib, urllib
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(22,GPIO.IN)
GPIO.setup(25,GPIO.IN)

while True:
        x=0
        while not GPIO.input(25):
                conn = httplib.HTTPSConnection("api.pushover.net:443")
                conn.request("POST", "/1/messages.json",
                        urllib.urlencode({
                                "token": "auRmuk8k3RMwMvBsUWHd32HiFKA1q1",
                                "user": "uhXNJNNZ2vXGoLvuHRipD6RbPVpGQR",
                                "message": "Gate Opened",
                                "sound": "bike",
                        }), { "Content-type": "application/x-www-form-urlencoded" })
                conn.getresponse()
                while not GPIO.input(25):
                        time.sleep(5)
                        x=x+1
#..24*5sec=2min
                        while x>=24:
                                conn = httplib.HTTPSConnection("api.pushover.net:443")
                                conn.request("POST", "/1/messages.json",
                                        urllib.urlencode({
                                                "token": "auRmuk8k3RMwMvBsUWHd32HiFKA1q1",
                                                "user": "uhXNJNNZ2vXGoLvuHRipD6RbPVpGQR",
                                                "message": "Gate Ajar Alarm!",
                                                "sound": "falling",
                                                "priority": "1"
                                        }), { "Content-type": "application/x-www-form-urlencoded" })
                                conn.getresponse()
                                while not GPIO.input(25):
                                        time.sleep(1)
                                        if GPIO.input(25):
                                                conn = httplib.HTTPSConnection("api.pushover.net:443")
                                                conn.request("POST", "/1/messages.json",
                                                        urllib.urlencode({
                                                                "token": "auRmuk8k3RMwMvBsUWHd32HiFKA1q1",
                                                                "user": "uhXNJNNZ2vXGoLvuHRipD6RbPVpGQR",
                                                                "message": "Ajar Alarm Healthy",
                                                                "sound": "classical",
                                                        }), { "Content-type": "application/x-www-form-urlencoded" })
                                                conn.getresponse()
                                                time.sleep(5)
                                                x=0
                                                break
