import smtplib
from dotenv import load_dotenv
import requests
import datetime
import os

load_dotenv()

date = datetime.datetime.today()
today = str(date).split(" ")[0]
yesterday = str(date - datetime.timedelta(days=1)).split(" ")[0]
day_before_yesterday = str(date - datetime.timedelta(days=2)).split(" ")[0]

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

api_key_news = os.environ.get("API_NEWS")
api_key_stock = os.environ.get("API_STOCKS")
params_stock = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK,
        "apikey": api_key_stock,
    }

response = requests.get(STOCK_ENDPOINT, params=params_stock)
data = response.json()

yesterday_price = data["Time Series (Daily)"][yesterday]["4. close"]
day_before_yesterday_price = data["Time Series (Daily)"][day_before_yesterday]["4. close"]
abs_difference = abs(float(yesterday_price) - float(day_before_yesterday_price))
diff_percent = abs_difference / float(day_before_yesterday_price) * 100

if diff_percent > 3:
    params_news = {
        "apiKey": api_key_news,
        "qInTitle": COMPANY_NAME,
        "sortBy": "relevancy",
    }

    response = requests.get(NEWS_ENDPOINT, params=params_news)
    news = response.json()["articles"]
    message = news[:3]
    formated_news = [f"Headline: {article['title']}. \nBrief: {article['description']}"
            for article in message]

    for one_news in formated_news:
        my_email = 'testForCoursesOlga@gmail.com'
        password = os.environ.get('PASSWORD_GMAIL')
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=my_email, password=password)
        one_news = one_news.encode("ascii", errors="ignore")
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:STOCK price increase/decreases by 3% or more. Get News!!!\n\n {one_news}")
        connection.close()
