import httplib, urllib
conn = httplib.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.urlencode({
    "token": "auRmuk8k3RMwMvBsUWHd32HiFKA1q1",
    "user": "uhXNJNNZ2vXGoLvuHRipD6RbPVpGQR",
    "message": "Gate Opened!",
    "sound": "bike",
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()
