from locust import HttpUser, constant, task


class MyReqRes(HttpUser):

    wait_time = constant(1)
    host = "http://localhost:8001"

    @task
    def get_todos(self):
        res = self.client.get("/todos/104")
        print(res.text)
