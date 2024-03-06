import requests
from datetime import datetime
import smtplib

MY_LAT = 29.863185
MY_LONG = 77.895035

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.

def close(lat, long):
    if abs(MY_LAT - lat) <= 5 and abs(MY_LONG - long) <= 5:
        return True
    return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
# print(iss_latitude)
# print(iss_longitude)
time_now = datetime.now()
curr_hour = time_now.hour

if curr_hour >= sunset or curr_hour <= sunrise:
    if close(iss_latitude, iss_longitude):
        print("done")
        username = "chdvanshsingh@gmail.com"
        password = "ylah umpf iwjk ibxs"

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=username, password=password)
            connection.sendmail(username, "workman3140@gmail.com", msg="Subject:ISS-Overhead\n\nLook Above in the sky "
                                                                       "to see me!!")
