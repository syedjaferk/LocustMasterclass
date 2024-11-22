from locust import User, task, between, constant, constant_pacing
from datetime import datetime

def print_datetime(useclass):
    print(datetime.now())

def print_greeting(userclass):
    print("Hello !")

class MyUser(User):

    wait_time = between(1, 5)

    tasks = [print_datetime, print_greeting]
