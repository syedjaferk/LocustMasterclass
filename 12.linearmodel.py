from locust import HttpUser, task, LoadTestShape, constant


class StepLoadShape(LoadTestShape):
    step_time = 60       # each step lasts 60 seconds
    step_users = 10      # add 10 users each step
    spawn_rate = 5       # spawn 5 users per second
    max_users = 100      # maximum of 100 users

    def tick(self):
        run_time = self.get_run_time()

        # calculate which step we are in
        current_step = run_time // self.step_time + 1
        if current_step * self.step_users > self.max_users:
            return None  # stop the test if we reach max_users

        user_count = current_step * self.step_users
        return user_count, self.spawn_rate


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

# locust -f 12.linearmodel.py -u 10 -r 1 --headless --step-load --step-users 2 --step-time 10s