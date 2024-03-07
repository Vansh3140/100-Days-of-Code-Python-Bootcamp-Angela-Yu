import requests
from twilio.rest import Client

account_sid = "AC982903546ad8c22a6fe2103a6e7acbe5"
auth_token = "20da1d5fb4e77af539bebf30d062dfe9"

MY_LAT = 31.690783
MY_LONG = 76.517715
api_key = "5937458e6882c8bef6990439168dfd5d"

data = requests.get(
    url=f"https://api.openweathermap.org/data/2.5/forecast?lat={MY_LAT}&lon={MY_LONG}&cnt=4&appid={api_key}")

weather_data = data.json()
rain = False
index = 0

for x in weather_data["list"]:
    id_today = x["weather"][0]["id"]
    index += 1

    if id_today < 700:
        rain = True
        break

if rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"Rain Alert!!\n Keep an umbrella with you as rain is predicted at "
             f"{weather_data["list"][index]["dt_txt"]}",
        from_="+14406642904",
        to="+918219391456"
    )

    print(message.status)
