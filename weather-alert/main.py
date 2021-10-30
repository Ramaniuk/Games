import os
import smtplib
from dotenv import load_dotenv
import requests

load_dotenv()

end_point = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = "e18611562ff8fb6d183813c48ab80615"
parametrs = {
    "lat": 27.167,
    "lon": -82.3332,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(end_point, params=parametrs)
response.raise_for_status()
code_status = response.status_code
data = response.json()

for i in range (0,12):
    weather = data["hourly"][i]["weather"][0]["id"]
    if weather < 700:
        my_email = 'testForCoursesOlga@gmail.com'
        password = os.environ.get('PASSWORD_GMAIL')
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:Weather\n\n Bring an umbrella")
        connection.close()