import requests
import random
import smtplib
import os

#-----Constants and Variables-----#
TOKEN = os.environ.get("TOKEN")
my_email = os.environ.get("my_email")
password = os.environ.get("password")
your_addy = "insert"
your_name = "insert"
sheety_endpoint = os.environ.get("sheety_endpoint")

#-----Headers-----#
headers = {
    "Authorization": TOKEN
}

#----Get Contacts Data----#
response = requests.get(url=sheety_endpoint, headers = headers)
sheet_data = response.json()

#-----Make Matches-----#
match1 = sheet_data["colleagues"][random.randint(1,len(sheet_data["colleagues"]))]["contact"]
match2 = sheet_data["colleagues"][random.randint(1, len(sheet_data["colleagues"]))]["contact"]
match3 = sheet_data["colleagues"][random.randint(1,len(sheet_data["colleagues"]))]["contact"]

#-----Send Email-----#
connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user = my_email, password =password)
connection.sendmail(from_addr=my_email,
                    to_addrs=your_addy,
                    msg = "Subject:TRB Reunion Brunch Speed Dating!\n\n"
                          f"Oh, {your_name}, thank you so much for participating in our little brunch-less experiment. "
                          f"I hope you make a great connection today! Here are your matches:\n\n"
                          f"{match1}\n"
                          f"{match2} and\n"
                          f"{match3}!\n\n"
                          f"Your matches don't know you've been paired with them, so it's up to you to reach out and take a chance!\n\n"
                          f"Best wishes,\n"
                          f"Holly")
connection.close()


