from locust import User, task, between, constant, constant_pacing
from datetime import datetime


class MyUser(User):

    wait_time = between(1, 5)

    def on_start(self):
        print("on start")

    def on_stop(self):
        print("on stop")

    @task
    def print_datetime(self):
        print(datetime.now())
