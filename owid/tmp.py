import django

django.setup()

import json
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import *

from owid.text_owid import *
from owid.models import *
from main.secrets import *
from main.send_email import *

#CovidData.objects.all().delete(using='coviduk')
#Country.objects.all().delete(using='coviduk')

def read_json_file(filename):
    with open(filename, "r") as file:
        data_dict = json.load(file)
    db_models_exists = False

    status = []
    try:
        country_obj = Country.objects.using('owid').get(location=COUNTRY)
        db_models_exists = True
    except:
        error = Country.DoesNotExist
    if db_models_exists is True:
        country_obj = Country.objects.using('owid').get(location=COUNTRY)
        covid_data_objects = country_obj.coviddata_set.all()
        last_db_date = str(covid_data_objects[len(covid_data_objects) - 1].date)
        last_db_date_obj = datetime.datetime.strptime(last_db_date[:10], '%Y-%m-%d').date()
    else:
        last_db_date_obj = datetime.datetime.strptime('1950-01-01', '%Y-%m-%d').date()
    last_json_date = data_dict['USA']['data'][-1]['date']
    last_json_date_obj = datetime.datetime.strptime(last_json_date, '%Y-%m-%d').date()
    delta = last_json_date_obj - last_db_date_obj

    if not delta.days > 0:
        status.append('No new data')
    else:
        status.append('New data present')
        status.append('date_now: ' + str(datetime.now()))
        countries = Country.objects.using('owid').all()
        countries_name = [x.country_name for x in countries]
        print(countries_name)
        for k, v in data_dict.items():
            country = v['location']
            if country not in countries_name:
                status.append('adding new country: ' + country)

            for v1 in v['data']:
                data_date_obj = datetime.strptime(v1['date'], '%Y-%m-%d').date()
                delta_country = data_date_obj - last_db_date_obj
                if delta_country.days > 0:
                    status.append('adding data for: ' + data_date_obj.strftime('%Y-%m-%d'))

    return str(status)



def send_email(sender, receiver, subject, text):

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    html = text
    part2 = MIMEText(html, 'html')
    msg.attach(part2)
    # Send the message via gmail's regular server, over SSL - passwords are being sent, afterall
    s = smtplib.SMTP_SSL(SMTP_SERVER_GMAIL)
    # s.set_debuglevel(1)
    # do the smtp auth; sends ehlo if it hasn't been sent already
    s.login(LATITUDE99_LOGIN, LATIDUDE99_PSWD)
    s.sendmail(LATITUDE99_LOGIN, LATITUDE99_LOGIN, msg.as_string())
    s.quit()
    print('status email has been sent')



status = read_json_file(COVID_DATA_FILE_JSON)

send(LATITUDE99_LOGIN, LATITUDE99_LOGIN, 'Import json data into OWID DB status', status)



