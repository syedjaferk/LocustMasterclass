from locust import User, task, between


class MyUser(User):

    wait_time = between(1, 5)

    @task
    def login_url(self):
        print("I am logging in to the url")
