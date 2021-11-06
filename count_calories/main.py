import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app_id = os.environ.get("APP_ID")
api_key = os.environ.get("API_KEY")
autorization=os.environ.get("AUTORIZATION")

user_data = input("Tell me which exercises you did: ")

nutritionix_endpoint = "https://trackapi.nutritionix.com"
exercise_endpoint = f"{nutritionix_endpoint}/v2/natural/exercise"

headers = {
    "x-app-id" : app_id,
    "x-app-key" : api_key,
}

body = {
    "query": user_data,
     "gender": "female",
     "weight_kg": 69,
     "height_cm": 170,
     "age": 40
}


response = requests.post(url=exercise_endpoint,headers=headers,json=body)
result = response.json()
#print(result)

workout_tracking_endpoint = "https://api.sheety.co/add050214c49664399aace272de62318/workoutTracking/workouts"
headers = {"Authorization": f"Basic {autorization}"}
workout_time = datetime.now()
date = workout_time.strftime("%d/%m/%Y")
time = workout_time.strftime("%X")

for exercise in result["exercises"]:
    body_sheety = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
        }
    sheet_response = requests.post(url=workout_tracking_endpoint,headers=headers,json=body_sheety)
#print(sheet_response.text)
print(sheet_response.status_code)


# https://docs.google.com/spreadsheets/d/185gWoMZyyDK6R6Y9YRF1j06N-b_KbSCxEP6pqWWtAi4/edit#gid=0