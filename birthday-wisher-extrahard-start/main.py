##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib

now = dt.datetime.now()
date_today = now.date()

file = pandas.read_csv("birthdays.csv")
for ind in file.index:
    birthday = f'{now.year}-{file["month"][ind]}-{file["day"][ind]}'
    if birthday == str(date_today):
        letter = f'letter_{random.randint(1,3)}.txt'
        with open(f"letter_templates/{letter}") as file_wishes:
            sample = file_wishes.readlines()
        sample[0] = f'Dear {file["name"][ind]},\n'
        sample[-1] = f'Olga'
        message = ""
        message = message.join(sample)

        my_email = 'testForCoursesOlga@gmail.com'
        password = 'password'
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls() # call connection
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=str(file["email"][ind]),
                            msg=f'Subject:Happy birthday!!!\n\n {message}')
        connection.close()
