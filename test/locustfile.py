from locust import HttpLocust, TaskSet

def health(l):
    l.client.get("/test-fadhil/health")

def info(l):
    l.client.get("/test-fadhil/info")

class UserBehavior(TaskSet):
    tasks = {info: 2, health: 1}

    def on_start(self):
        health(self)
        info(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000