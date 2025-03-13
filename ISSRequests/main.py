import requests
from datetime import datetime
# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()

# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)

# print(iss_position)

#dictionary
parameters = {
    "lat": 51.507351,
    "lng": -0.127758,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status() #raises exception if API call fails
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(f"Sunrise: {sunrise}, Sunset: {sunset}")

time_now = datetime.now()

print(time_now)