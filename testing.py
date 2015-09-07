import httplib, urllib
import time

#David = uhXNJNNZ2vXGoLvuHRipD6RbPVpGQR
#Andi = utZvgrnLdruUmL5LfoxDVdmCUKfKiz

while True:

    entereturn = raw_input("Choose: ")

    if entereturn == "andi":
        conn = httplib.HTTPSConnection("api.pushover.net:443")
        conn.request("POST", "/1/messages.json",
          urllib.urlencode({
            "token": "auRmuk8k3RMwMvBsUWHd32HiFKA1q1",
            "user": "utZvgrnLdruUmL5LfoxDVdmCUKfKiz",
            "message": "That food looks delicious! :)",
            "priority": "1",
            "sound": "persistent",
          }), { "Content-type": "application/x-www-form-urlencoded" })
        conn.getresponse()
        time.sleep(5)

    elif entereturn == "david":
        conn = httplib.HTTPSConnection("api.pushover.net:443")
        conn.request("POST", "/1/messages.json",
            urllib.urlencode({
                "token": "auRmuk8k3RMwMvBsUWHd32HiFKA1q1",
                "user": "uhXNJNNZ2vXGoLvuHRipD6RbPVpGQR",
                "message": "Doorbell!",
                "priority": "1",
                "sound": "persistent",
            }), { "Content-type": "application/x-www-form-urlencoded" })
        conn.getresponse()
        time.sleep(5)
