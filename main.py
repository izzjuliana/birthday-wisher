import smtplib
import datetime as dt
import random
import pandas

my_email = "INSERT_SOURCE_EMAIL"
password = "INSERT_SOURCE_PASSWORD"

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

current_month = dt.datetime.now().month
current_day = dt.datetime.now().day

if(current_month, current_day) in birthdays_dict:


    random_letter = random.randint(1, 3)

    letter = open(f"letter_templates/letter_{random_letter}.txt", "r").read()
    message = letter.replace("[NAME]", birthdays_dict[(current_month, current_day)]["name"])



    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthdays_dict[(current_month, current_day)]["email"],
            msg=f"Subject: Happy Birthday To The Most Special Person Ever!\n\n{message}"
         )




