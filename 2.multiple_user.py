from locust import User, task, between


class MyWebUser(User):
    wait_time = between(1, 3)
    weight = 1

    @task
    def login_url(self):
        print("I am logging in to URL")


class MyMobileUser(User):
    wait_time = between(1, 3)
    weight = 2

    @task
    def login_url(self):
        print("I am logging in to URL 1")