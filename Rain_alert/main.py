import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_data():
    api_key = API_KEY
    api_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Johannesburg"
    complete_url = api_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    
    # json method of response object 
    # convert json format data into
    # python format data
    data = response.json()
    print(data)

get_data()
