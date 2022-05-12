import smtplib
import pandas
import datetime as dt
import random

my_email = "your mail"
my_pass = "your mail pass"
recipient_email = ''
recipient_name = ''
msg_content = ''
letters_list = ["letter_1", "letter_2", "letter_3"]


now = dt.datetime.now()
day_now = now.day
month_now = now.month

data = pandas.read_csv("birthdays.csv")
data_list = data.to_dict(orient='records')
for person in data_list:
    if person["month"] == month_now and person["day"] == day_now:
        print(f"Today is {person['name']}`s birthday")
        recipient_email = person["email"]
        recipient_name = person["name"]
        random_letter = random.choice(letters_list)
        with open(f"letter_templates/{random_letter}.txt") as file:
            file_content = file.read()
            msg_content = file_content.replace("[NAME]", recipient_name)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, my_pass)
            connection.sendmail(from_addr=my_email, to_addrs=recipient_email, msg=f"Subject:Birthday wish\n\n{msg_content}")




# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




