from locust import User, task, between
from datetime import datetime
from locust import events

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("on test start")

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("on test stop")

class MyUser(User):

    wait_time = between(1, 5)



    @task
    def print_datetime(self):
        print(datetime.now())
