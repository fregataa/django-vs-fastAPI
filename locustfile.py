import time
import os
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    def on_start(self):
        TEST_ENV = os.environ["TEST_ENV"]
        if TEST_ENV == "sync":
            self.model = "books"
        elif TEST_ENV == "async":
            self.model = "async-books"
        else:
            print("Wrong ENV !!")
            assert False

        self.method = os.environ["METHOD"]
        if self.method not in ("get", "post"):
            print("Wrong METHOD !!")
            assert False

    def get_one():
        pass

    def get_all():
        pass

    @task
    def load_test_server(self):
        if self.method == "get":
            pass
        elif self.method == "post":

            self.client.post("/testapp/{self.model}/")
