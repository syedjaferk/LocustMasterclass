from locust import HttpUser, constant, task


class MyReqRes(HttpUser):

    wait_time = constant(1)
    host = "http://localhost:8001"

    @task
    def get_todos(self):
        with self.client.get("/todos/104", name="test todo", catch_response=True ) as resp1:
            if "Christian Adams" in resp1.json().get("name"):
                return resp1.success()
            else:
                return resp1.failure()
