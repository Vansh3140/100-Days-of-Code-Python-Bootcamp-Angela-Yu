import requests
from twilio.rest import Client

account_sid = "83299210010101-1-1--3"
auth_token = "82932023489920202"

stock_raw_data = requests.get(
    "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=RELIANCE.BSE&outputsize=compact&apikey"
    "=XB2FEUBEYLVX4F0Y")
stock_data = stock_raw_data.json()
# print(stock_data)
flag = 2

for x in stock_data["Time Series (Daily)"]:
    if flag == 2:
        first_key = x
    elif flag == 1:
        second_key = x
    else:
        break
    flag -= 1

change = round(100 * ((float(stock_data["Time Series (Daily)"][first_key]["4. close"]) -
                       float(stock_data["Time Series (Daily)"][second_key]["4. close"])) /
                      float(stock_data["Time Series (Daily)"][first_key]["4. close"])), 2)

if change > 0:
    sign = "🔺"
else:
    sign = "🔻"

if change >= 5 or change <= -5:
    news_raw_data = requests.get(
        f"https://newsapi.org/v2/everything?q=reliance&searchIn=description&from={second_key}&to={first_key}&language=en&sortBy=relevance&pageSize=3&apiKey=f7bae75b748b4918a3719bd06728479d")
    news_data = news_raw_data.json()
    for x in news_data["articles"]:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_="+14406642904",
            body=f"RELIANCE: {sign}{change}%\n"
                 f"Headline:{x['title']}\n"
                 f"Brief:{x['content']}\n"
                 f"URL:{x['url']}",
            to="+918219391456"
        )
        print(message.sid)
