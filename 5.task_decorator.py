from locust import User, task, between, constant, constant_pacing
from datetime import datetime


class MyUser(User):

    wait_time = between(1, 5)

    @task
    def print_datetime(self):
        print(datetime.now())
    
    @task
    def print_greeting(self):
        print("Hello !")
