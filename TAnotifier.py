#!/usr/bin/env python3

from outlook import outlook
from outlook import config
import TAconfig
import os.path
from os import path
import datetime
import requests


# Get the last TA-mail using Outlook API/Package
def retrieve_last_mail():
    to_open = open(TAconfig.mail_log, 'w+')
    mail = outlook.Outlook()
    mail.login(TAconfig.mail_epitech, TAconfig.password)
    mail.select("INBOX/TA")
    id_list = mail.allIds()
    last_mail = id_list[-1]
    last_mail = last_mail[:-1]
    mail_content = mail.getEmail(last_mail)
    mail_content = str(mail_content)
    mail_content = mail_content.replace("\\r", '')
    mail_content = mail_content.replace("\\n", '\n')
    mail_content = mail_content.replace("\\t", '')
    print(mail_content, file=to_open)
    to_open.close()


def get_file_content(file):
    to_open = open(file, 'r')
    file_content = to_open.read()
    to_open.close()
    return file_content


def parse_content(content):
    return content.split('\n')


# Parsing the mail content to get the date
def fetch_date(array):
    date_line = array[14].split(' ')
    hour = date_line[5].split(':')
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return datetime.datetime(int(date_line[4]), months.index(date_line[3]) + 1, int(date_line[2]), int(hour[0]),
                             int(hour[1]), int(hour[2]))


retrieve_last_mail()

# Get the content and date of the last mail
last_mail_content = get_file_content(TAconfig.mail_log)
last_trace_array = parse_content(last_mail_content)
last_date = fetch_date(last_trace_array)

# Creates a latest_log if no backup available
if path.exists(TAconfig.latest_mail) is False:
    logs = open(TAconfig.latest_mail, "w+")
    print(last_mail_content, file=logs)
    logs.close()

# Get the content and date of the latest TA
latest_content = get_file_content(TAconfig.latest_mail)
latest_array = parse_content(latest_content)
latest_date = fetch_date(latest_array)

# If not a new TA, exits the program
if latest_date >= last_date:
    exit()

# Else, update the backup with the last mail received
logs = open(TAconfig.latest_mail, 'w+')
print(last_mail_content, file=logs)
logs.close()

# Get the TA's results from trace details to the end
trace_start_index = last_trace_array.index("See attached file trace.txt for details.")
result_array = last_trace_array[trace_start_index:]
activity_name = result_array[9]

i = 13
nbr_tests = 0
tests_passed = 0
while i < len(result_array):
    line = result_array[i].strip()
    if "test" in line:
        dash_idx = line.index('-')
        nb_test_exercise = line[(dash_idx + 1):-5]
        nbr_tests += int(nb_test_exercise)
        while '-' in result_array[i].strip():
            if "OK" in result_array[i+1].strip():
                tests_passed += 1
            i += 1
    i += 1
average = (tests_passed / nbr_tests) * 100
average = str(round(average, 1))

# API request to wirepusher.com
title = "Nouvelle TA"
message = activity_name + " : " + average + "%"
url_request = "https://wirepusher.com/send?id=" + TAconfig.wirepusher_token + "&title=" + title + "&message=" + message + "&type=" + TAconfig.alert_type + ("", "&action=" + TAconfig.action)[len(TAconfig.action) != 0]
response = requests.get(url_request)
# Deleting the temp. file and printing the API response
os.remove(TAconfig.mail_log)
print(response.status_code)
