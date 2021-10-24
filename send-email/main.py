import datetime as dt
import random
import smtplib

now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()
date_of_birth = dt.datetime(year=1995,month=12,day=13,hour=4)

if day_of_week == 6:
    with open("quotes.txt") as file:
        f = file.readlines()
        quote = random.choice(f)

my_email = 'testForCoursesOlga@gmail.com'
password = 'password'
connection = smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email, to_addrs="testForCourse@yahoo.com",
                    msg=f"Subject:Hello\n\n {quote}")
connection.close()


# with smtplib.SMTP("smtp.gmail.com",587) as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="testForCourse@yahoo.com",
#                         msg="Subject:Hello\n\n Hello")


now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()

date_of_birth = dt.datetime(year=1995,month=12,day=13,hour=4)
