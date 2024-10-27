import requests
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
def get_birthday_data():
    API_URL = os.getenv("API_URL")
    response = requests.get(API_URL)

    if response.status_code == 200:
        data = response.json()
#loop through the birthday data to see whose birthday is it based on the current date
        return data["sheet1"]

get_birthday_data()

def email_if_birthday():
    sender_email = "palesal613@gmail.com"


    today = datetime.today()
    current_date = today.strftime("%d %B")
    print("Today's date:", current_date)


    server = smtplib.SMTP('smtp.googlemail.com', 587)
    server.starttls()
    server.login(sender_email, 'xrsbfmiehpqnsauo')

    rows = get_birthday_data()
    there_is_bday = False
    for row in rows:
        receiver_email = {row["email"]}
        if row["birthday"] == current_date:
            msg = MIMEMultipart("alternative")
            msg["Subject"] = "Test mail"
            msg["From"] = sender_email
            msg["To"] = receiver_email

            #send email
            server.sendmail(sender_email, receiver_email, "Happy Birthday! Wishing you a day filled with smiles, laughter, and all the good vibes. Enjoy every moment!")
            print(f"Sent birthday email to {row["name"]}")
            there_is_bday = True
            
    if there_is_bday is not True:
        print(f"It's no one's birthday today")
            
    server.quit()


email_if_birthday()


