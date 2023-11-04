import smtplib
# connection2 = smtplib.SMTP("smtp.mail.yahoo.com")

my_email = "email to send from"
password = "Generared App password"


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() #Transport layer security, securing connection
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="email to send to", msg="Subject:Hello \n\n This is the body of the email")


