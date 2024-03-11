import requests
import datetime as dt
from requests.auth import HTTPBasicAuth

APP_ID = "a"
API_KEY = "7"

api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheets_endpoint = "https://api.sheety.co/myWorkouts/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

params = {
    "query": input("Enter the exercises done:")
}

response = requests.post(url=api_endpoint, headers=headers, json=params)

date = dt.datetime.now().date()

basic = HTTPBasicAuth("chm", "9")

for x in response.json()["exercises"]:
    workout_data = {
        "workout": {
            "date": date.strftime("%Y-%m-%d"),
            "time": dt.datetime.now().strftime("%H:%M:%S"),
            "exercise": x["user_input"][0].upper() + x["user_input"][1:],
            "duration": x["duration_min"],
            "calories": x["nf_calories"]
        }
    }

    sheets_response = requests.post(url=sheets_endpoint, json=workout_data, auth=basic)
    print(sheets_response.text)
