import random
import datetime
import time


class Sensor:

    lower_bound = 0
    upper_bound = 100
    steps = 1
    round = 5

    def __init__(self, name):
        self.name = name
        self.date = datetime.datetime.now().strftime("%H:%M:%S:%M")
        self.data1 = random.randrange(self.lower_bound, self.upper_bound, self.steps)
        self.data2 = round(random.SystemRandom().uniform(self.lower_bound, self.upper_bound), self.round)

    def __str__(self):
        return "{name}: {date} {data1} {data2}".\
            format(name=self.name, date=self.date, data1=self.data1, data2=self.data2)

    def update_sensor_data(self):
        self.date = datetime.datetime.now().strftime("%H:%M:%S")
        self.data1 = random.randrange(self.lower_bound, self.upper_bound, self.steps)
        self.data2 = round(random.SystemRandom().uniform(self.lower_bound, self.upper_bound), self.round)

    def get_sensor_data(self):
        return [self.name, self.date, self.data1, self.data2]
