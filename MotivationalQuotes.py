import datetime as dt
import smtplib, random

my_email = "email sending from"
password = " " #Email app password

time = dt.datetime.now()
current_day_week = time.weekday()

if current_day_week == 0:
    with open("quotes.txt") as quoate_file:
        all_quotes = quoate_file.readlines()
        random_quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="email sending to",
                             msg=f"Subject:Motivational Quote \n\n {random_quote} ")
        print("Email sent")
    
