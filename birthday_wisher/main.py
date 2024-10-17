import requests

response = requests.get("https://api.sheety.co/94bfc57e81196c71920460b02f378a1a/theRoster/sheet1")
print(response.status_code)
print(response.json())