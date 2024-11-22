from locust import User, TaskSet, task, constant

class RandomOrderTasks(TaskSet):
    @task(2)
    def task_one(self):
        print("Task one")
    
    @task(1)
    def task_two(self):
        print("Task two")

    @task(3)
    def task_three(self):
        print("Task Three")

class MyUser(User):
    tasks = [RandomOrderTasks]
    wait_time = constant(1)
