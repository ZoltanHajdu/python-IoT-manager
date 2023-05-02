import time


class Communication:
    def __init__(self, url):
        self.url = url

    def send_data(self, data):
        print(f"Sending data to server {self.url} : {data}")
        time.sleep(2)
        print("Data sent")

    def get_data(self):
        print(f"Getting data from server {self.url}")
        time.sleep(2)
        print("Data received")

