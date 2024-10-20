import requests
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_birthday_data():
    api_url = "https://api.sheety.co/94bfc57e81196c71920460b02f378a1a/birthdays/sheet1"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
#loop through the birthday data to see whose birthday is it based on the current date
        rows = data["sheet1"]

get_birthday_data()

def email_if_birthday():
    sender_email = "palesal613@gmail.com"
    sender_password = ""


    today = datetime.today()
    current_date = today.strftime("%d %B")
    print("Today's date:", current_date)


    server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
    server.login(sender_email, sender_password)

    rows = get_birthday_data()

    for row in rows:
        receiver_email = {row["email"]}
        if row["birthday"] == current_date:
            msg = MIMEMultipart("alternative")
            msg["Subject"] = "Test mail"
            msg["From"] = sender_email
            msg["To"] = receiver_email
            html = """
                <h1>HAPPY BIRTHDAY</h1
            """
            msg.attach(MIMEText(html, "html"))

            #send email
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print({row["name"]})
        else:
            print("its no one's birthday")
            
    server.quit()


email_if_birthday()


