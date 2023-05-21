import os
import django
from django.conf import settings
import schedule
import time

# Переменной окружения
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# Инициализация Django
django.setup()

from letters.models import Client, Message, Mailing
from letters.mailer import Mailer

def run_mailer():

    current_time = time.localtime()
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
    print(formatted_time)
    mailer = Mailer()
    mailer.process_active_mailings()

def schedule_task():
    schedule.every(1).minutes.do(run_mailer)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    schedule_task()
