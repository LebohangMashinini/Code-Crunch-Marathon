import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_data():
    api_key = API_KEY
    api_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = input("Please enter your city name for a weather update: ")
    complete_url = api_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    
    # json method of response object 
    # convert json format data into
    # python format data
    if response.status_code == 200:
        data = response.json()
        return data

get_data()

def send_sms():
    ACCOUNT_SID = os.getenv("ACCOUNT_SID")
    AUTH_TOKEN = os.getenv("AUTH_TOKEN")
    TO_NUMBER = os.getenv("TO")
    FROM_NUMBER = os.getenv("FROM_NUMBER")

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    data = get_data()
    print("data received:", data)
    if data:
        for weather in data["weather"]:
            weather_description = weather["description"]
            print(f"today's weather: {weather_description}")
            if "rain" in weather_description:
                message = client.messages.create(
                    to = TO_NUMBER,
                    from_ = FROM_NUMBER,
                    body = "It looks like its going to rain today. Don’t forget your umbrella!"
                )

                print(f"Message sent with SID {message.sid}")
            elif "rain" not in weather_description:
                message = client.messages.create(
                    to = TO_NUMBER,
                    from_ = FROM_NUMBER,
                    body = "There is no rain today. Enjoy your day!"
                )

                print(f"Message sent with SID {message.sid}")

send_sms()