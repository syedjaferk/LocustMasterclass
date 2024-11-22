from locust import HttpUser, constant, task
import uuid


class MyReqRes(HttpUser):

    wait_time = constant(1)
    host = "http://localhost:8001"

    @task
    def get_todos(self):
        res = self.client.get("/todos/104")
        print(res.text)

    @task
    def create_todos(self):
        request = {
            "id": str(uuid.uuid4()),
            "name": "Meet at 9 AM",
            "description": "Need to meet client at 9 AM tommorow"
        }
        res = self.client.post("/todos", json=request)
        print(res.text)
