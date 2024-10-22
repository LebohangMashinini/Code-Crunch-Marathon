import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_data():
    api_key = API_KEY
    api_url = "https://home.openweathermap.org/data/2.5/weather?"
    city_name = "Johannesburg"

    
