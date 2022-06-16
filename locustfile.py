from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    wait_timme = between(5, 15)

    # def on_start(self):
    #     print("Starting up login Test...")

    @task
    def index(self):
        self.client.get("/")

    @task
    def index(self):
        self.client.post("/login", json={"userName": "vredenburgben@gmail.com", "password": "N7T5PpQz!"})